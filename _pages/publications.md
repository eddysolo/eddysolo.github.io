---
layout: page
permalink: /publications/
title: Publications
description: Full indexed list of journal and conference publications with external links to Google Scholar and PubMed.
nav: true
nav_order: 4
hide_page_header: true
_styles: |
  .pub-page-note {
    margin: 0 0 1rem;
    font-size: 1rem;
    line-height: 1.6;
    text-align: left;
  }

  .pub-page-note a {
    font-weight: 800;
    text-decoration: underline;
    text-underline-offset: 0.14rem;
  }

  .pub-tabs-wrap {
    background: linear-gradient(135deg, rgba(0, 150, 199, 0.16) 0%, rgba(0, 150, 199, 0.08) 100%);
    border: 1px solid rgba(0, 150, 199, 0.28);
    border-radius: 20px;
    padding: 0.8rem;
    margin: 1rem 0 1.1rem;
  }

  .pub-tabs-wrap .nav-link {
    border-radius: 999px;
    padding: 0.78rem 1.45rem;
    font-weight: 700;
    margin: 0 0.3rem;
    color: var(--global-text-color);
    background: rgba(0, 150, 199, 0.12);
    border: 1px solid rgba(0, 150, 199, 0.24);
    transition: all 0.2s ease;
  }

  .pub-tabs-wrap .nav-link:hover {
    border-color: rgba(0, 150, 199, 0.5);
    background: rgba(0, 150, 199, 0.18);
  }

  .pub-tabs-wrap .nav-link.active {
    background: var(--global-theme-color);
    color: #fff;
    box-shadow: 0 10px 24px rgba(0, 150, 199, 0.28);
  }

  .publications h2,
  .publications h2.year {
    color: #6f7681;
    font-weight: 820;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-size: clamp(1.1rem, 1.5vw, 1.4rem);
    margin: 1.4rem 0 0.85rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid rgba(111, 118, 129, 0.35);
  }

  .publications ol.bibliography li .periodical,
  .publications ol.bibliography li .periodical em,
  html[data-theme="dark"] .publications ol.bibliography li .periodical,
  html[data-theme="dark"] .publications ol.bibliography li .periodical em {
    color: #111424 !important;
  }

  /* Peer Reviewed tab: remove preview figure column and expand content cards. */
  #peer-pane .abbr {
    display: none;
  }

  #peer-pane .col-sm-10 {
    flex: 0 0 100%;
    max-width: 100%;
  }

  @media (max-width: 768px) {
    .pub-tabs-wrap .nav-link {
      margin: 0.2rem;
      font-size: 0.93rem;
      padding: 0.65rem 1rem;
    }
  }
---

<!-- _pages/publications.md -->

<div class="glass-section pub-page-shell">
  <div class="glass-section-body">
<p class="pub-page-note">For a full list, you can visit <a href="https://scholar.google.com/citations?user=tAOr0VwAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Google Scholar</a> or <a href="https://pubmed.ncbi.nlm.nih.gov/?term=eddy+solomon&sort=date&utm_source=Pubmed" target="_blank" rel="noopener noreferrer">PubMed</a>.</p>

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">
  <!-- Tabs Navigation -->
  <div class="pub-tabs-wrap">
    <ul class="nav nav-pills justify-content-center" id="pub-tabs" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="journal-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#journal-pane" data-bs-target="#journal-pane" type="button" role="tab" aria-controls="journal-pane" aria-selected="true">Journal Articles</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="peer-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#peer-pane" data-bs-target="#peer-pane" type="button" role="tab" aria-controls="peer-pane" aria-selected="false">Peer Reviewed Conference Abstracts</button>
      </li>
    </ul>
  </div>

  <!-- Tabs Content -->
  <div class="tab-content" id="pub-tabs-content">
    <div class="tab-pane fade show active" id="journal-pane" role="tabpanel" aria-labelledby="journal-tab">
      {% bibliography --query @article{*} --group_by year --sort_by year --order descending %}
    </div>
    
    <div class="tab-pane fade" id="peer-pane" role="tabpanel" aria-labelledby="peer-tab">
      {% bibliography --query @inproceedings{*} --group_by year --sort_by year --order descending %}
    </div>
  </div>
</div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  // Normalize 0000 headings so they are human-readable.
  document.querySelectorAll(".bibliography h2, h2.year, .tab-pane h2").forEach(function(h) {
    if (h.textContent.trim() === "0000") {
      h.textContent = "Unknown Year";
    }
  });

  // Move Unknown Year entries from Journal Articles to Conference Abstracts,
  // but keep only the entries (remove the Unknown Year heading box).
  const journalPane = document.getElementById("journal-pane");
  const peerPane = document.getElementById("peer-pane");
  if (!journalPane || !peerPane) return;

  const journalHeadings = Array.from(journalPane.querySelectorAll("h2, h2.year"));
  journalHeadings.forEach(function(heading) {
    const yearText = heading.textContent.trim();
    if (yearText !== "Unknown Year" && yearText !== "0000") return;

    let nextNode = heading.nextElementSibling;
    const entriesToMove = [];

    while (nextNode && nextNode.tagName.toLowerCase() !== "h2") {
      const current = nextNode;
      nextNode = nextNode.nextElementSibling;
      entriesToMove.push(current);
    }

    heading.remove();
    entriesToMove.forEach(function(node) {
      peerPane.appendChild(node);
    });
  });



  // Remove duplicate bibliography cards by DOI first, and by normalized title as fallback.
  const seen = new Set();
  const allRows = Array.from(document.querySelectorAll("#journal-pane .bibliography .row, #peer-pane .bibliography .row"));

  allRows.forEach(function(row) {
    const titleNode = row.querySelector(".title");
    if (!titleNode) return;

    const titleText = titleNode.textContent.trim().toLowerCase().replace(/\s+/g, " ");

    let doi = "";
    const titleLink = titleNode.querySelector("a[href]");
    if (titleLink) {
      const href = titleLink.getAttribute("href") || "";
      const doiMatch = href.match(/doi\.org\/(.+)$/i);
      if (doiMatch && doiMatch[1]) {
        doi = doiMatch[1].toLowerCase();
      }
    }

    if (!doi) {
      const doiButton = row.querySelector('.links a[href*="doi.org/"]');
      if (doiButton) {
        const href = doiButton.getAttribute("href") || "";
        const doiMatch = href.match(/doi\.org\/(.+)$/i);
        if (doiMatch && doiMatch[1]) {
          doi = doiMatch[1].toLowerCase();
        }
      }
    }

    const dedupeKey = doi ? `doi:${doi}` : `title:${titleText}`;
    if (seen.has(dedupeKey)) {
      row.remove();
      return;
    }
    seen.add(dedupeKey);
  });

  // In Peer Reviewed Conference Abstracts tab, hide verbose unknown venue stamp
  // and remove PDF badges from entry cards.
  peerPane.querySelectorAll(".periodical").forEach(function(node) {
    const text = (node.textContent || "").replace(/\s+/g, " ").trim();
    if (text.includes("ISMRM Annual Meeting") && text.includes("0000")) {
      const cleaned = text
        .replace(/ISMRM\s+Annual\s+Meeting\s*,?\s*0000/gi, "")
        .replace(/^\s*[.,;:-]\s*/, "")
        .trim();

      if (cleaned) {
        node.textContent = cleaned;
      } else {
        node.remove();
      }
    }
  });

  peerPane.querySelectorAll(".links a").forEach(function(link) {
    const label = (link.textContent || "").trim().toLowerCase();
    if (label === "pdf") {
      link.remove();
    }
  });

  ["solomon20134288robustdiffusionwe"].forEach(function(entryId) {
    const entry = document.getElementById(entryId);
    const card = entry?.closest("li") || entry?.closest(".row");
    if (card) {
      card.remove();
    }
  });

  // Remove any peer-reviewed cards that render with no visible citation content.
  peerPane.querySelectorAll(".bibliography .row").forEach(function(row) {
    const titleText = (row.querySelector(".title")?.textContent || "").replace(/\s+/g, " ").trim();
    const authorText = (row.querySelector(".author")?.textContent || "").replace(/\s+/g, " ").trim();
    const periodicalText = Array.from(row.querySelectorAll(".periodical"))
      .map(function(node) {
        return (node.textContent || "").replace(/\s+/g, " ").trim();
      })
      .join(" ")
      .trim();

    if (!titleText || !authorText || !periodicalText) {
      const card = row.closest("li") || row;
      card.remove();
    }
  });

});
</script>
