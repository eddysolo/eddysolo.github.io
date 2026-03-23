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

.home-fixed-gap {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.home-fixed-gap > * {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.home-fixed-gap > .row {
  margin-left: 0 !important;
  margin-right: 0 !important;
}

.home-fixed-gap > .row > [class*="col-"] {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

.home-fixed-gap > .row.gx-2 {
  margin-left: -0.35rem !important;
  margin-right: -0.35rem !important;
}

.home-fixed-gap > .row.gx-2 > [class*="col-"] {
  padding-left: 0.35rem !important;
  padding-right: 0.35rem !important;
}
</style>

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%; overflow-x: hidden;">
  <div class="post mx-auto home-fixed-gap" style="border: none; background: transparent; padding: 0; width: 100%; max-width: 100%;">
    
    <!-- Row 1: Welcome Box -->
    <div class="row g-0">
      <div class="col-12">
        
        <!-- Welcome Box -->
        <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center" style="border-radius: 24px; padding: 4rem 3rem;">
          <h1 style="font-weight: 800; font-size: 3.5rem; letter-spacing: -0.02em; margin-bottom: 0.75rem;">Welcome to Solomon MRI Lab</h1>
          <h3 style="font-weight: 600; font-size: 1.75rem; color: var(--global-theme-color); margin-bottom: 0;">Faster, Smarter, and More Accessible MRI</h3>
        </div>
      </div>
    </div>

    <!-- Row 2: About Box -->
    <div class="row g-0">
      <div class="col-12">
        <!-- About Box -->
        <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center" style="border-radius: 24px; padding: 2.1rem 3rem;">
          <p style="font-size: 1.35rem; margin: 0 auto; color: var(--global-text-color); line-height: 1.72; max-width: 1200px;">
            Our team combines expertise in physics, engineering, and deep learning to advance medical imaging, with a particular focus on Magnetic Resonance Imaging (MRI). We develop novel MRI technologies that translate cutting-edge algorithms into meaningful clinical impact, improving both the speed and quality of imaging. By making MRI faster, more reliable, and more accessible, we aim to enhance patient care across a wide range of applications, including brain, breast, and abdominal imaging.
          </p>
        </div>
      </div>
    </div>

    <!-- Row 3: Core Mission + News -->
    <div class="row gx-2 gy-0 align-items-stretch">
      <div class="col-lg-6 d-flex">
        <div class="glass-section h-100 w-100 d-flex flex-column text-center align-items-center" style="padding: 1.25rem; border-radius: 24px;">
          <h2 style="font-weight: 800; font-size: 1.85rem; line-height: 1.2; margin: 0 0 0.65rem 0; min-height: 3rem; display: flex; align-items: center; justify-content: center; gap: 0.45rem;"><i class="fa-solid fa-microscope" style="color: var(--global-theme-color);"></i><span>Our Research</span></h2>
          
          <div class="d-flex flex-column gap-1 w-100" style="max-width: 100%;">
            <a href="{{ '/computational-mri/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Computational MRI</h4>
              <p style="margin: 0; font-size: 1rem;">Novel acquisition strategies and deep learning reconstruction for faster, higher-quality MRI.</p>
            </a>
            
            <a href="{{ '/motion-correction/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Motion Correction</h4>
              <p style="margin: 0; font-size: 1rem;">Free-breathing MRI methods that reduce motion artifacts and improve robustness in clinical scans.</p>
            </a>

            <a href="{{ '/advanced-hardware/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Advanced Hardware</h4>
              <p style="margin: 0; font-size: 1rem;">Integration of MR-compatible external sensors, including ultra-wideband radar, for enhanced imaging.</p>
            </a>

            <a href="{{ '/non-cartesian-imaging/' | relative_url }}" class="glass-box p-3 text-decoration-none text-center" style="border-radius: 16px; transition: transform 0.2s; color: var(--global-text-color); border: 1px solid rgba(0,150,199,0.3);">
              <h4 style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; color: var(--global-theme-color);">Non-Cartesian Imaging</h4>
              <p style="margin: 0; font-size: 1rem;">Radial and spiral k-space trajectories for faster and more motion-robust MRI reconstruction.</p>
            </a>
          </div>
        </div>
      </div>

      <!-- Announcements Box -->
      <div class="col-lg-6 d-flex">
        <div class="glass-section h-100 w-100 text-center" style="padding: 1.25rem; border-radius: 24px;">
          <h2 style="font-weight: 800; font-size: 1.85rem; line-height: 1.2; margin: 0 0 0.65rem 0; min-height: 3rem; display: flex; align-items: center; justify-content: center; gap: 0.45rem;">
            <a href="{{ '/news/' | relative_url }}" style="color: inherit; text-decoration: none; display: inline-flex; align-items: center; gap: 0.45rem;">
              <i class="fa-solid fa-bullhorn" style="color: var(--global-theme-color);"></i>
              <span>Latest News</span>
            </a>
          </h2>
          
          <div class="d-flex flex-column gap-1 text-left">
            <div class="glass-box p-3" style="border-radius: 16px; border-left: 4px solid var(--global-theme-color);">
              <div class="mb-1">
                <span style="font-size: 0.95rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.35rem;">Mar 3, 2026</span>
                <h3 style="margin: 0; font-weight: 700; font-size: 1.2rem; line-height: 1.35;">Paper Accepted to MICCAI 2026</h3>
              </div>
              <p style="margin: 0; font-size: 1rem; margin-top: 0.35rem; line-height: 1.45;">Our latest work on free-breathing MRI techniques has been accepted for presentation at MICCAI in Kyoto, Japan.</p>
            </div>
            
            <div class="glass-box p-3" style="border-radius: 16px; border-left: 4px solid var(--global-theme-color);">
              <div class="mb-1">
                <span style="font-size: 0.95rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.35rem;">Feb 15, 2026</span>
                <h3 style="margin: 0; font-weight: 700; font-size: 1.2rem; line-height: 1.35;">Pediatric MRI Grant Secured</h3>
              </div>
              <p style="margin: 0; font-size: 1rem; margin-top: 0.35rem; line-height: 1.45;">We are thrilled to announce a new grant to accelerate our research on making MRI faster and more accessible for pediatric patients.</p>
            </div>

            <div class="glass-box p-3" style="border-radius: 16px; border-left: 4px solid var(--global-theme-color);">
              <div class="mb-1">
                <span style="font-size: 0.95rem; font-weight: 700; color: var(--global-theme-color); display: block; margin-bottom: 0.35rem;">Jan 28, 2026</span>
                <h3 style="margin: 0; font-weight: 700; font-size: 1.2rem; line-height: 1.35;">New MRI Workshop Announced</h3>
              </div>
              <p style="margin: 0; font-size: 1rem; margin-top: 0.35rem; line-height: 1.45;">Our lab will host a hands-on workshop focused on rapid MRI acquisition and reconstruction methods for graduate students and researchers.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Join Us (Call to Action) with Background Image -->
    <a href="{{ '/contact/' | relative_url }}" style="display: block; color: inherit; text-decoration: none;">
      <section class="position-relative" style="border-radius: 24px; padding: 4rem 3rem; text-align: center; color: white; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.15); background-image: url('{{ "assets/img/ChatGPT_brain_scan_idea.png" | relative_url }}'); background-size: cover; background-position: center; background-repeat: no-repeat; cursor: pointer;">
        <!-- Animated MRI Scanline grid overlay -->
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: repeating-linear-gradient(0deg, transparent, transparent 19px, rgba(255,255,255,0.05) 20px), repeating-linear-gradient(90deg, transparent, transparent 19px, rgba(255,255,255,0.05) 20px); background-size: 20px 20px;"></div>
        
        <!-- Gradient Overlay for Contrast -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: linear-gradient(135deg, rgba(8, 20, 48, 0.85) 0%, rgba(0, 93, 143, 0.75) 100%); mix-blend-mode: multiply;"></div>
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: rgba(0,0,0,0.2);"></div>
        
        <!-- Content -->
        <div style="position: relative; z-index: 2;">
          <h2 style="font-weight: 800; font-size: 2.5rem; color: white; margin-bottom: 1.5rem; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">Intreseted to join us?</h2>
          <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto; color: #f0f8ff; text-shadow: 0 1px 5px rgba(0,0,0,0.5);">
            We are always looking for motivated students and postdocs to join our team. If you are passionate about medical imaging and AI, we'd love to hear from you.
          </p>
        </div>
      </section>
    </a>

    <!-- Collaborations Block -->
    <section class="glass-section collaborators-section" style="padding: 3rem 2.5rem; border-radius: 24px; text-align: center;">
      <h2 style="font-weight: 700; margin-bottom: 2rem; font-size: 2.2rem;">Our Collaborators</h2>
      
      <div class="row gx-3 gy-4 justify-content-center align-items-stretch" style="row-gap: 0.6rem;">
        <!-- Weill Cornell Medicine -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/Weill_Cornell_Medicine.png' | relative_url }}" alt="Weill Cornell Medicine Logo" style="max-height: 102px; object-fit: contain; margin-bottom: 0; width: 100%;">
          </div>
        </div>
        <!-- NYU Radiology -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/nyu_radiology.png' | relative_url }}" alt="NYU Radiology Logo" style="max-height: 102px; object-fit: contain; margin-bottom: 0; width: 100%;">
          </div>
        </div>
        <!-- University of Chicago -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/Chicago_University.png' | relative_url }}" alt="University of Chicago Logo" style="max-height: 102px; object-fit: contain; margin-bottom: 0; width: 100%;">
          </div>
        </div>
        <!-- Memorial Sloan Kettering -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/Memorial_Sloan.png' | relative_url }}" alt="Memorial Sloan Kettering Logo" style="max-height: 88px; object-fit: contain; margin-bottom: 0; width: 100%;">
          </div>
        </div>
        <!-- NIST -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/NIST.png' | relative_url }}" alt="NIST Logo" style="max-height: 102px; object-fit: contain; margin-bottom: 0; width: 100%;">
          </div>
        </div>
        <!-- NeuroSpin -->
        <div class="col-6 col-md-4 d-flex">
          <div class="glass-box collaborators-logo-card p-4 w-100 h-100 d-flex flex-column justify-content-center" style="border-radius: 20px; background: rgba(255,255,255,0.05);">
            <img class="collaborators-logo-image" src="{{ 'assets/img/logos/NeuroSpin.png' | relative_url }}" alt="NeuroSpin Logo" style="max-height: 88px; object-fit: contain; margin-bottom: 0; width: 100%;">
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
