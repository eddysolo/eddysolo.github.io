---
layout: default
title: Motion Correction
permalink: /motion-correction/
fluid: true
no_hero: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="row g-4 mb-4 align-items-stretch">
    <!-- Main Concept -->
    <div class="col-lg-8">
      <div class="glass-box p-4 p-md-5 h-100 d-flex flex-column justify-content-center" style="border-radius: 24px; font-size: 1.25rem; line-height: 1.6;">
        <h2 style="font-weight: 800; margin-bottom: 1.5rem; display: flex; align-items: center;"><i class="fa-solid fa-person-running fa-lg mr-3" style="color: var(--global-theme-color);"></i> The Concept</h2>
        <p>
          One of the greatest challenges in medical imaging is patient motion. Breathing, heartbeat, and involuntary twitches can blur an MRI scan so severely that it becomes diagnostically useless. Traditionally, patients are asked to hold their breath for long durations, which is incredibly difficult for the elderly, young children, or critically ill patients.
        </p>
        <p class="mb-0">
          Our lab is developing <strong>Motion Correction</strong> algorithms that automatically resolve and compensate for physiological movements during the scan. By extracting motion signatures directly from the data (or utilizing external sensors), we can retrospectively "freeze" the motion, yielding crystal-clear imaging while allowing patients to breathe comfortably and freely.
        </p>
      </div>
    </div>
    
    <!-- Image Box -->
    <div class="col-lg-4">
      <div class="glass-box p-4 h-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(0,0,0,0.05);">
        <img src="{{ 'assets/img/mri-abdominal.png' | relative_url }}" alt="Abdominal MRI Motion Correction" style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
      </div>
    </div>
  </div>

  <div class="glass-section mb-4" style="border-radius: 24px; padding: 3rem;">
    <h3 style="font-weight: 800; font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center;"><i class="fa-solid fa-book-open fa-md mr-3" style="color: var(--global-theme-color);"></i> Relevant Articles</h3>
    <div class="row g-4 justify-content-center">
      
      <!-- Article 1 -->
      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-file-pdf fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">Navigator-free motion-resolved 3D MRI using deep generative models</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Nature Communications (2025)</p>
          </div>
        </a>
      </div>
      
      <!-- Article 2 -->
      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-file-pdf fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">Robust free-breathing cardiac MRI</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Journal of Cardiovascular Magnetic Resonance (2024)</p>
          </div>
        </a>
      </div>
      
      <!-- Article 3 -->
      <div class="col-md-4">
        <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex flex-column align-items-center text-center h-100" style="border-radius: 16px; color: var(--global-text-color); transition: transform 0.3s ease;">
          <div style="background: rgba(0, 150, 199, 0.1); width: 80px; height: 80px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem; flex-shrink: 0;">
            <i class="fa-solid fa-file-pdf fa-2x" style="color: var(--global-theme-color);"></i>
          </div>
          <div>
            <h5 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.25rem;">Unsupervised learning for motion correction</h5>
            <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">MICCAI Proceedings (2023)</p>
          </div>
        </a>
      </div>
      
    </div>
  </div>

  <!-- Contact Us / LinkedIn CTA block -->
  <div class="glass-section mb-5 text-center p-5" style="border-radius: 24px; background: rgba(0, 150, 199, 0.05); border: 1px solid rgba(0, 150, 199, 0.2);">
    <h2 style="font-weight: 800; font-size: 2.2rem; margin-bottom: 1rem;">Interested in Motion Correction?</h2>
    <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 2rem; color: var(--global-text-color);">
      We are actively looking for collaborators and students enthusiastic about solving uncooperative physiological motion challenges in diagnostic imaging.
    </p>
    <div class="d-flex justify-content-center gap-4 flex-wrap">
      <a href="{{ '/contact/' | relative_url }}" class="btn btn-primary btn-lg d-flex align-items-center" style="font-weight: 700; border-radius: 12px; padding: 0.75rem 2rem; box-shadow: 0 10px 20px rgba(0,150,199,0.3);">
        <i class="fa-solid fa-envelope fa-lg mr-2"></i> Contact Us
      </a>
      <a href="https://linkedin.com/company/solomons-mri-lab" target="_blank" class="btn btn-outline-primary btn-lg d-flex align-items-center" style="font-weight: 700; border-radius: 12px; padding: 0.75rem 2rem; border-width: 2px;">
        <i class="fa-brands fa-linkedin fa-lg mr-2"></i> Follow Updates
      </a>
    </div>
  </div>
</div>
