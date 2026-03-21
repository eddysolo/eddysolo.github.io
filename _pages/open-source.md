---
layout: default
title: Open Source
permalink: /open-source/
description: Open-source software and code repositories from the Solomon's MRI Lab.
nav: true
nav_order: 5
fluid: true
---

<style>
  .open-source-tabs-wrap {
    background: linear-gradient(135deg, rgba(0, 150, 199, 0.1) 0%, rgba(0, 150, 199, 0.03) 100%);
    border: 1px solid rgba(0, 150, 199, 0.18);
    border-radius: 20px;
    padding: 0.8rem;
    margin-top: -0.5rem;
    margin-bottom: 1.2rem;
  }

  .open-source-tabs-wrap .nav-link {
    border-radius: 999px;
    padding: 0.78rem 1.45rem;
    font-weight: 700;
    margin: 0 0.3rem;
    color: var(--global-text-color);
    border: 1px solid transparent;
    transition: all 0.2s ease;
  }

  .open-source-tabs-wrap .nav-link:hover {
    border-color: rgba(0, 150, 199, 0.35);
    background: rgba(0, 150, 199, 0.08);
  }

  .open-source-tabs-wrap .nav-link.active {
    background: var(--global-theme-color);
    color: #fff;
    box-shadow: 0 10px 24px rgba(0, 150, 199, 0.28);
  }

  .open-source-tab-hero {
    border-radius: 20px;
    padding: 1.5rem 1.4rem;
    margin-bottom: 1.1rem;
    border: 1px solid rgba(0, 150, 199, 0.2);
    background: linear-gradient(130deg, rgba(255, 255, 255, 0.08), rgba(0, 150, 199, 0.06));
  }

  .open-source-repo-card .repo-title-row {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    margin-bottom: 0.85rem;
  }

  .open-source-repo-card .repo-title-row i {
    flex-shrink: 0;
    margin-top: 0.1rem;
  }

  .open-source-repo-card .repo-title-row h3 {
    margin: 0;
    font-size: 1.02rem;
    line-height: 1.35;
    font-weight: 800;
    overflow-wrap: anywhere;
    word-break: break-word;
  }

  .open-source-code-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.5rem;
    margin-bottom: 1rem;
  }

  .open-source-code-grid .open-source-repo-card {
    min-width: 0;
  }

  @media (max-width: 767px) {
    .open-source-code-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 768px) {
    .open-source-tabs-wrap .nav-link {
      margin: 0.2rem;
      font-size: 0.93rem;
      padding: 0.65rem 1rem;
    }
  }
</style>

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="open-source-tabs-wrap">
    <ul class="nav nav-pills justify-content-center" id="open-source-tabs" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="source-code-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#source-code-pane" data-bs-target="#source-code-pane" type="button" role="tab" aria-controls="source-code-pane" aria-selected="true">Code &amp; Repositories</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="source-popular-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#source-popular-pane" data-bs-target="#source-popular-pane" type="button" role="tab" aria-controls="source-popular-pane" aria-selected="false">Popular Science</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="source-patents-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#source-patents-pane" data-bs-target="#source-patents-pane" type="button" role="tab" aria-controls="source-patents-pane" aria-selected="false">Patents</button>
      </li>
    </ul>
  </div>

  <div class="tab-content" id="open-source-content">
    <div class="tab-pane fade show active" id="source-code-pane" role="tabpanel" aria-labelledby="source-code-tab">
      <div class="glass-section open-source-tab-hero d-flex flex-column justify-content-center align-items-center text-center">
        <h2 style="font-weight: 800; font-size: 2rem; margin-bottom: 0.4rem;">Code &amp; Repositories</h2>
        <p style="font-size: 1.08rem; margin: 0; max-width: 980px; line-height: 1.65;">Open-source tools and reproducible codebases from our lab, spanning MRI reconstruction pipelines, acceleration frameworks, and motion simulation platforms.</p>
      </div>

      <div class="open-source-code-grid">
        <div class="glass-box p-4 h-100 d-flex flex-column open-source-repo-card" style="border-radius: 24px;">
          <div class="repo-title-row">
            <i class="fa-brands fa-github fa-2x" style="color: var(--global-text-color);"></i>
            <h3>eddysolo/demo_dce_recon</h3>
          </div>
          <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Demonstrates DCE MRI reconstruction with temporal TV regularization using the fastMRI Breast dataset.</p>
          <a href="https://github.com/eddysolo/demo_dce_recon" target="_blank" class="btn btn-outline-primary w-100 mt-auto" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
        </div>

        <div class="glass-box p-4 h-100 d-flex flex-column open-source-repo-card" style="border-radius: 24px;">
          <div class="repo-title-row">
            <i class="fa-brands fa-github fa-2x" style="color: var(--global-text-color);"></i>
            <h3>eddysolo/ELITE</h3>
          </div>
          <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">ELITE framework for accelerated DCE breast MRI reconstruction combining low-rank modeling and a ResNet-based enhancement stage.</p>
          <a href="https://github.com/eddysolo/ELITE" target="_blank" class="btn btn-outline-primary w-100 mt-auto" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
        </div>

        <div class="glass-box p-4 h-100 d-flex flex-column open-source-repo-card" style="border-radius: 24px;">
          <div class="repo-title-row">
            <i class="fa-brands fa-github fa-2x" style="color: var(--global-text-color);"></i>
            <h3>eddysolo/MR-Motion-Phantom-Platform</h3>
          </div>
          <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Open-source platform to simulate internal organ motion for MRI testing and algorithm validation.</p>
          <a href="https://github.com/eddysolo/MR-Motion-Phantom-Platform" target="_blank" class="btn btn-outline-primary w-100 mt-auto" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
        </div>
      </div>
    </div>

    <div class="tab-pane fade" id="source-popular-pane" role="tabpanel" aria-labelledby="source-popular-tab">
      <div class="glass-section open-source-tab-hero d-flex flex-column justify-content-center align-items-center text-center">
        <h2 style="font-weight: 800; font-size: 2rem; margin-bottom: 0.4rem;">Popular Science</h2>
        <p style="font-size: 1.08rem; margin: 0; max-width: 980px; line-height: 1.65;">Resources and outreach content that translate MRI research into accessible explanations for broader audiences.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px; color: inherit;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-database fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">
                <a href="{{ '/fastmri-dataset/' | relative_url }}" class="text-decoration-none" style="color: inherit;">FastMRI &amp; Breast DCE MRI Dataset</a>
              </h3>
            </div>
            <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Open-source MRI dataset support for reconstruction and machine learning research.</p>
            <p style="font-size: 1.1rem; flex-grow: 1;">We contributed Breast DCE MRI data to the NYU FastMRI ecosystem to support robust reconstruction benchmarks and reproducible algorithm development.</p>
            <img src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}" alt="fastMRI breast dataset preview" class="mt-3 w-100" style="border-radius: 16px; object-fit: cover;">
          </div>
        </div>
        <div class="col-lg-6"></div>
      </div>
    </div>

    <div class="tab-pane fade" id="source-patents-pane" role="tabpanel" aria-labelledby="source-patents-tab">
      <div class="glass-section open-source-tab-hero d-flex flex-column justify-content-center align-items-center text-center">
        <h2 style="font-weight: 800; font-size: 2rem; margin-bottom: 0.4rem;">Patents</h2>
        <p style="font-size: 1.08rem; margin: 0; max-width: 980px; line-height: 1.65;">A curated area for translational intellectual property and inventions evolving from open-source and methodological work.</p>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-file-contract fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-size: 1.08rem; color: var(--global-theme-color); font-weight: 800; margin: 0;">Method apparatus and system for determining a data signature of 3D image</h3>
            </div>
            <div class="d-flex flex-wrap mb-3" style="gap: 0.45rem;">
              <span class="badge badge-pill" style="background: rgba(0, 150, 199, 0.1); color: var(--global-text-color); font-weight: 700; padding: 0.45rem 0.75rem;">US20150366463A1</span>
              <span class="badge badge-pill" style="background: rgba(0, 150, 199, 0.15); color: var(--global-theme-color); font-weight: 700; padding: 0.45rem 0.75rem;">Publication: Dec 24, 2015</span>
              <span class="badge badge-pill" style="background: rgba(226, 80, 80, 0.14); color: #b33a3a; font-weight: 700; padding: 0.45rem 0.75rem;">Status: Expired</span>
            </div>
            <p style="font-size: 1rem; margin-bottom: 0.55rem;"><strong>Inventors:</strong> Eyal Naimi, Eddy Solomon, Israel Boaz Arnon</p>
            <p style="font-size: 1.02rem; line-height: 1.64; flex-grow: 1;"><strong>Abstract:</strong> A method for determining a thermal signature from thermal data of a body section by segmenting thermal values into groups and calculating contour-defining central locations for each segment. The resulting signature supports comparison against references for identifying thermally distinguishable regions.</p>
            <a href="https://patents.google.com/patent/US20150366463A1/en" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary mt-2 align-self-start" style="font-weight: 700; border-radius: 12px; padding: 0.68rem 1rem;">View In Google Patents</a>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-file-contract fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-size: 1.08rem; color: var(--global-theme-color); font-weight: 800; margin: 0;">Method apparatus and system for determining a thermal signature</h3>
            </div>
            <div class="d-flex flex-wrap mb-3" style="gap: 0.45rem;">
              <span class="badge badge-pill" style="background: rgba(0, 150, 199, 0.1); color: var(--global-text-color); font-weight: 700; padding: 0.45rem 0.75rem;">US9144397B2</span>
              <span class="badge badge-pill" style="background: rgba(0, 150, 199, 0.15); color: var(--global-theme-color); font-weight: 700; padding: 0.45rem 0.75rem;">Grant Date: Sep 29, 2015</span>
              <span class="badge badge-pill" style="background: rgba(46, 164, 79, 0.16); color: #1f6f37; font-weight: 700; padding: 0.45rem 0.75rem;">Status: Active</span>
            </div>
            <p style="font-size: 1rem; margin-bottom: 0.55rem;"><strong>Inventors:</strong> Eyal Naimi, Eddy Solomon, Israel Boaz Arnon</p>
            <p style="font-size: 1.02rem; line-height: 1.64; flex-grow: 1;"><strong>Abstract:</strong> A method for extracting a thermal signature from body-surface thermal data by segmenting image values and computing representative contour points. The signature enables analysis, detection, and longitudinal monitoring of thermally distinguished regions in clinical imaging contexts.</p>
            <a href="https://patents.google.com/patent/US9144397B2/en" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary mt-2 align-self-start" style="font-weight: 700; border-radius: 12px; padding: 0.68rem 1rem;">View In Google Patents</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
