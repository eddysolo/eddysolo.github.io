---
layout: default
title: Codes
permalink: /codes/
description: Open-source software and code repositories from the AI2MR Lab.
nav: true
nav_order: 4
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 95%; width: calc(100% - 2rem);">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-5" style="border-radius: 24px; padding: 4rem 3rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.75rem;">Codes & Repositories</h1>
    <h3 style="font-weight: 600; font-size: 1.5rem; color: var(--global-theme-color); margin-bottom: 0;">Open-source software developed at AI2MR Lab</h3>
  </div>

  <div class="row g-4 mb-4">
    <!-- Example Repo 1 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/motion-correction-net</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: Retrospectively corrects free-breathing cardiac MRI motion using unsupervised adversarial networks.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Designed to plug-and-play with raw k-space datasets containing random translational shifts. Can be invoked via `python correct.py --input scan.h5 --epochs 50` to output perfectly reconstructed images.</p>
        <a href="https://github.com/eddysolo/motion-correction-net" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>

    <!-- Example Repo 2 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/uwb-radar-gating</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: Python API for real-time serial parsing and phase-unwrapping of generic ultra-wideband radar streams.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Intended for real-time deployment alongside an MRI acquisition computer. Run `--listen COM3` to intercept, clean, and forward human respiratory waveforms back to the imaging console.</p>
        <a href="https://github.com/eddysolo/uwb-radar-gating" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>
  </div>

  <div class="row g-4">
    <!-- Example Repo 3 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/pydicom-mri-tools</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: Fast batch converter for organizing deeply nested DICOM archives into standardized NIfTI files.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Simply point the command line tool at your hospital export directory: `python dicom_tool.py --src /mnt/data/hospital --dst /mnt/data/nifti --anonymize`</p>
        <a href="https://github.com/eddysolo/pydicom-mri-tools" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>

    <!-- Example Repo 4 -->
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
        <div class="d-flex align-items-center mb-3">
          <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
          <h3 style="font-weight: 800; margin: 0;">eddysolo/fast-mri-reconstruction</h3>
        </div>
        <p style="font-size: 1.15rem; color: var(--global-theme-color); font-weight: 700;">Contribution: PyTorch implementation of cascaded unrolled neural networks for accelerated parallel imaging.</p>
        <p style="font-size: 1.1rem; flex-grow: 1;">Usage: Integrates perfectly with the ISMRM raw data format. Use `python train.py --config config.yaml` to begin distributed multi-GPU training on a generic cluster.</p>
        <a href="https://github.com/eddysolo/fast-mri-reconstruction" target="_blank" class="btn btn-outline-primary w-100" style="font-weight: 600; border-radius: 12px; padding: 0.75rem;">View on GitHub</a>
      </div>
    </div>
  </div>
</div>
