import json
import re
import ssl
import urllib.parse
import urllib.request
from typing import Dict, List


AUTHOR_QUERY = "Eddy Solomon"
API_BASE = "https://api.semanticscholar.org/graph/v1"
BIB_FILE = "_bibliography/papers.bib"
FEATURED_FILE = "_data/open_science.yml"
PAGE_SIZE = 100


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {"User-Agent": "Mozilla/5.0"}


def api_get(url: str) -> Dict:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode("utf-8"))


def bib_safe(value: str) -> str:
    if value is None:
        return ""
    return value.replace("{", "\\{").replace("}", "\\}").replace("\n", " ").strip()


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def make_unique_key(base_key: str, key_counts: Dict[str, int]) -> str:
    if base_key not in key_counts:
        key_counts[base_key] = 1
        return base_key
    key_counts[base_key] += 1
    return f"{base_key}{key_counts[base_key]}"


def find_author_ids() -> List[str]:
    query = urllib.parse.quote_plus(AUTHOR_QUERY)
    search_url = (
        f"{API_BASE}/author/search?query={query}&fields=authorId,name,paperCount&limit=20"
    )
    data = api_get(search_url)
    authors = data.get("data", [])
    if not authors:
        raise RuntimeError(f"No author found for query: {AUTHOR_QUERY}")

    # Primary profile: highest paper-count result for this query.
    primary = max(authors, key=lambda a: a.get("paperCount", 0))

    # Merge split profiles with exact Eddy Solomon naming.
    exact_eddy = [
        a for a in authors if a.get("name", "").strip().lower() == AUTHOR_QUERY.lower()
    ]

    selected = [primary]
    for author in exact_eddy:
        if author.get("authorId") != primary.get("authorId"):
            selected.append(author)

    author_ids = [a.get("authorId") for a in selected if a.get("authorId")]
    if not author_ids:
        raise RuntimeError("No authorIds returned by Semantic Scholar.")

    print("Selected Semantic Scholar author profiles:")
    for author in selected:
        print(
            f"- {author.get('name')} (ID: {author.get('authorId')}, papers: {author.get('paperCount', 0)})"
        )

    return author_ids


def fetch_all_papers(author_ids: List[str]) -> List[Dict]:
    fields = "title,year,authors,venue,externalIds,url,openAccessPdf,paperId,citationCount"
    papers: List[Dict] = []

    for author_id in author_ids:
        offset = 0
        while True:
            papers_url = (
                f"{API_BASE}/author/{author_id}/papers?fields={fields}&limit={PAGE_SIZE}&offset={offset}"
            )
            payload = api_get(papers_url)
            batch = payload.get("data", [])
            if not batch:
                break
            papers.extend(batch)

            print(
                f"Fetched {len(batch)} papers from author {author_id} (total so far: {len(papers)})."
            )

            if len(batch) < PAGE_SIZE:
                break
            offset += PAGE_SIZE

    deduped = {}
    for paper in papers:
        paper_id = paper.get("paperId")
        if paper_id:
            deduped[paper_id] = paper

    return list(deduped.values())


def write_bibtex(papers: List[Dict]) -> List[Dict]:
    # Sort newest first, then title for stable output.
    papers.sort(key=lambda p: (p.get("year") or 0, p.get("title") or ""), reverse=True)

    key_counts: Dict[str, int] = {}
    entries_for_featured: List[Dict] = []

    with open(BIB_FILE, "w", encoding="utf-8") as f:
        for paper in papers:
            title = bib_safe(paper.get("title") or "Unknown Title")
            year = paper.get("year") or "0000"

            authors_list = paper.get("authors", [])
            author_names = [a.get("name", "") for a in authors_list if a.get("name")]
            authors_str = " and ".join(author_names) if author_names else "Unknown"

            venue = bib_safe(paper.get("venue") or "")
            entry_type = "article" if venue else "misc"

            first_author_last = (
                author_names[0].split()[-1] if author_names and author_names[0].split() else "paper"
            )
            title_chunk = slugify((paper.get("title") or "")[:24]) or "untitled"
            base_key = slugify(f"{first_author_last}{year}{title_chunk}") or "paper"
            cite_key = make_unique_key(base_key, key_counts)

            external_ids = paper.get("externalIds") or {}
            doi = bib_safe(external_ids.get("DOI") or "")
            html_url = bib_safe(paper.get("url") or "")

            open_access_pdf = paper.get("openAccessPdf") or {}
            pdf_url = bib_safe(open_access_pdf.get("url") or "")
            citation_count = int(paper.get("citationCount") or 0)
            preview_file = f"{cite_key}.jpg"

            f.write(f"@{entry_type}{{{cite_key},\n")
            f.write(f"  title={{{title}}},\n")
            f.write(f"  author={{{bib_safe(authors_str)}}},\n")
            if venue:
                f.write(f"  journal={{{venue}}},\n")
            f.write(f"  year={{{year}}},\n")
            if doi:
                f.write(f"  doi={{{doi}}},\n")
            if html_url:
                pass
                # Semantic Scholar landing page link
                # f.write(f"  html={{{html_url}}},\n")
            if pdf_url:
                # Open-access PDF when available
                f.write(f"  pdf={{{pdf_url}}},\n")
            # Add a local preview image placeholder; user can drop figure files here.
            f.write(f"  preview={{{preview_file}}},\n")
            f.write("}\n\n")

            entries_for_featured.append(
                {
                    "key": cite_key,
                    "title": title,
                    "year": int(year) if isinstance(year, int) or str(year).isdigit() else 0,
                    "citation_count": citation_count,
                    "html": html_url,
                    "doi": doi,
                    "pdf": pdf_url,
                    "preview": preview_file,
                }
            )

    return entries_for_featured


def write_featured_publications(entries: List[Dict]) -> None:
    if not entries:
        raise RuntimeError("No entries available for featured publications output.")

    latest = max(entries, key=lambda e: (e.get("year", 0), e.get("citation_count", 0)))
    most_cited = max(entries, key=lambda e: (e.get("citation_count", 0), e.get("year", 0)))

    def to_yaml_block(block_name: str, entry: Dict) -> str:
        def q(value: str) -> str:
            escaped = (value or "").replace("\\", "\\\\").replace('"', '\\"')
            return f'"{escaped}"'

        return "\n".join(
            [
                f"{block_name}:",
                f"  key: {q(entry.get('key', ''))}",
                f"  title: {q(entry.get('title', ''))}",
                f"  year: {entry.get('year', 0)}",
                f"  citation_count: {entry.get('citation_count', 0)}",
                f"  html: {q(entry.get('html', ''))}",
                f"  doi: {q(entry.get('doi', ''))}",
                f"  pdf: {q(entry.get('pdf', ''))}",
                f"  preview: {q(entry.get('preview', ''))}",
            ]
        )

    yaml_content = (
        "metadata:\n"
        f"  generated_from: \"Semantic Scholar\"\n"
        f"  author_query: \"{AUTHOR_QUERY}\"\n"
        + to_yaml_block("latest", latest)
        + "\n"
        + to_yaml_block("most_cited", most_cited)
        + "\n"
    )

    with open(FEATURED_FILE, "w", encoding="utf-8") as f:
        f.write(yaml_content)


def main() -> None:
    author_ids = find_author_ids()
    papers = fetch_all_papers(author_ids)
    print(f"Fetched {len(papers)} unique papers from Semantic Scholar.")

    if not papers:
        raise RuntimeError("No papers were fetched. Aborting bibliography generation.")

    entries = write_bibtex(papers)
    write_featured_publications(entries)
    print(f"Successfully generated {BIB_FILE} with {len(papers)} entries.")
    print(f"Successfully generated {FEATURED_FILE} for Open Science highlights.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error fetching data: {exc}")
        raise
