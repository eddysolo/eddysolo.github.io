---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 3
hide_page_header: true
display_categories: [work, fun]
horizontal: false
---

<div class="projects">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-4" style="border-radius: 24px; padding: 3.2rem 2.6rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.65rem;">Our Research</h1>
    <h3 style="font-weight: 600; font-size: 1.35rem; color: var(--global-theme-color); margin-bottom: 0;"></h3>
  </div>

  <div class="row g-4 mb-5">
    <div class="col-lg-4">
      <a href="{{ '/computational-mri/' | relative_url }}" class="text-decoration-none" style="color: inherit;">
        <div class="glass-box p-4 h-100 d-flex flex-column text-center" style="border-radius: 24px; border: 1px solid rgba(0, 150, 199, 0.28);">
          <div class="mb-3" style="font-size: 2rem; color: var(--global-theme-color);">
            <i class="fa-solid fa-microchip"></i>
          </div>
          <h2 style="font-weight: 800; font-size: 1.65rem; margin-bottom: 0.55rem; color: var(--global-theme-color);">Computational MRI</h2>
          <p style="font-size: 1.05rem; line-height: 1.6; margin: 0;">Novel sampling and reconstruction methods that transform accelerated k-space acquisitions into diagnostic-quality images.</p>
        </div>
      </a>
    </div>

    <div class="col-lg-4">
      <a href="{{ '/motion-correction/' | relative_url }}" class="text-decoration-none" style="color: inherit;">
        <div class="glass-box p-4 h-100 d-flex flex-column text-center" style="border-radius: 24px; border: 1px solid rgba(0, 150, 199, 0.28);">
          <div class="mb-3" style="font-size: 2rem; color: var(--global-theme-color);">
            <i class="fa-solid fa-wave-square"></i>
          </div>
          <h2 style="font-weight: 800; font-size: 1.65rem; margin-bottom: 0.55rem; color: var(--global-theme-color);">Motion Correction</h2>
          <p style="font-size: 1.05rem; line-height: 1.6; margin: 0;">Free-breathing and motion-robust MRI pipelines designed to improve stability across pediatric and abdominal imaging.</p>
        </div>
      </a>
    </div>

    <div class="col-lg-4">
      <a href="{{ '/advanced-hardware/' | relative_url }}" class="text-decoration-none" style="color: inherit;">
        <div class="glass-box p-4 h-100 d-flex flex-column text-center" style="border-radius: 24px; border: 1px solid rgba(0, 150, 199, 0.28);">
          <div class="mb-3" style="font-size: 2rem; color: var(--global-theme-color);">
            <i class="fa-solid fa-satellite-dish"></i>
          </div>
          <h2 style="font-weight: 800; font-size: 1.65rem; margin-bottom: 0.55rem; color: var(--global-theme-color);">Advanced Hardware</h2>
          <p style="font-size: 1.05rem; line-height: 1.6; margin: 0;">MR-compatible sensing, external tracking, and instrumentation that extend what is measurable in real scans.</p>
        </div>
      </a>
    </div>
  </div>

  <div style="display: none;" aria-hidden="true">
    <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-4" style="border-radius: 24px; padding: 2.4rem 2.2rem;">
      <h2 style="font-weight: 800; font-size: 2.3rem; margin-bottom: 0.5rem;">Projects</h2>
      <p style="font-size: 1.1rem; margin: 0; max-width: 980px; line-height: 1.7;">Selected implementations from our lab, including practical software, reconstruction frameworks, and translational tools that support robust MRI research.</p>
    </div>

    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col">
        <div class="card h-100 glass-box" style="border-radius: 24px;">
          <div class="card-body d-flex flex-column align-items-start">
            <h2 class="card-title">Tissue Segmentation Model (ELITE)</h2>
            <p class="card-text mb-3">Segmentation-guided reconstruction pipeline for accelerated breast DCE MRI with robust temporal fidelity and reduced undersampling artifacts.</p>
            <img src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}" alt="Tissue segmentation model preview" style="width: 100%; max-width: 230px; height: auto; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.12);">
            <p class="card-text mt-3 mb-0" style="opacity: 0.85;">The project integrates tissue-prior segmentation with ELITE reconstruction to improve image quality in highly accelerated dynamic MRI scans.</p>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100 hoverable glass-box" style="border-radius: 24px;">
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
</div>
