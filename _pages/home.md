---
layout: default
title: Home
main_title: "AI2MR Lab - Advanced Imaging 2 Magnetic Resonance"
permalink: /
hero_image: assets/img/mri_hero_new.png
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 95%; width: calc(100% - 2rem); overflow-x: hidden;">
  <div class="post mx-auto" style="border: none; background: transparent; padding: 0; width: 100%; max-width: 100%;">
    
    <!-- Row 1: Welcome Box -->
    <div class="row g-4 mb-4">
      <div class="col-12">
        
        <!-- Welcome Box -->
        <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center" style="border-radius: 24px; padding: 4rem 3rem;">
          <h1 style="font-weight: 800; font-size: 3.5rem; letter-spacing: -0.02em; margin-bottom: 0.75rem;">Welcome to AI2MR Lab</h1>
          <h3 style="font-weight: 600; font-size: 1.75rem; color: var(--global-theme-color); margin-bottom: 0;">Advanced Imaging 2 Magnetic Resonance</h3>
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

    <!-- Row 3: Mission & Images -->
    <div class="row g-4 mb-4 align-items-stretch">
      <!-- Core Mission (Wide) -->
      <div class="col-lg-6 d-flex">
        <div class="glass-box p-4 w-100 d-flex flex-column justify-content-center text-center align-items-center" style="border-radius: 24px;">
          <h2 style="font-weight: 800; margin-bottom: 1.25rem;"><i class="fa-solid fa-microscope mr-2" style="color: var(--global-theme-color);"></i> Our Core Mission</h2>
          <p style="font-size: 1.25rem; margin-bottom: 2rem; max-width: 600px; line-height: 1.6;">
            We aim to make MRI <strong>faster, more accurate, and more accessible</strong> to vulnerable populations like children and the elderly.
          </p>
          
          <div class="d-flex flex-column gap-3 w-100" style="max-width: 600px;">
            <a href="{{ '/computational-mri/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Computational MRI</h4>
              <p style="margin: 0; font-size: 1rem;">Revolutionary acquisition strategies and deep-learning image reconstruction.</p>
            </a>
            
            <a href="{{ '/motion-correction/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Motion Correction</h4>
              <p style="margin: 0; font-size: 1rem;">Free-breathing MRI techniques that eliminate motion artifacts.</p>
            </a>

            <a href="{{ '/smart-sensors/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Smart Sensors</h4>
              <p style="margin: 0; font-size: 1rem;">Integration of MR-compatible external sensors like ultra-wideband radar.</p>
            </a>
          </div>
        </div>
      </div>

      <!-- Vertical Image Stack -->
      <div class="col-lg-6 d-flex flex-column gap-4">
        
        <!-- Brain Image Box -->
        <div class="glass-box p-0 w-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(255,255,255,0.4); overflow: hidden;">
          <img src="{{ 'assets/img/brain-image.png' | relative_url }}" alt="Brain Scan" style="width: 100%; height: auto; display: block; object-fit: contain;">
        </div>
        
        <!-- Abdominal Image Box -->
        <div class="glass-box p-0 w-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(255,255,255,0.4); overflow: hidden;">
          <img src="{{ 'assets/img/mri-abdominal.png' | relative_url }}" alt="Abdominal MRI" style="width: 100%; height: auto; display: block; object-fit: contain;">
        </div>
        
      </div>
    </div>

    <!-- Bento Box Grid (Row 3: News & Selected Pubs) -->
    <div class="row g-4 mb-4 align-items-stretch">
      <!-- Announcements Box -->
      <div class="col-lg-6">
        <div class="glass-section h-100" style="padding: 2.5rem; border-radius: 24px;">
          <h2 class="glass-section-title" style="margin-bottom: 2rem; font-weight: 800;">
            <a href="{{ '/news/' | relative_url }}" style="color: inherit">📣 Latest Announcements</a>
          </h2>
          
          <div class="d-flex flex-column gap-3">
            <div class="glass-box p-4" style="border-radius: 16px; border-left: 4px solid var(--global-theme-color);">
              <div class="mb-2">
                <span style="font-size: 0.95rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.5rem;">Mar 3, 2026</span>
                <h3 style="margin: 0; font-weight: 800; font-size: 1.6rem; line-height: 1.3;">Paper Accepted to MICCAI 2026</h3>
              </div>
              <p style="margin: 0; font-size: 1.1rem; margin-top: 1rem;">Our latest work on free-breathing MRI techniques has been accepted for presentation at MICCAI in Kyoto, Japan.</p>
            </div>
            
            <div class="glass-box p-4 mt-3" style="border-radius: 16px; border-left: 4px solid var(--global-theme-color);">
              <div class="mb-2">
                <span style="font-size: 0.95rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.5rem;">Feb 15, 2026</span>
                <h3 style="margin: 0; font-weight: 800; font-size: 1.6rem; line-height: 1.3;">Pediatric MRI Grant Secured</h3>
              </div>
              <p style="margin: 0; font-size: 1.1rem; margin-top: 1rem;">We are thrilled to announce a new grant to accelerate our research on making MRI faster and more accessible for pediatric patients.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Selected Publications Box -->
      <div class="col-lg-6">
        <div class="glass-section h-100 text-center" style="padding: 2.5rem; border-radius: 24px;">
          <h2 class="glass-section-title" style="margin-bottom: 2rem; font-weight: 800;">
            <a href="{{ '/publications/' | relative_url }}" style="color: inherit">Selected Publications</a>
          </h2>
          
          <div class="d-flex flex-column gap-3">
            <!-- Publication Card 1 -->
            <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 text-decoration-none d-flex align-items-center" style="border-radius: 16px; color: var(--global-text-color); transition: all 0.3s ease;">
              <div style="background: rgba(0, 150, 199, 0.1); width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 1.5rem; flex-shrink: 0;">
                <i class="fa-solid fa-file-pdf fa-2x" style="color: var(--global-theme-color);"></i>
              </div>
              <div>
                <h3 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.5rem; line-height: 1.3;">Navigator-free motion-resolved 3D MRI using deep generative models</h3>
                <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Nature Communications (2025)</p>
              </div>
            </a>

            <!-- Publication Card 2 -->
            <a href="{{ '/publications/' | relative_url }}" class="glass-box p-4 mt-3 text-decoration-none d-flex align-items-center" style="border-radius: 16px; color: var(--global-text-color); transition: all 0.3s ease;">
              <div style="background: rgba(0, 150, 199, 0.1); width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 1.5rem; flex-shrink: 0;">
                <i class="fa-solid fa-file-pdf fa-2x" style="color: var(--global-theme-color);"></i>
              </div>
              <div>
                <h3 style="margin: 0 0 0.5rem 0; font-weight: 800; font-size: 1.5rem; line-height: 1.3;">Highly-accelerated parallel MRI using deep learning prior</h3>
                <p style="margin: 0; font-size: 1rem; opacity: 0.8; font-family: monospace;">Magnetic Resonance in Medicine (2025)</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Join Us (Call to Action) with Background Image -->
    <section class="mb-4 position-relative" style="border-radius: 24px; padding: 4rem 3rem; text-align: center; color: white; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15);">
      <!-- Background Image -->
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; background-image: url('{{ "assets/img/ChatGPT_brain_scan_idea.png" | relative_url }}'); background-size: cover; background-position: center; filter: brightness(0.9);"></div>
      
      <!-- Gradient Overlay for Contrast -->
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(135deg, rgba(8, 20, 48, 0.85) 0%, rgba(0, 93, 143, 0.75) 100%); mix-blend-mode: multiply;"></div>
      <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: rgba(0,0,0,0.2);"></div>
      
      <!-- Content -->
      <div style="position: relative; z-index: 2;">
        <h2 style="font-weight: 800; font-size: 2.5rem; color: white; margin-bottom: 1.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Looking for Opportunities?</h2>
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
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <i class="fa-solid fa-hospital fa-3x mb-3" style="color: var(--global-theme-color);"></i>
            <h5 style="margin: 0; font-weight: 600;">Medical Centers</h5>
          </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <i class="fa-solid fa-university fa-3x mb-3" style="color: var(--global-theme-color);"></i>
            <h5 style="margin: 0; font-weight: 600;">Universities</h5>
          </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <i class="fa-solid fa-industry fa-3x mb-3" style="color: var(--global-theme-color);"></i>
            <h5 style="margin: 0; font-weight: 600;">Industry Partners</h5>
          </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
          <div class="glass-box p-4 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <i class="fa-solid fa-microscope fa-3x mb-3" style="color: var(--global-theme-color);"></i>
            <h5 style="margin: 0; font-weight: 600;">Research Institutes</h5>
          </div>
        </div>
      </div>
    </section>

  </div>
</div>
