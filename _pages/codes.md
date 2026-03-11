---
layout: default
title: Codes
permalink: /codes/
description: Open-source software and code repositories from the Solomon's MRI Lab.
nav: true
nav_order: 4
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 95%; width: calc(100% - 2rem);">
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
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: Demonstrates DCE MRI reconstruction with temporal TV regularization using the fastMRI Breast dataset.</p>
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
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: ELITE framework for accelerated DCE breast MRI reconstruction combining low-rank modeling and a ResNet-based enhancement stage.</p>
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
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: Open-source platform to simulate internal organ motion for MRI testing and algorithm validation.</p>
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
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: To be announced.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: This slot is intentionally left blank for an upcoming open-source release.</p>
        <a href="#" class="btn btn-outline-primary w-100 disabled" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">Coming Soon</a>
      </div>
    </div>
  </div>
</div>
