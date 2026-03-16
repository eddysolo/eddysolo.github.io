---
layout: page
title: projects
permalink: /projects/
description: A growing collection of your cool projects.
nav: false
nav_order: 3
display_categories: [work, fun]
horizontal: false
---

<div class="projects">
  <div class="row row-cols-1 row-cols-md-2">
    <div class="col">
      <div class="card h-100 glass-box">
        <div class="card-body d-flex flex-column align-items-start">
          <h2 class="card-title">Tissue Segmentation Model (ELITE)</h2>
          <p class="card-text mb-3">Segmentation-guided reconstruction pipeline for accelerated breast DCE MRI with robust temporal fidelity and reduced undersampling artifacts.</p>
          <img src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}" alt="Tissue segmentation model preview" style="width: 100%; max-width: 230px; height: auto; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.12);">
          <p class="card-text mt-3 mb-0" style="opacity: 0.85;">The project integrates tissue-prior segmentation with ELITE reconstruction to improve image quality in highly accelerated dynamic MRI scans.</p>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card h-100 hoverable glass-box">
        <div class="card-body d-flex flex-column">
          <h2 class="card-title">Future Project Slot</h2>
          <p class="card-text mb-2">This space is intentionally reserved for your next project.</p>
          <p class="card-text" style="opacity: 0.8;">Use this box later for title, short description, and relevant links once the new project is ready.</p>
          <span class="btn btn-outline-primary disabled mt-auto" aria-disabled="true">Coming Soon</span>
        </div>
      </div>
    </div>
  </div>
</div>
