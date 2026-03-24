---
layout: default
title: Motion-Robust MRI
permalink: /motion-robust-mri/
fluid: true
no_hero: true
---

<style>
  .mr-shell {
    width: min(1240px, 92vw);
    margin: 0 auto;
  }

  .mr-hero {
    border-radius: 26px;
    overflow: hidden;
    background:
      linear-gradient(145deg, rgba(245, 250, 255, 0.96), rgba(234, 246, 255, 0.96)),
      linear-gradient(90deg, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0));
    border: 1px solid rgba(0, 94, 124, 0.12);
    box-shadow: 0 22px 50px rgba(8, 42, 61, 0.16);
  }

  .mr-hero .row {
    margin: 0;
  }

  .mr-copy {
    padding: clamp(1.3rem, 2vw, 2.1rem);
    border-left: 6px solid rgba(0, 158, 185, 0.7);
  }

  .mr-kicker {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    border-radius: 999px;
    padding: 0.36rem 0.85rem;
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    background: rgba(0, 158, 185, 0.12);
    color: #025f74;
    margin-bottom: 0.95rem;
    font-weight: 700;
  }

  .mr-title {
    font-size: clamp(1.4rem, 2.6vw, 2.1rem);
    line-height: 1.3;
    margin: 0 0 1rem 0;
    font-weight: 800;
    color: #07364f;
  }

  .mr-text {
    margin: 0;
    font-size: 1rem;
    line-height: 1.74;
    color: rgba(7, 54, 79, 0.92);
    max-width: 70ch;
  }

  .mr-media {
    padding: clamp(1rem, 1.8vw, 1.6rem);
    display: flex;
    flex-direction: column;
    background: linear-gradient(180deg, rgba(0, 158, 185, 0.08), rgba(0, 158, 185, 0.03));
  }

  .mr-figure {
    border-radius: 16px;
    border: 1px solid rgba(0, 94, 124, 0.14);
    padding: 0.65rem;
    background: rgba(255, 255, 255, 0.88);
    box-shadow: 0 12px 26px rgba(3, 39, 57, 0.14);
  }

  .mr-figure img {
    width: 100%;
    height: 100%;
    min-height: 280px;
    max-height: 430px;
    object-fit: contain;
    border-radius: 10px;
    background: #fff;
  }

  .mr-caption {
    margin: 0.75rem 0 0 0;
    font-size: 0.9rem;
    line-height: 1.5;
    color: #124056;
  }

  .mr-caption a {
    color: #006b86;
    text-decoration: underline;
    text-underline-offset: 0.15rem;
  }

  .mr-stats {
    margin-top: 0.9rem;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.55rem;
  }

  .mr-stat {
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(0, 94, 124, 0.12);
    padding: 0.65rem 0.6rem;
    text-align: center;
  }

  .mr-stat b {
    display: block;
    font-size: 0.95rem;
    line-height: 1.25;
    color: #064158;
  }

  .mr-stat span {
    display: block;
    margin-top: 0.22rem;
    font-size: 0.75rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: #1f6882;
  }

  .mr-ref-wrap {
    margin-top: 1rem;
    padding: clamp(1rem, 1.8vw, 1.8rem);
    border-radius: 24px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.84), rgba(242, 250, 255, 0.92));
    border: 1px solid rgba(0, 94, 124, 0.12);
  }

  .mr-ref-wrap h3 {
    margin: 0 0 1rem 0;
    font-size: 1.5rem;
    font-weight: 800;
    color: #06374e;
    display: flex;
    align-items: center;
    gap: 0.55rem;
  }

  .mr-ref {
    display: flex;
    gap: 0.9rem;
    border-radius: 14px;
    border: 1px solid rgba(0, 94, 124, 0.12);
    background: rgba(255, 255, 255, 0.9);
    padding: 0.95rem;
    text-decoration: none;
    color: #07364f;
    height: 100%;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  }

  .mr-ref:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(6, 55, 78, 0.12);
    border-color: rgba(0, 158, 185, 0.4);
    text-decoration: none;
  }

  .mr-ref-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    flex-shrink: 0;
    display: grid;
    place-items: center;
    background: rgba(0, 158, 185, 0.14);
    color: #005f76;
  }

  .mr-ref h5 {
    margin: 0 0 0.35rem 0;
    font-size: 1rem;
    line-height: 1.34;
    font-weight: 700;
    color: #07364f;
  }

  .mr-ref p {
    margin: 0;
    font-size: 0.9rem;
    color: #2d6074;
    font-family: monospace;
  }

  @media (max-width: 991.98px) {
    .mr-copy {
      border-left: 0;
      border-top: 5px solid rgba(0, 158, 185, 0.7);
    }

    .mr-figure img {
      max-height: 320px;
    }

    .mr-stats {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 575.98px) {
    .mr-stats {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="mr-shell">
  <section class="mr-hero">
    <div class="row g-0 align-items-stretch">
      <div class="col-lg-7">
        <div class="mr-copy">
          <span class="mr-kicker"><i class="fa-solid fa-wave-square"></i> Motion-Robust MRI</span>
          <h2 class="mr-title">Motion-robust MRI for free breathing, reliable imaging</h2>
          <p class="mr-text">
          One of the greatest challenges in medical imaging is patient motion. Breathing, heartbeat, and voluntary motion can degrade image quality and limit diagnostic reliability. We develop motion-robust MRI methods that leverage the inherent robustness of non-Cartesian acquisition strategies to motion which enables prospective and retrospective correction. By integrating advanced image reconstruction and physics-informed deep learning, our approaches, such as MP-RAVE, enable high-resolution structural brain imaging in minutes while correcting for head motion. By reducing scan time and eliminating the need for sedation/anesthesia, our methods improve the reliability and accessibility of brain and abdominal MRI.
          </p>
        </div>
      </div>

      <div class="col-lg-5">
        <div class="mr-media">
          <div class="mr-figure">
            <img src="{{ '/assets/img/publication_preview/MP-RAVE IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction.png' | relative_url }}" alt="Figure 5 from MP-RAVE motion-robust MRI study">
          </div>
          <p class="mr-caption">
            From
            <a href="https://pubmed.ncbi.nlm.nih.gov/36763847/" target="_blank" rel="noopener">MP-RAVE: IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction</a>.
          </p>

          <div class="mr-stats">
            <div class="mr-stat">
              <b>Free Breathing</b>
              <span>Acquisition</span>
            </div>
            <div class="mr-stat">
              <b>Retrospective</b>
              <span>Motion Correction</span>
            </div>
            <div class="mr-stat">
              <b>No Sedation</b>
              <span>Improved Access</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="mr-ref-wrap">
    <h3><i class="fa-solid fa-book-open"></i> References</h3>
    <div class="row g-3">
      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/36763847/" target="_blank" rel="noopener" class="mr-ref">
          <div class="mr-ref-icon">
            <i class="fa-solid fa-brain"></i>
          </div>
          <div>
            <h5>MP-RAVE: IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction</h5>
            <p>Magnetic Resonance in Medicine, 2023</p>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/33306216/" target="_blank" rel="noopener" class="mr-ref">
          <div class="mr-ref-icon">
            <i class="fa-solid fa-wind"></i>
          </div>
          <div>
            <h5>Free-breathing radial imaging using a pilot-tone radiofrequency transmitter for detection of respiratory motion</h5>
            <p>Magnetic Resonance in Medicine, 2021</p>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/40511639/" target="_blank" rel="noopener" class="mr-ref">
          <div class="mr-ref-icon">
            <i class="fa-solid fa-wave-square"></i>
          </div>
          <div>
            <h5>Free-Breathing Hybrid Technique for Simultaneous Morphological and Quantitative Abdominal Imaging at 0.55 T</h5>
            <p>Investigative Radiology, 2026</p>
          </div>
        </a>
      </div>
    </div>
  </section>

</div>
