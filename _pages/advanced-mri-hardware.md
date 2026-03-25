---
layout: default
title: Advanced MRI Hardware
permalink: /advanced-mri-hardware/
fluid: true
no_hero: true
---

<style>
  .cmri-shell {
    width: min(1220px, 92vw);
    margin: 0 auto;
  }

  .cmri-hero {
    border-radius: 28px;
    padding: clamp(1.3rem, 2vw, 2rem);
    background:
      radial-gradient(circle at 15% 15%, rgba(0, 153, 170, 0.2), transparent 40%),
      radial-gradient(circle at 90% 10%, rgba(255, 171, 47, 0.2), transparent 35%),
      linear-gradient(145deg, rgba(17, 29, 48, 0.9), rgba(11, 47, 69, 0.9));
    box-shadow: 0 28px 58px rgba(8, 16, 28, 0.32);
    color: #f4f8fc;
    overflow: hidden;
  }

  .cmri-kicker {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.18);
    font-size: 1.05rem;
    letter-spacing: 0.02em;
    text-transform: none;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 1rem;
  }

  .cmri-title {
    font-size: clamp(1.65rem, 3vw, 2.45rem);
    line-height: 1.22;
    letter-spacing: -0.025em;
    margin: 0 0 1.2rem 0;
    font-weight: 800;
    color: #ffffff;
  }

  .cmri-body {
    margin: 0;
    color: rgba(244, 248, 252, 0.96);
    line-height: 1.8;
    font-size: 1.15rem;
    font-weight: 400;
    max-width: 72ch;
  }

  .cmri-media-frame {
    height: 100%;
    min-height: 380px;
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.18);
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
    backdrop-filter: blur(2px);
  }

  .cmri-media-frame img {
    width: 100%;
    height: 100%;
    min-height: 0;
    object-fit: contain;
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.92);
    flex: 1 1 auto;
  }

  .cmri-media-grid {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
    flex: 1 1 auto;
    height: 100%;
  }

  .cmri-media-grid .cmri-media-tile {
    border-radius: 16px;
    background: rgba(8, 22, 38, 0.52);
    border: 1px solid rgba(255, 255, 255, 0.16);
    padding: 0.75rem;
    display: flex;
    flex-direction: column;
    flex: 1 1 auto;
  }

  .cmri-media-grid .cmri-media-figure {
    border-radius: 12px;
    background: rgba(8, 22, 38, 0.28);
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1 1 auto;
    overflow: hidden;
    min-height: 140px;
  }

  .cmri-media-grid .cmri-media-tile img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
    display: block;
    border-radius: 10px;
  }

  .cmri-media-grid .cmri-media-tile img.cmri-native-res {
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
    margin: 0;
    object-fit: contain;
    object-position: center;
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;
  }

  .cmri-media-tile .cmri-caption {
    margin: 0.48rem 0 0;
    font-size: 0.84rem;
    line-height: 1.45;
    color: rgba(232, 244, 255, 0.95);
  }

  .cmri-caption {
    margin-top: 0.75rem;
    margin-bottom: 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: rgba(244, 248, 252, 0.92);
  }

  .cmri-caption a {
    color: #98f0ff;
    text-decoration: underline;
    text-underline-offset: 0.16rem;
  }

  .cmri-references {
    margin-top: 1.15rem;
  }

  .cmri-references h3 {
    margin: 0 0 1.35rem 0;
    font-size: 1.65rem;
    font-weight: 800;
    color: #f8fbff;
  }

  .cmri-paper {
    height: 100%;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.16);
    background: linear-gradient(150deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.08)) !important;
    padding: 1rem;
    color: #f8fbff !important;
    text-decoration: none !important;
    background-image: linear-gradient(150deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.08)) !important;
    display: grid;
    grid-template-columns: auto 1fr;
    column-gap: 0.9rem;
    align-items: flex-start;
    transition: transform 0.22s ease, box-shadow 0.22s ease;
  }

  .cmri-paper:hover {
    transform: translateY(-4px);
    background: linear-gradient(150deg, rgba(255, 255, 255, 0.28), rgba(255, 255, 255, 0.1)) !important;
    text-decoration: none !important;
    background-image: linear-gradient(150deg, rgba(255, 255, 255, 0.28), rgba(255, 255, 255, 0.1)) !important;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.14);
  }

  .cmri-paper-icon {
    width: 46px;
    height: 46px;
    border-radius: 12px;
    display: grid;
    place-items: center;
    background: rgba(152, 240, 255, 0.2);
    color: #d4f8ff;
    flex-shrink: 0;
  }

  .cmri-paper h5 {
    margin: 0 0 0.45rem 0;
    font-size: 1.08rem;
    line-height: 1.45;
    font-weight: 800;
    letter-spacing: -0.01em;
    color: #ffffff;
  }

  .cmri-paper p {
    margin: 0;
    font-size: 0.95rem;
    color: rgba(244, 248, 252, 0.88);
    font-family: inherit;
    font-style: italic;
    opacity: 0.95;
  }

  @media (max-width: 991.98px) {
    .cmri-hero {
      padding: 1.1rem;
    }

    .cmri-media-grid .cmri-media-tile {
      min-height: 168px;
    }

    .cmri-references {
      margin-top: 1.25rem;
    }
  }
</style>

<div class="cmri-shell">
  <section class="cmri-hero">
    <div class="row g-3 align-items-stretch">
      <div class="col-lg-7">
        <span class="cmri-kicker"><i class="fa-solid fa-tower-broadcast"></i> Advanced MRI Hardware</span>
        <h2 class="cmri-title">MR-compatible sensing and external tracking beyond conventional MRI.</h2>
        <p class="cmri-body">
          We develop MRI hardware that enables fast, motion-robust imaging without requiring patient immobilization. Our approach integrates real-time, MR-safe, contactless smart sensors based on radiofrequency (RF) signals (e.g., pilot tone) to continuously capture cardiac, respiratory, and bulk motion. Coupled with accelerated acquisition, these frameworks provide real-time feedback, enabling free-motion and free-breathing MRI with improved image quality and reduced scan times.
        </p>
      </div>

      <div class="col-lg-5">
        <div class="cmri-media-grid">
          <div class="cmri-media-tile">
            <div class="cmri-media-figure">
              <img src="{{ '/assets/img/publication_preview/Free‐breathing radial imaging using a pilot‐tone radiofrequency transmitter for detection of respiratory motion.png' | relative_url }}" alt="Pilot-tone respiratory motion sensing figure from free-breathing radial MRI study">
            </div>
            <p class="cmri-caption">
              Figure 1.
              <a href="https://pubmed.ncbi.nlm.nih.gov/33306216/" target="_blank" rel="noopener">Free-breathing radial imaging using a pilot-tone radiofrequency transmitter for detection of respiratory motion</a>.
            </p>
          </div>
          <div class="cmri-media-tile">
            <div class="cmri-media-figure">
              <img class="cmri-native-res" src="{{ '/assets/img/pilot-tone-image.png' | relative_url }}" alt="Contactless hand and pilot-tone sensing setup">
            </div>
            <p class="cmri-caption">
              Pilot tone setup
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cmri-hero cmri-references">
    <h3>Relevant Articles</h3>
    <div class="row g-3" style="row-gap: 1.5rem;">
      <div class="col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/33306216/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
          </div>
          <div>
            <h5>Free-breathing radial imaging using a pilot-tone radiofrequency transmitter for detection of respiratory motion</h5>
            <p>Magnetic Resonance in Medicine, 2021</p>
          </div>
        </a>
      </div>

      <div class="col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/41352869/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
          </div>
          <div>
            <h5>Experience of how to build an MRI machine from scratch</h5>
            <p>Progress in Nuclear Magnetic Resonance Spectroscopy, 2025</p>
          </div>
        </a>
      </div>

      <div class="col-md-6">
        <a href="https://archive.ismrm.org/2021/1388.html" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
          </div>
          <div>
            <h5>Detecting Respiratory Motion Using Accelerometer Sensors: Preliminary Insight</h5>
            <p>ISMRM 2021, Abstract 1388</p>
          </div>
        </a>
      </div>

      <div class="col-md-6">
        <a href="#" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
          </div>
          <div>
            <h5>Contactless sensing of internal motion using frequency-dependent Doppler radar</h5>
            <p>Coming Soon</p>
          </div>
        </a>
      </div>
    </div>
  </section>
</div>
