---
layout: default
title: Home
main_title: "Solomon MRI Lab - Advanced Imaging to Magnetic Resonance"
permalink: /
hero_image: assets/img/mri_hero.jpg
fluid: true
---

<style>
@keyframes scanline {
  0% { top: -100px; }
  100% { top: 100%; }
}

@keyframes pulse-ring {
  0% { transform: scale(0.8); box-shadow: 0 0 0 0 rgba(0, 150, 199, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 20px rgba(0, 150, 199, 0); }
  100% { transform: scale(0.8); box-shadow: 0 0 0 0 rgba(0, 150, 199, 0); }
}
</style>

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%; overflow-x: hidden;">
  <div class="post mx-auto" style="border: none; background: transparent; padding: 0; width: 100%; max-width: 100%;">
    
    <!-- Row 1: Welcome Box -->
    <div class="row g-4 mb-4">
      <div class="col-12">
        
        <!-- Welcome Box -->
        <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center" style="border-radius: 24px; padding: 4rem 3rem;">
          <h1 style="font-weight: 800; font-size: 3.5rem; letter-spacing: -0.02em; margin-bottom: 0.75rem;">Welcome to Solomon MRI Lab</h1>
          <h3 style="font-weight: 600; font-size: 1.75rem; color: var(--global-theme-color); margin-bottom: 0;">Advanced Imaging to Magnetic Resonance</h3>
        </div>
      </div>
    </div>

    <!-- Row 2: About Box -->
    <div class="row g-4 mb-4">
      <div class="col-12">
        <!-- About Box -->
        <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center" style="border-radius: 24px; padding: 3rem;">
          <p style="font-size: 1.35rem; margin: 0 auto; color: var(--global-text-color); line-height: 1.8; max-width: 1200px;">
            We bridge the gap between abstract algorithmic innovations and urgent clinical reality. By synergizing deep learning, physics, and advanced engineering, we enhance the speed, clarity, and accessibility of Magnetic Resonance Imaging for high-stakes, real-world diagnostic challenges.
          </p>
        </div>
      </div>
    </div>

    <!-- Row 3: Core Mission + News -->
    <div class="row g-4 mb-4 align-items-stretch">
      <div class="col-lg-6 d-flex">
        <div class="glass-box p-4 w-100 d-flex flex-column justify-content-center text-center align-items-center" style="border-radius: 24px;">
          <h2 style="font-weight: 800; margin-bottom: 1.25rem;"><i class="fa-solid fa-microscope mr-2" style="color: var(--global-theme-color);"></i> Our Core Mission</h2>
          <p style="font-size: 1.25rem; margin-bottom: 2rem; max-width: 900px; line-height: 1.6;">
            We aim to make MRI <strong>faster, more accurate, and more accessible</strong> to vulnerable populations like children and the elderly.
          </p>
          
          <div class="d-flex flex-column gap-3 w-100" style="max-width: 100%;">
            <a href="{{ '/computational-mri/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Computational MRI</h4>
              <p style="margin: 0; font-size: 1rem;">Revolutionary acquisition strategies and deep-learning image reconstruction.</p>
            </a>
            
            <a href="{{ '/motion-correction/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Motion Correction</h4>
              <p style="margin: 0; font-size: 1rem;">Free-breathing MRI techniques that eliminate motion artifacts.</p>
            </a>

            <a href="{{ '/advanced-hardware/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Advanced Hardware</h4>
              <p style="margin: 0; font-size: 1rem;">Integration of MR-compatible external sensors like ultra-wideband radar.</p>
            </a>
          </div>
        </div>
      </div>

      <!-- Announcements Box -->
      <div class="col-lg-6">
        <div class="glass-section h-100 text-center" style="padding: 2.5rem; border-radius: 24px;">
          <h2 class="glass-section-title" style="margin-bottom: 2rem; font-weight: 800; font-size: 2.5rem;">
            <a href="{{ '/news/' | relative_url }}" style="color: inherit; text-decoration: none;">📣 Latest Announcements</a>
          </h2>
          
          <div class="d-flex flex-column gap-3 text-left">
            <div class="glass-box p-4" style="border-radius: 16px; border-left: 6px solid var(--global-theme-color);">
              <div class="mb-2">
                <span style="font-size: 1.1rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.5rem;">Mar 3, 2026</span>
                <h3 style="margin: 0; font-weight: 800; font-size: 1.8rem; line-height: 1.3;">Paper Accepted to MICCAI 2026</h3>
              </div>
              <p style="margin: 0; font-size: 1.25rem; margin-top: 1rem;">Our latest work on free-breathing MRI techniques has been accepted for presentation at MICCAI in Kyoto, Japan.</p>
            </div>
            
            <div class="glass-box p-4 mt-3" style="border-radius: 16px; border-left: 6px solid var(--global-theme-color);">
              <div class="mb-2">
                <span style="font-size: 1.1rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.5rem;">Feb 15, 2026</span>
                <h3 style="margin: 0; font-weight: 800; font-size: 1.8rem; line-height: 1.3;">Pediatric MRI Grant Secured</h3>
              </div>
              <p style="margin: 0; font-size: 1.25rem; margin-top: 1rem;">We are thrilled to announce a new grant to accelerate our research on making MRI faster and more accessible for pediatric patients.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Join Us (Call to Action) with Background Image -->
    <section class="mb-4 position-relative" style="border-radius: 24px; padding: 4rem 3rem; text-align: center; color: white; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15); background-image: url('{{ "assets/img/ChatGPT_brain_scan_idea.png" | relative_url }}'); background-size: cover; background-position: center; background-repeat: no-repeat;">
      <!-- Animated MRI Scanline grid overlay -->
      <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: repeating-linear-gradient(0deg, transparent, transparent 19px, rgba(255,255,255,0.05) 20px), repeating-linear-gradient(90deg, transparent, transparent 19px, rgba(255,255,255,0.05) 20px); background-size: 20px 20px;"></div>
      
      <!-- Gradient Overlay for Contrast -->
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(135deg, rgba(8, 20, 48, 0.85) 0%, rgba(0, 93, 143, 0.75) 100%); mix-blend-mode: multiply;"></div>
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: rgba(0,0,0,0.2);"></div>
      
      <!-- Content -->
      <div style="position: relative; z-index: 2;">
        <h2 style="font-weight: 800; font-size: 2.5rem; color: white; margin-bottom: 1.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Intreseted to join us?</h2>
        <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 2.5rem; color: #f0f8ff; text-shadow: 0 1px 5px rgba(0,0,0,0.5);">
          We are always looking for motivated students and postdocs to join our team. If you are passionate about medical imaging and AI, we'd love to hear from you.
        </p>
        <a href="{{ '/contact/' | relative_url }}" class="btn btn-light btn-lg" style="color: #111424; font-weight: 700; padding: 1rem 3rem; text-transform: uppercase; letter-spacing: 0.05em; border-radius: 12px; font-size: 1.1rem; box-shadow: 0 10px 25px rgba(255,255,255,0.2);">Join Us Today</a>
      </div>
    </section>

    <!-- Collaborations Block -->
    <section class="glass-section mb-0" style="padding: 3rem 2.5rem; border-radius: 24px; text-align: center;">
      <h2 style="font-weight: 700; margin-bottom: 2rem; font-size: 2.2rem;">Our Collaborators</h2>
      
      <div class="row justify-content-center align-items-center">
        <!-- Technion -->
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img src="{{ 'assets/img/logos/technion_logo_transparent.png' | relative_url }}" alt="Technion Logo" style="max-height: 72px; object-fit: contain; margin-bottom: 1rem; width: 100%;">
            <h5 style="margin: 0; font-weight: 600;">Technion</h5>
          </div>
        </div>
        <!-- Cornell -->
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Cornell_University_seal.svg/1200px-Cornell_University_seal.svg.png" alt="Cornell Logo" style="max-height: 60px; object-fit: contain; margin-bottom: 1rem; width: 100%;">
            <h5 style="margin: 0; font-weight: 600;">Cornell University</h5>
          </div>
        </div>
        <!-- NYU Radiology -->
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img src="{{ 'assets/img/logos/nyu_radiology.png' | relative_url }}" alt="NYU Radiology Logo" style="max-height: 60px; object-fit: contain; margin-bottom: 1rem; width: 100%;">
            <h5 style="margin: 0; font-weight: 600;">NYU Radiology</h5>
          </div>
        </div>
        <!-- More Collaborators Placeholder -->
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <i class="fa-solid fa-plus fa-3x mb-3" style="color: var(--global-theme-color); opacity: 0.5;"></i>
            <h5 style="margin: 0; font-weight: 600; opacity: 0.7;">More to come</h5>
          </div>
        </div>
      </div>
    </section>

    <section style="padding: 2rem 1rem 0; text-align: center;">
      <div class="d-flex justify-content-center align-items-center flex-wrap" style="gap: 0.9rem;">
        <a href="https://www.linkedin.com/in/eddy-solomon-93159119b/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" style="color: #000; font-size: 3.45rem; line-height: 1;">
          <i class="fa-brands fa-linkedin"></i>
        </a>
        <a href="https://github.com/eddysolo" target="_blank" rel="noopener noreferrer" aria-label="GitHub" style="color: #000; font-size: 3.45rem; line-height: 1;">
          <i class="fa-brands fa-github"></i>
        </a>
        <a href="https://outlook.office.com/mail/deeplink/compose?to=eddy.solomon@bm.technion.ac.il" target="_blank" rel="noopener noreferrer" aria-label="Outlook" style="color: #000; font-size: 3.45rem; line-height: 1;">
          <i class="fa-solid fa-envelope"></i>
        </a>
        <a href="https://scholar.google.com/citations?user=tAOr0VwAAAAJ&hl=iw&oi=ao" target="_blank" rel="noopener noreferrer" aria-label="Google Scholar" style="color: #000; font-size: 3.45rem; line-height: 1;">
          <i class="ai ai-google-scholar"></i>
        </a>
      </div>
      <p style="margin-top: 0.8rem; margin-bottom: 0; font-size: 1rem; color: #000;">you can reach out us best by email.</p>
    </section>

  </div>
</div>
