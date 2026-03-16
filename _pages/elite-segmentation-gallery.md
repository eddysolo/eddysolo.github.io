---
layout: default
title: ELITE Segmentation Gallery
permalink: /elite-segmentation-gallery/
description: Dedicated visual and link hub for the tissue segmentation ELITE project.
nav: false
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="glass-section w-100 text-center mb-4" style="border-radius: 24px; padding: 3rem 2rem;">
    <h1 style="font-weight: 800; font-size: 2.6rem; margin-bottom: 0.6rem;">ELITE Segmentation Gallery</h1>
    <p style="font-size: 1.15rem; margin: 0; opacity: 0.9;">A focused page for project visuals and quick-access links.</p>
  </div>

  <div class="row g-4 mb-4">
    <div class="col-lg-8">
      <div class="glass-box p-3 h-100" style="border-radius: 20px;">
        {% include figure.liquid path="assets/img/publication_preview/breast scan example.png" title="Breast DCE MRI example used in segmentation-guided reconstruction" class="img-fluid rounded z-depth-1" %}
      </div>
    </div>
    <div class="col-lg-4">
      <div class="glass-box p-3 h-100" style="border-radius: 20px;">
        {% include figure.liquid path="assets/img/publication_preview/Multiple-Coil k-Space Interpolation Enhances Resolution.png" title="Multi-coil interpolation and reconstruction concept" class="img-fluid rounded z-depth-1" %}
      </div>
    </div>
  </div>

  <div class="row g-4 mb-4">
    <div class="col-lg-4">
      <div class="glass-box p-3 h-100" style="border-radius: 20px;">
        {% include figure.liquid path="assets/img/publication_preview/FastMRI Breast A Publicly Available Radial k-Space Dataset of Breast Dynamic Contrast-enhanced MRI.png" title="fastMRI Breast dataset publication visual" class="img-fluid rounded z-depth-1" %}
      </div>
    </div>
    <div class="col-lg-8">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 20px;">
        <h3 style="font-weight: 800; margin-bottom: 1rem; display: flex; align-items: center;">
          <i class="fa-solid fa-link mr-2" style="color: var(--global-theme-color);"></i>
          Project Links
        </h3>
        <a href="https://github.com/eddysolo/ELITE" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px;">
          <i class="fa-brands fa-github mr-2"></i>
          ELITE GitHub Repository
        </a>
        <a href="https://doi.org/10.21203/rs.3.rs-5448452/v1" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
          <i class="fa-solid fa-file-lines mr-2"></i>
          ELITE Preprint
        </a>
        <a href="https://doi.org/10.1148/ryai.240345" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-lg text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
          <i class="fa-solid fa-book-open mr-2"></i>
          fastMRI Breast Article
        </a>
      </div>
    </div>
  </div>

  <div class="text-center mb-5">
    <a href="{{ '/projects/' | relative_url }}" class="btn btn-outline-primary" style="font-weight: 700; border-radius: 12px; padding: 0.7rem 1.6rem; border-width: 2px;">
      <i class="fa-solid fa-arrow-left mr-2"></i>
      Back to Projects
    </a>
  </div>
</div>
