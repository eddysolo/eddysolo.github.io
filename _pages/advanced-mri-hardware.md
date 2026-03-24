---
layout: default
title: Advanced MRI Hardware
permalink: /advanced-mri-hardware/
fluid: true
no_hero: true
---

<style>
  .hw-shell {
    width: min(1240px, 92vw);
    margin: 0 auto;
  }

  .hw-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 1rem;
    align-items: stretch;
  }

  .hw-panel {
    border-radius: 22px;
    border: 1px solid rgba(17, 28, 38, 0.12);
    background: linear-gradient(165deg, rgba(247, 249, 252, 0.98), rgba(232, 237, 245, 0.98));
    box-shadow: 0 18px 44px rgba(17, 28, 38, 0.12);
  }

  .hw-copy {
    padding: clamp(1.1rem, 1.9vw, 2rem);
    display: flex;
    flex-direction: column;
  }

  .hw-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    font-size: 0.74rem;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    font-weight: 700;
    color: #3a4f64;
    margin-bottom: 0.75rem;
  }

  .hw-chip::before {
    content: "";
    width: 30px;
    height: 2px;
    border-radius: 999px;
    background: linear-gradient(90deg, #154360, #4c7aa1);
  }

  .hw-title {
    margin: 0 0 0.95rem 0;
    font-size: clamp(1.4rem, 2.5vw, 2.1rem);
    line-height: 1.3;
    color: #182a3a;
    font-weight: 800;
  }

  .hw-text {
    margin: 0;
    color: #2e4a60;
    line-height: 1.72;
    font-size: 1rem;
    max-width: 68ch;
  }

  .hw-badges {
    margin-top: 1rem;
    display: flex;
    gap: 0.55rem;
    flex-wrap: wrap;
  }

  .hw-badge {
    border-radius: 999px;
    padding: 0.35rem 0.8rem;
    font-size: 0.78rem;
    color: #163a52;
    background: rgba(21, 67, 96, 0.12);
    border: 1px solid rgba(21, 67, 96, 0.16);
  }

  .hw-visual {
    padding: 0.65rem;
    display: grid;
    grid-template-rows: 1fr 1fr auto;
    gap: 0.5rem;
    background:
      radial-gradient(circle at 92% 10%, rgba(110, 145, 180, 0.18), transparent 42%),
      linear-gradient(165deg, rgba(224, 233, 243, 0.98), rgba(206, 220, 236, 0.98));
  }

  .hw-image {
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid rgba(17, 28, 38, 0.1);
    padding: 0.45rem;
    min-height: 190px;
    display: flex;
  }

  .hw-image img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    border-radius: 10px;
  }

  .hw-caption {
    margin: 0;
    padding: 0.15rem 0.45rem 0.3rem;
    color: #2f4d63;
    font-size: 0.88rem;
    line-height: 1.45;
  }

  .hw-caption a {
    color: #194f78;
    text-decoration: underline;
    text-underline-offset: 0.14rem;
  }

  .hw-ref-wrap {
    margin-top: 1rem;
    border-radius: 22px;
    border: 1px solid rgba(17, 28, 38, 0.1);
    background: linear-gradient(180deg, rgba(247, 249, 252, 0.98), rgba(236, 242, 249, 0.98));
    padding: clamp(0.95rem, 1.7vw, 1.5rem);
  }

  .hw-ref-wrap h3 {
    margin: 0 0 0.95rem;
    font-size: 1.45rem;
    font-weight: 800;
    color: #1d3347;
    display: flex;
    align-items: center;
    gap: 0.55rem;
  }

  .hw-ref {
    height: 100%;
    display: flex;
    gap: 0.75rem;
    align-items: flex-start;
    border-radius: 14px;
    border: 1px solid rgba(17, 28, 38, 0.1);
    background: rgba(255, 255, 255, 0.92);
    padding: 0.85rem;
    color: #203b50;
    text-decoration: none;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .hw-ref:hover {
    transform: translateY(-3px);
    border-color: rgba(21, 67, 96, 0.34);
    box-shadow: 0 8px 20px rgba(17, 28, 38, 0.1);
    text-decoration: none;
  }

  .hw-ref-icon {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: grid;
    place-items: center;
    background: rgba(21, 67, 96, 0.12);
    color: #1a4866;
    flex-shrink: 0;
  }

  .hw-ref h5 {
    margin: 0 0 0.3rem;
    font-size: 0.98rem;
    line-height: 1.33;
    font-weight: 700;
    color: #1f3b50;
  }

  .hw-ref p {
    margin: 0;
    font-size: 0.88rem;
    color: #456178;
    font-family: monospace;
  }

  @media (max-width: 991.98px) {
    .hw-grid {
      grid-template-columns: 1fr;
    }

    .hw-image {
      min-height: 170px;
    }
  }
</style>

<div class="hw-shell">
  <section class="hw-grid">
    <article class="hw-panel hw-copy">
      <span class="hw-chip">Advanced MRI Hardware</span>
      <h2 class="hw-title">MR-compatible sensing and external tracking beyond conventional MRI.</h2>
      <p class="hw-text">
          We develop MRI hardware that enables fast, motion-robust imaging without requiring patient immobilization. Our approach integrates real-time, MR-safe, contactless smart sensors based on radiofrequency (RF) signals (e.g., pilot tone) to continuously capture cardiac, respiratory, and bulk motion. Coupled with accelerated acquisition, these frameworks provide real-time feedback, enabling free-motion and free-breathing MRI with improved image quality and reduced scan times.
      </p>

      <div class="hw-badges">
        <span class="hw-badge">MR-safe sensors</span>
        <span class="hw-badge">Pilot-tone tracking</span>
        <span class="hw-badge">Free-motion workflow</span>
      </div>
    </article>

    <article class="hw-panel hw-visual">
      <div class="hw-image">
        <img src="{{ '/assets/img/publication_preview/Free‐breathing radial imaging using a pilot‐tone radiofrequency transmitter for detection of respiratory motion.png' | relative_url }}" alt="Pilot-tone respiratory motion sensing figure from free-breathing radial MRI study">
      </div>
      <div class="hw-image">
        <img src="{{ '/assets/img/pilot-tone-image.png' | relative_url }}" alt="Pilot-tone hardware setup">
      </div>
      <p class="hw-caption">
        From
        <a href="https://pubmed.ncbi.nlm.nih.gov/33306216/" target="_blank" rel="noopener">Free-breathing radial imaging using a pilot-tone radiofrequency transmitter for detection of respiratory motion</a>
        and lab pilot-tone hardware imagery.
      </p>
    </article>
  </section>

  <section class="hw-ref-wrap">
    <h3><i class="fa-solid fa-book-open"></i> References</h3>
    <div class="row g-3">
      <div class="col-lg-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/33306216/" target="_blank" rel="noopener" class="hw-ref">
          <div class="hw-ref-icon">
            <i class="fa-solid fa-wave-square"></i>
          </div>
          <div>
            <h5>Free-breathing radial imaging using a pilot-tone radiofrequency transmitter for detection of respiratory motion</h5>
            <p>Magnetic Resonance in Medicine, 2021</p>
          </div>
        </a>
      </div>

      <div class="col-lg-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/41352869/" target="_blank" rel="noopener" class="hw-ref">
          <div class="hw-ref-icon">
            <i class="fa-solid fa-screwdriver-wrench"></i>
          </div>
          <div>
            <h5>Experience of how to build an MRI machine from scratch</h5>
            <p>Progress in Nuclear Magnetic Resonance Spectroscopy, 2025</p>
          </div>
        </a>
      </div>

      <div class="col-lg-6">
        <div class="hw-ref">
          <div class="hw-ref-icon">
            <i class="fa-solid fa-tower-broadcast"></i>
          </div>
          <div>
            <h5>Contactless sensing of internal motion using frequency-dependent Doppler radar</h5>
            <p>Featured as attached lab material</p>
          </div>
        </div>
      </div>

      <div class="col-lg-6">
        <a href="https://archive.ismrm.org/2021/1388.html" target="_blank" rel="noopener" class="hw-ref">
          <div class="hw-ref-icon">
            <i class="fa-solid fa-gauge-high"></i>
          </div>
          <div>
            <h5>Detecting Respiratory Motion Using Accelerometer Sensors: Preliminary Insight</h5>
            <p>ISMRM 2021, Abstract 1388</p>
          </div>
        </a>
      </div>
    </div>
  </section>
</div>
