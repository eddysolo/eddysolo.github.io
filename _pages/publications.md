---
layout: page
permalink: /publications/
title: publications
description: Publications organized by category and year.
nav: false
nav_order: 2
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
      <button class="nav-link" id="peer-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#peer-pane" data-bs-target="#peer-pane" type="button" role="tab" aria-controls="peer-pane" aria-selected="false" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Peer reviewed featured publications</button>
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
  document.querySelectorAll(".bibliography h2, h2.year, .tab-pane h2").forEach(function(h) {
    if (h.textContent.trim() === "0000") {
      h.textContent = "Unknown Year";
    }
  });
});
</script>
