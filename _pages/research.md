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

<style>
  .research-grid {
    row-gap: 1.35rem;
    margin-bottom: 2.4rem;
  }

  .research-card-link {
    text-decoration: none !important;
    background-image: none !important;
    color: inherit;
    display: block;
    height: 100%;
  }
  .research-card-link:hover {
    text-decoration: none !important;
    background-image: none !important;
  }

  .research-card {
    border-radius: 24px;
    border: 1px solid rgba(0, 150, 199, 0.24);
    padding: 1.4rem 1.3rem;
    height: 100%;
    display: flex;
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .research-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(0, 150, 199, 0.12);
  }

  .research-icon {
    font-size: 2.05rem;
    color: var(--global-theme-color);
    margin-bottom: 0.25rem;
  }

  .research-card h2 {
    font-weight: 800;
    font-size: 1.62rem;
    margin: 0;
    color: var(--global-theme-color);
    line-height: 1.25;
  }

  .research-card p {
    font-size: 1.01rem;
    line-height: 1.58;
    margin: 0;
  }

  @media (max-width: 767.98px) {
    .research-grid {
      row-gap: 1rem;
    }

    .research-card {
      padding: 1.15rem 1rem;
    }
  }
</style>

<div class="projects">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-4" style="border-radius: 24px; padding: 3.2rem 2.6rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.65rem;">Our Research</h1>
    <h3 style="font-weight: 600; font-size: 1.35rem; color: var(--global-theme-color); margin-bottom: 0;"></h3>
  </div>

  <div class="row g-4 research-grid">
    <div class="col-md-6">
      <a href="{{ '/computational-mri/' | relative_url }}" class="research-card-link">
        <div class="glass-box research-card">
          <div class="research-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z"/><path d="M12 10.5h-2.5l-1-1"/><path d="M12 14h-2"/><path d="M12 6h1.5l1.5-1.5h2"/><circle cx="18" cy="4.5" r="1"/><path d="M12 9h5"/><circle cx="18" cy="9" r="1"/><path d="M12 12h3"/><circle cx="16" cy="12" r="1"/><path d="M12 15h4.5"/><circle cx="17.5" cy="15" r="1"/><path d="M12 18h1.5l1.5 1.5h1"/><circle cx="17" cy="19.5" r="1"/></svg>
          </div>
          <h2>Computational MRI</h2>
          <p>Novel sampling and reconstruction strategies that turn accelerated k-space acquisitions into diagnostic-quality MRI.</p>
        </div>
      </a>
    </div>

    <div class="col-md-6">
      <a href="{{ '/motion-robust-mri/' | relative_url }}" class="research-card-link">
        <div class="glass-box research-card">
          <div class="research-icon">
            <i class="fa-solid fa-heart-pulse"></i>
          </div>
          <h2>Motion-Robust MRI</h2>
          <p>Free-breathing acquisition and correction pipelines designed for reliable brain and abdominal MRI.</p>
        </div>
      </a>
    </div>

    <div class="col-md-6">
      <a href="{{ '/advanced-mri-hardware/' | relative_url }}" class="research-card-link">
        <div class="glass-box research-card">
          <div class="research-icon">
            <i class="fa-solid fa-tower-broadcast"></i>
          </div>
          <h2>Advanced MRI Hardware</h2>
          <p>MR-compatible sensing and external tracking frameworks enabling robust free-motion and free-breathing MRI.</p>
        </div>
      </a>
    </div>

    <div class="col-md-6">
      <a href="{{ '/quantitative-diffusion-mri/' | relative_url }}" class="research-card-link">
        <div class="glass-box research-card">
          <div class="research-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 15c6.667-6 13.333 0 20-6"/><path d="M9 22c1.798-1.998 2.518-3.995 2.808-5.993"/><path d="M15 2c-1.798 1.998-2.518 3.995-2.808 5.993"/><path d="m17 6-2.5-2.5"/><path d="m14 8-1-1"/><path d="m7 18 2.5 2.5"/><path d="m3.5 14.5.5.5"/><path d="m20 9 .5.5"/><path d="m6.5 12.5 1 1"/><path d="m16.5 10.5 1 1"/><path d="m10 16 1.5 1.5"/></svg>
          </div>
          <h2>Quantitative Diffusion MRI</h2>
          <p>Advanced diffusion MRI for probing tissue microstructure, heterogeneity, and cellular dynamics.</p>
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
