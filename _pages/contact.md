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
  body {
    background-image: url('{{ "assets/img/technion_contact_bg_google.jpg" | relative_url }}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
  }
  
  body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: linear-gradient(135deg, rgba(8, 20, 48, 0.85) 0%, rgba(0, 93, 143, 0.75) 100%);
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
    background: rgba(0, 0, 0, 0.4);
    z-index: -1;
  }

  /* Bento Box Actual Grid Structure */
  .bento-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2vw;
    padding: 2.5vw;
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
    border-radius: 32px;
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
    <div class="bento-card bento-card-main glass-dark p-4 p-md-5 d-flex flex-column justify-content-center text-left" style="height: 100%;">
      <h2 class="mb-4" style="font-weight: 800; color: #ffffff; font-size: 3.5rem; letter-spacing: -0.02em;">Get in Touch</h2>
      <p class="mb-5" style="font-size: 1.35rem; line-height: 1.6; color: rgba(255,255,255,0.85);">
        We are always looking for passionate scientists and students to join our team! Whether you are seeking a PhD position, looking for collaboration, or have a general inquiry, our inbox is open.
      </p>

      <ul class="list-unstyled mb-0 mt-auto">
        <!-- Email -->
        <li class="mb-5 d-flex align-items-center">
          <div style="background: rgba(144, 216, 255, 0.15); height: 80px; width: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1.5rem; flex-shrink: 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <i class="fa-solid fa-envelope" style="color: #90d8ff; font-size: 2rem;"></i>
          </div>
          <div>
            <h5 class="mb-1" style="font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.15em;">Email Us</h5>
            <a href="mailto:{{ site.email | default: 'eddy.solomon@bm.technion.ac.il' }}" style="font-size: 1.5rem; color: #ffffff; text-decoration: none; font-weight: 700;">{{ site.email | default: "eddy.solomon@bm.technion.ac.il" }}</a>
          </div>
        </li>
        <!-- Location -->
        <li class="d-flex align-items-center">
          <div style="background: rgba(144, 216, 255, 0.15); height: 80px; width: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 1.5rem; flex-shrink: 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <i class="fa-solid fa-location-dot" style="color: #90d8ff; font-size: 2rem;"></i>
          </div>
          <div>
            <h5 class="mb-1" style="font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; font-size: 0.9rem; letter-spacing: 0.15em;">Visit Our Lab</h5>
            <span style="font-size: 1.3rem; line-height: 1.5; display: inline-block; color: #ffffff; font-weight: 500;">
              Faculty of Biomedical Engineering<br>
              Technion - Israel Institute of Technology<br>
              Haifa 3200003, Israel
            </span>
          </div>
        </li>
      </ul>
    </div>

    <!-- Block 2: Logo Link -->
    <a href="https://bme.technion.ac.il/en/" target="_blank" class="bento-card bento-card-logo glass-light d-flex flex-column align-items-center justify-content-center text-decoration-none p-4 p-xl-5" style="height: 100%; min-height: 340px; gap: 0.8rem; padding-top: 1rem; padding-bottom: 0.75rem;">
      <img src="{{ 'assets/img/logos/bme_logo_transparent_hires.png' | relative_url }}" alt="BME Logo" style="width: 120%; max-width: 120%; height: auto; object-fit: contain; image-rendering: auto; transform: translateY(-8px); filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.1));">
      <div style="background: #002b5b; color: white; padding: 0.7rem 1.5rem; border-radius: 50px; font-weight: 800; font-size: 0.95rem; display: inline-flex; align-items: center; gap: 0.6rem; box-shadow: 0 10px 25px rgba(0, 43, 91, 0.4); text-transform: uppercase; letter-spacing: 0.03em; transition: all 0.3s; margin-top: 0.2rem;">
        Go to website <i class="fa-solid fa-arrow-right"></i>
      </div>
    </a>

    <!-- Block 3: Embedded Map -->
    <div class="bento-card bento-card-map p-0 m-0 glass-dark d-flex" style="height: 100%; min-height: 350px;">
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
