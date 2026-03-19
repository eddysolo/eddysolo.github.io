---
layout: default
title: Open Science
permalink: /open-source/
description: Open-source software and code repositories from the Solomon's MRI Lab.
nav: true
nav_order: 5
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-5" style="border-radius: 24px; padding: 4rem 3rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.75rem;">Codes & Repositories</h1>
    <h3 style="font-weight: 600; font-size: 1.5rem; color: var(--global-theme-color); margin-bottom: 0;">Open-source software developed at Solomon's MRI Lab</h3>
  </div>

  <div class="row g-4 mb-4">
    <!-- Repo 1 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/demo_dce_recon</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Demonstrates DCE MRI reconstruction with temporal TV regularization using the fastMRI Breast dataset.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Includes shell and Python scripts (`loop_single_data.sh`, `dce_recon.py`, `dcm_recon.py`) for reconstructing undersampled radial k-space data and exporting DICOM outputs.</p>
        <a href="https://github.com/eddysolo/demo_dce_recon" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>

    <!-- Repo 2 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/ELITE</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">ELITE framework for accelerated DCE breast MRI reconstruction combining low-rank modeling and a ResNet-based enhancement stage.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: MATLAB reconstruction scripts and Python training/testing workflows are included to generate high spatial and temporal resolution image series from undersampled data.</p>
        <a href="https://github.com/eddysolo/ELITE" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>
  </div>

  <div class="row g-4">
    <!-- Repo 3 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/MR-Motion-Phantom-Platform</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Open-source platform to simulate internal organ motion for MRI testing and algorithm validation.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Includes design files and implementation code to prototype motion phantom experiments for controlled evaluation of motion-correction methods.</p>
        <a href="https://github.com/eddysolo/MR-Motion-Phantom-Platform" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>

    <!-- Repo 4 (Intentionally blank) -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">Repository Slot 4</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">To be announced.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: This slot is intentionally left blank for an upcoming open-source release.</p>
        <a href="#" class="btn btn-outline-primary w-100 disabled" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">Coming Soon</a>
      </div>
    </div>
  </div>

  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mt-5 mb-4" style="border-radius: 24px; padding: 3rem 2.5rem;">
    <h2 style="font-weight: 800; font-size: 2.4rem; margin-bottom: 0.65rem;">Open Source</h2>
    <h3 style="font-weight: 600; font-size: 1.3rem; color: var(--global-theme-color); margin-bottom: 0;">Our open source contributions and resources</h3>
  </div>

  <div class="row g-4">
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px; color: inherit;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-solid fa-database fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">
            <a href="{{ '/fastmri-dataset/' | relative_url }}" class="text-decoration-none" style="color: inherit;">FastMRI & Breast DCE MRI Dataset</a>
          </h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Open-source MRI dataset support for reconstruction and machine learning research.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">We contributed Breast DCE MRI data to the NYU FastMRI ecosystem to support robust reconstruction benchmarks and reproducible algorithm development.</p>
        <img
          src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}"
          alt="fastMRI breast dataset preview"
          class="mt-3 w-100"
          style="border-radius: 16px; object-fit: cover;"
        >
      </div>
    </div>

    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-solid fa-flask fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">Future Open Science Slot</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">To be announced.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Reserve this box for your next dataset release, benchmark suite, or public challenge contribution.</p>
        <span class="btn btn-outline-primary disabled mt-2" aria-disabled="true">Coming Soon</span>
      </div>
    </div>
  </div>
</div>
