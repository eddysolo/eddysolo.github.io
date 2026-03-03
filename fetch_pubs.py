import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. Search for author 'Eddy Solomon' to get the authorId
author_search_url = "https://api.semanticscholar.org/graph/v1/author/search?query=Eddy+Solomon&fields=authorId,name,paperCount"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    req = urllib.request.Request(author_search_url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as response:
        data = json.loads(response.read().decode('utf-8'))
        authors = data.get('data', [])
        
        if not authors:
            print("No author found on Semantic Scholar.")
            exit(1)
            
        # Pick the most likely (highest paper count)
        author = max(authors, key=lambda x: x.get('paperCount', 0))
        author_id = author['authorId']
        print(f"Found author: {author['name']} (ID: {author_id}) with {author['paperCount']} papers.")

        # 2. Fetch works for this authorId
        works_url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers?fields=title,year,authors,venue,externalIds&limit=100"
        req = urllib.request.Request(works_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx) as r:
            works_data = json.loads(r.read().decode('utf-8'))
            papers = works_data.get('data', [])
            
            print(f"Fetched {len(papers)} papers. Sorting by year...")
            
            # Sort newest first
            valid_papers = [p for p in papers if p.get('year') is not None]
            valid_papers.sort(key=lambda x: x['year'], reverse=True)
            top_20 = valid_papers[:20]

            with open('_bibliography/papers.bib', 'w', encoding='utf-8') as f:
                for w in top_20:
                    title = w.get('title', 'Unknown Title')
                    year = w.get('year', 'Unknown Year')
                    
                    authors_list = w.get('authors', [])
                    author_names = [a.get('name', '') for a in authors_list]
                    authors_str = " and ".join(filter(None, author_names)) if author_names else "Unknown"
                    
                    venue = w.get('venue', '')
                    if not venue:
                        venue = 'Unknown Journal'
                    
                    first_author = author_names[0].split()[-1] if author_names else "Unknown"
                    cite_key = "".join(filter(str.isalnum, f"{first_author}{year}{title[:8]}".lower()))
                    entry_type = 'article' if venue != 'Unknown Journal' else 'misc'
                    
                    doi = w.get('externalIds', {}).get('DOI', '')
                    
                    f.write(f"@{entry_type}{{{cite_key},\n")
                    f.write(f"  title={{{title}}},\n")
                    f.write(f"  author={{{authors_str}}},\n")
                    f.write(f"  journal={{{venue}}},\n")
                    f.write(f"  year={{{year}}},\n")
                    if doi:
                        f.write(f"  doi={{{doi}}},\n")
                    f.write("}\n\n")

            print("Successfully generated _bibliography/papers.bib from Semantic Scholar.")

except Exception as e:
    print(f"Error fetching data: {e}")
