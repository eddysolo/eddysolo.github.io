---
layout: default
title: fastMRI Breast DCE Dataset
permalink: /fastmri-dataset/
description: Open science resource page for the fastMRI Breast DCE MRI dataset contribution.
fluid: true
no_hero: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="row g-4 mb-4 align-items-stretch">
    <div class="col-lg-4">
      <div class="glass-box p-4 h-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(0,0,0,0.05);">
        <img
          src="{{ '/assets/img/publication_preview/FastMRI Breast A Publicly Available Radial k-Space Dataset of Breast Dynamic Contrast-enhanced MRI.png' | relative_url }}"
          alt="fastMRI Breast DCE dataset visual"
          style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"
        >
      </div>
    </div>

    <div class="col-lg-8">
      <div class="glass-box p-4 p-md-5 h-100 d-flex flex-column justify-content-center" style="border-radius: 24px; font-size: 1.2rem; line-height: 1.6;">
        <h2 style="font-weight: 800; margin-bottom: 1.5rem; display: flex; align-items: center;">
          <i class="fa-solid fa-database fa-lg mr-3" style="color: var(--global-theme-color);"></i>
          fastMRI Breast DCE Dataset
        </h2>
        <p>
          The <strong>fastMRI Breast DCE dataset</strong> is part of our open science effort to accelerate reproducible MRI research. It expands the fastMRI ecosystem with clinically meaningful breast dynamic contrast-enhanced (DCE) acquisitions that can be used for reconstruction, denoising, and downstream machine learning tasks.
        </p>
        <p class="mb-0">
          By releasing curated k-space and image data with clear documentation, we help researchers benchmark methods under realistic conditions and compare algorithms with transparent, community-driven standards.
        </p>
      </div>
    </div>
  </div>

  <div class="glass-section mb-4" style="border-radius: 24px; padding: 3rem;">
    <h3 style="font-weight: 800; font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center;">
      <i class="fa-solid fa-circle-check fa-md mr-3" style="color: var(--global-theme-color);"></i>
      Why This Resource Matters
    </h3>

    <div class="row g-4">
      <div class="col-md-4">
        <div class="glass-box p-4 h-100" style="border-radius: 16px;">
          <h5 style="font-weight: 800; margin-bottom: 0.75rem;">Reproducible Benchmarks</h5>
          <p class="mb-0" style="font-size: 1.05rem;">Common data enables apples-to-apples comparison across compressed sensing and deep learning pipelines.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="glass-box p-4 h-100" style="border-radius: 16px;">
          <h5 style="font-weight: 800; margin-bottom: 0.75rem;">Clinically Relevant Contrast</h5>
          <p class="mb-0" style="font-size: 1.05rem;">Breast DCE MRI captures dynamic enhancement patterns that challenge reconstruction models in realistic scenarios.</p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="glass-box p-4 h-100" style="border-radius: 16px;">
          <h5 style="font-weight: 800; margin-bottom: 0.75rem;">Open Science Impact</h5>
          <p class="mb-0" style="font-size: 1.05rem;">Public access lowers barriers, speeds collaboration, and supports robust validation across institutions.</p>
        </div>
      </div>
    </div>
  </div>

  <div class="row g-4 mb-5 align-items-stretch">
    <div class="col-lg-6">
      <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 20px;">
        <h4 style="font-weight: 800; margin-bottom: 1rem; display: flex; align-items: center;">
          <i class="fa-solid fa-link mr-2" style="color: var(--global-theme-color);"></i>
          Useful Links
        </h4>
        <p style="font-size: 1.05rem; margin-bottom: 1.25rem;">Explore the official website, the code repository, and the related article below.</p>

        <a href="https://fastmri.med.nyu.edu/" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px;">
          <i class="fa-solid fa-arrow-up-right-from-square mr-2"></i>
          Official fastMRI Website
        </a>

        <a href="https://github.com/facebookresearch/fastMRI" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
          <i class="fa-brands fa-github mr-2"></i>
          fastMRI GitHub Repository
        </a>

        <a href="https://doi.org/10.48550/arXiv.2406.05270" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-lg text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
          <i class="fa-solid fa-book-open mr-2"></i>
          fastMRI Breast Article
        </a>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="glass-box p-4 h-100" style="border-radius: 20px;">
        <h4 style="font-weight: 800; margin-bottom: 1rem; display: flex; align-items: center;">
          <i class="fa-solid fa-image mr-2" style="color: var(--global-theme-color);"></i>
          Example Breast MRI Slice
        </h4>
        <img
          src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}"
          alt="Breast MRI scan example"
          class="w-100"
          style="border-radius: 14px; object-fit: cover;"
        >
      </div>
    </div>
  </div>
</div>
