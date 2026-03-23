---
layout: default
title: Non-Cartesian Imaging
permalink: /non-cartesian-imaging/
fluid: true
no_hero: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="row g-4 mb-4 align-items-stretch">
    <div class="col-lg-8">
      <div class="glass-box p-4 p-md-5 h-100 d-flex flex-column justify-content-center" style="border-radius: 24px; font-size: 1.25rem; line-height: 1.6;">
        <h2 style="font-weight: 800; margin-bottom: 1.5rem; display: flex; align-items: center;"><i class="fa-solid fa-circle-nodes fa-lg mr-3" style="color: var(--global-theme-color);"></i> The Concept</h2>
        <p>
          Traditional MRI usually samples k-space on a Cartesian grid, line-by-line. In contrast, <strong>Non-Cartesian Imaging</strong> acquires data along trajectories such as radial spokes, spirals, and stack-of-stars patterns. These trajectories improve sampling efficiency and naturally spread undersampling artifacts in a more manageable way.
        </p>
        <p class="mb-0">
          Our lab develops end-to-end non-Cartesian pipelines that combine physics-based forward models, robust density compensation, and modern model-based reconstruction. The outcome is faster scans, stronger motion resilience, and practical free-breathing protocols for brain, breast, abdominal, and body MRI applications.
        </p>
      </div>
    </div>

    <div class="col-lg-4">
      <div class="glass-box p-4 h-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(0,0,0,0.05);">
        <img src="{{ 'assets/img/publication_preview/GRASP acquisition diagram.jpg' | relative_url }}" alt="Non-Cartesian MRI trajectory diagram" style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
      </div>
    </div>
  </div>

  <div class="glass-section mb-4" style="border-radius: 24px; padding: 3rem;">
    <h3 style="font-weight: 800; font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center;"><i class="fa-solid fa-book-open fa-md mr-3" style="color: var(--global-theme-color);"></i> Relevant Articles</h3>
    <div class="row g-4 justify-content-center">
      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-file-waveform fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">fastMRI Breast: radial k-space dataset for DCE MRI</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Radiology: AI (2024)</p>
          </div>
        </a>
      </div>

      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-wind fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">Free-breathing radial MRI using pilot-tone motion tracking</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Magnetic Resonance in Medicine (2020)</p>
          </div>
        </a>
      </div>

      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-layer-group fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">MP-RAVE stack-of-stars reconstruction with retrospective correction</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Magnetic Resonance in Medicine (2023)</p>
          </div>
        </a>
      </div>
    </div>
  </div>

</div>
