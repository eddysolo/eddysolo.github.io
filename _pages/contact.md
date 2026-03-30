---
layout: default
title: Contact Us
permalink: /contact/
description: Get in touch with the Solomon's MRI Lab.
nav: true
nav_order: 999
fluid: true
---

<style>
  /* Page Level Background setup */
  html body, html[data-theme="dark"] body {
    background-image: url('{{ "assets/img/technion_contact_bg_google.jpg" | relative_url }}') !important;
    background-color: transparent !important;
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
  }
  
  body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: linear-gradient(135deg, rgba(8, 20, 48, 0.68) 0%, rgba(0, 93, 143, 0.56) 100%);
    mix-blend-mode: multiply;
    z-index: -1;
  }
  
  body::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(129, 127, 127, 0.2);
    z-index: -1;
  }

  /* Bento Box Actual Grid Structure */
  .bento-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2vw;
    padding: 1.8vw;
    width: 100%;
    min-height: calc(100vh - 80px); /* Fill screen minus header */
    margin: 0 auto;
    z-index: 2;
    position: relative;
  }

  /* Desktop Grid */
  @media (min-width: 992px) {
    .bento-wrapper {
      grid-template-columns: repeat(5, 1fr);
      grid-template-rows: auto auto;
    }
    
    .bento-card-main {
      grid-column: 1 / 4;
      grid-row: 1 / 3;
    }
    
    .bento-card-logo {
      grid-column: 4 / 6;
      grid-row: 1 / 2;
    }
    
    .bento-card-map {
      grid-column: 4 / 6;
      grid-row: 2 / 3;
    }
  }

  .bento-card {
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    overflow: hidden;
    position: relative;
    transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s ease;
  }
  
  .bento-card:hover {
    transform: translateY(-8px) scale(1.01);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    z-index: 3;
  }

  .glass-dark {
    background: rgba(8, 20, 48, 0.65);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .glass-light {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.4);
  }
</style>

<div class="container-fluid px-0 mx-auto" style="overflow-x: hidden;">
  <div class="bento-wrapper">
    
    <!-- Block 1: Main Info -->
    <div class="bento-card bento-card-main glass-dark p-3 p-md-4 d-flex flex-column justify-content-start text-left" style="height: 100%;">
      <h2 class="mb-3" style="font-weight: 800; color: #ffffff; font-size: 3rem; letter-spacing: -0.02em;">Let's Connect</h2>
      <p class="mb-4" style="font-size: 1.2rem; line-height: 1.6; color: rgba(255,255,255,0.85);">
        We are always seeking ambitious, motivated, and passionate undergraduates, graduate students,and postdoctoral scholars to join our lab. We also welcome messages from researchers and clinicians interested in initiating collaborations.
      </p>

      <ul class="list-unstyled mb-0 mt-3">
        <!-- Email -->
        <li class="mb-4 d-flex align-items-center">
          <div style="background: rgba(144, 216, 255, 0.15); height: 68px; width: 68px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1.2rem; flex-shrink: 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <i class="fa-solid fa-envelope" style="color: #90d8ff; font-size: 2rem;"></i>
          </div>
          <div>
            <h5 class="mb-1" style="font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.15em;">Email Us</h5>
            <a href="mailto:eddy.solomon@technion.ac.il" style="font-size: 1.3rem; color: #ffffff; text-decoration: none; font-weight: 700;">eddy.solomon@technion.ac.il</a>
          </div>
        </li>
        <!-- Location -->
        <li class="d-flex align-items-center">
          <div style="background: rgba(144, 216, 255, 0.15); height: 68px; width: 68px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1.2rem; flex-shrink: 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <i class="fa-solid fa-location-dot" style="color: #90d8ff; font-size: 2rem;"></i>
          </div>
          <div>
            <h5 class="mb-1" style="font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.15em;">Visit Our Lab</h5>
            <span style="font-size: 1.15rem; line-height: 1.5; display: inline-block; color: #ffffff; font-weight: 500;">
              Faculty of Biomedical Engineering<br>
              Julius Silver Building<br>
              Room 328, Floor 3<br>
              Technion - Israel Institute of Technology<br>
              Haifa 3200001, Israel
            </span>
          </div>
        </li>
      </ul>
    </div>

    <!-- Block 2: Logo Link -->
    <div class="bento-card bento-card-logo glass-dark d-flex flex-column p-0 overflow-hidden" style="height: 100%; min-height: 220px;">
      <a href="https://www.technion.ac.il/en/home-2/" target="_blank" class="h-50 w-100 d-flex flex-column align-items-center justify-content-center text-decoration-none" style="padding: 1.25rem; transition: background 0.3s; border-bottom: 1px solid rgba(255,255,255,0.15);" onmouseover="this.style.background='rgba(255,255,255,0.06)'" onmouseleave="this.style.background='transparent'">
        <img src="{{ 'assets/img/logos/Technion_Logo_transparent.png' | relative_url }}" alt="Technion Logo" style="width: 100%; max-width: 280px; max-height: 90%; object-fit: contain; filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.2));">
      </a>
      
      <a href="https://bme.technion.ac.il/en/" target="_blank" class="h-50 w-100 d-flex flex-column align-items-center justify-content-center text-decoration-none" style="padding: 0.5rem; transition: background 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.06)'" onmouseleave="this.style.background='transparent'">
        <img src="{{ 'assets/img/logos/bme_logo_transparent_hires.png' | relative_url }}" alt="BME Logo" style="width: 100%; max-width: 380px; max-height: 100%; object-fit: contain; filter: drop-shadow(0px 8px 12px rgba(0,0,0,0.2)); transform: scale(1.08);">
      </a>
    </div>

    <!-- Block 3: Embedded Map -->
    <div class="bento-card bento-card-map p-0 m-0 glass-dark d-flex" style="height: 100%; min-height: 380px;">
      <iframe 
          src="https://www.google.com/maps?q=Technion+Faculty+of+Biomedical+Engineering&ll=32.7752021,35.026504&z=17&output=embed" 
          width="100%" 
          height="100%" 
          style="border:0; width: 100%; height: 100%; position: absolute; top:0; left:0; filter: contrast(1.05) opacity(0.95); mix-blend-mode: normal;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade">
      </iframe>
    </div>

  </div>
</div>

<section style="padding: 1rem 1rem 2.5rem; text-align: center;">
  <div class="d-flex justify-content-center align-items-center flex-wrap" style="gap: 0.9rem;">
    <a href="https://www.linkedin.com/in/eddy-solomon-93159119b/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" style="color: #fff; font-size: 3.45rem; line-height: 1;">
      <i class="fa-brands fa-linkedin"></i>
    </a>
    <a href="https://github.com/eddysolo" target="_blank" rel="noopener noreferrer" aria-label="GitHub" style="color: #fff; font-size: 3.45rem; line-height: 1;">
      <i class="fa-brands fa-github"></i>
    </a>
    <a href="https://outlook.office.com/mail/deeplink/compose?to=eddy.solomon@technion.ac.il" target="_blank" rel="noopener noreferrer" aria-label="Outlook" style="color: #fff; font-size: 3.45rem; line-height: 1;">
      <i class="fa-solid fa-envelope"></i>
    </a>
    <a href="https://scholar.google.com/citations?user=tAOr0VwAAAAJ&hl=en" target="_blank" rel="noopener noreferrer" aria-label="Google Scholar" style="color: #fff; font-size: 3.45rem; line-height: 1;">
      <i class="ai ai-google-scholar"></i>
    </a>
  </div>
  <p style="margin-top: 0.8rem; margin-bottom: 0; font-size: 1rem; color: #fff;"></p>
</section>
