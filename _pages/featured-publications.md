---
layout: default
title: Featured Publications
permalink: /featured-publications/
description: A showcase of our best work and research highlights.
nav: false
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 95%; width: calc(100% - 2rem);">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-5" style="border-radius: 24px; padding: 4rem 3rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.75rem;">Featured Publications</h1>
    <h3 style="font-weight: 600; font-size: 1.5rem; color: var(--global-theme-color); margin-bottom: 0;">Our most impactful research highlights</h3>
  </div>

  <div class="row g-4 justify-content-center">
    <!-- Featured Pub 1 -->
    <div class="col-lg-10">
      <a href="https://github.com/eddysolo/motion-correction-net" target="_blank" class="glass-box p-4 p-md-5 d-flex flex-column flex-md-row gap-4 align-items-center text-decoration-none" style="border-radius: 24px; transition: transform 0.3s ease; color: inherit; display: block;">
        <div style="background: rgba(0, 150, 199, 0.1); width: 100px; height: 100px; border-radius: 20px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; overflow: hidden;">
          <!-- Optional Image Support: Replace the i tag with an img tag if an image is provided -->
          <i class="fa-solid fa-file-pdf fa-3x" style="color: var(--global-theme-color);"></i>
        </div>
        <div class="text-left">
          <h3 style="font-weight: 800; margin-bottom: 0.5rem; line-height: 1.3; color: var(--global-text-color);">Navigator-free motion-resolved 3D MRI using deep generative models</h3>
          <p class="text-muted" style="font-family: monospace; font-size: 1.1rem; margin-bottom: 1rem;">Nature Communications (2025)</p>
          <p style="font-size: 1.15rem; line-height: 1.6; max-width: 800px; margin-bottom: 0; color: var(--global-text-color);">We propose a totally new approach to managing uncooperative physiological motion during prolonged 3D MRI scans by combining real-time feature extraction with advanced generative networks capable of completing massive datasets securely.</p>
        </div>
      </a>
    </div>

    <!-- Featured Pub 2 -->
    <div class="col-lg-10">
      <a href="https://github.com/eddysolo/uwb-radar-gating" target="_blank" class="glass-box p-4 p-md-5 d-flex flex-column flex-md-row gap-4 align-items-center text-decoration-none" style="border-radius: 24px; transition: transform 0.3s ease; color: inherit; display: block;">
        <div style="background: rgba(0, 150, 199, 0.1); width: 100px; height: 100px; border-radius: 20px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; overflow: hidden;">
          <!-- Optional Image Example -->
          <img src="{{ 'assets/img/brain-image.png' | relative_url }}" alt="Publication Image" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div class="text-left">
          <h3 style="font-weight: 800; margin-bottom: 0.5rem; line-height: 1.3; color: var(--global-text-color);">Integration of ultra-wideband radar for MR respiratory gating</h3>
          <p class="text-muted" style="font-family: monospace; font-size: 1.1rem; margin-bottom: 1rem;">IEEE Transactions on Medical Imaging (2023)</p>
          <p style="font-size: 1.15rem; line-height: 1.6; max-width: 800px; margin-bottom: 0; color: var(--global-text-color);">By introducing non-contact external RF radar sensors that track minute cardiopulmonary surface displacements, we decoupled gating metrics from the scan acquisition entirely—delivering uninterrupted high-resolution imaging blocks unimpacted by traditional delays.</p>
        </div>
      </a>
    </div>
  </div>
</div>
