---
layout: page
permalink: /publications/
title: Publications
description: 'For a full list, visit <a href="https://scholar.google.com/citations?user=tAOr0VwAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Google Scholar</a> or <a href="https://pubmed.ncbi.nlm.nih.gov/?term=Eddy+Solomon" target="_blank" rel="noopener noreferrer">PubMed</a>.'
nav: true
nav_order: 4
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->
{% include bib_search.liquid %}

<div class="publications">
  <!-- Tabs Navigation -->
  <ul class="nav nav-pills justify-content-center mb-4" id="pub-tabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="journal-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#journal-pane" data-bs-target="#journal-pane" type="button" role="tab" aria-controls="journal-pane" aria-selected="true" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Journal articles</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="peer-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#peer-pane" data-bs-target="#peer-pane" type="button" role="tab" aria-controls="peer-pane" aria-selected="false" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Peer Reviewed Conference Abstracts</button>
    </li>
  </ul>

  <!-- Tabs Content -->
  <div class="tab-content" id="pub-tabs-content">
    <div class="tab-pane fade show active" id="journal-pane" role="tabpanel" aria-labelledby="journal-tab">
      {% bibliography --query @article{*} --group_by year --sort_by year --order descending %}
    </div>
    
    <div class="tab-pane fade" id="peer-pane" role="tabpanel" aria-labelledby="peer-tab">
      {% bibliography --query @inproceedings{*} --group_by year --sort_by year --order descending %}
      {% bibliography --query @incollection{*} --group_by year --sort_by year --order descending %}
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

  // Remove Unknown Year heading in Conference Abstracts while keeping entries/cards/links.
  const yearHeadings = Array.from(peerPane.querySelectorAll("h2, h2.year"));
  yearHeadings.forEach(function(heading) {
    const yearText = heading.textContent.trim();
    if (yearText === "Unknown Year" || yearText === "0000") {
      heading.remove();
    }
  });
});
</script>
