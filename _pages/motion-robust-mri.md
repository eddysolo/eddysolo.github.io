---
layout: default
title: Motion-Robust MRI
permalink: /motion-robust-mri/
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
    min-height: 320px;
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
    object-position: center;
    border-radius: 14px;
    background: transparent;
    flex: 1 1 auto;
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
    display: flex;
    align-items: center;
    gap: 0.65rem;
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

    .cmri-media-frame {
      min-height: 320px;
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
        <span class="cmri-kicker"><i class="fa-solid fa-heart-pulse"></i> Motion-Robust MRI</span>
        <h2 class="cmri-title">Motion-robust MRI for free breathing, reliable imaging</h2>
        <p class="cmri-body">
          One of the greatest challenges in medical imaging is patient motion. Breathing, heartbeat, and voluntary motion can degrade image quality and limit diagnostic reliability. We develop motion-robust MRI methods that leverage the inherent robustness of non-Cartesian acquisition strategies to motion which enables prospective and retrospective correction. By integrating advanced image reconstruction and physics-informed deep learning, our approaches, such as MP-RAVE, enable high-resolution structural brain imaging in minutes while correcting for head motion. By reducing scan time and eliminating the need for sedation/anesthesia, our methods improve the reliability and accessibility of brain and abdominal MRI.
        </p>
      </div>

      <div class="col-lg-5">
        <div class="cmri-media-frame">
          <img src="{{ '/assets/img/publication_preview/MP-RAVE IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction.png' | relative_url }}" alt="Figure 5 from MP-RAVE motion-robust MRI study">
          <p class="cmri-caption">
            From
            <a href="https://pubmed.ncbi.nlm.nih.gov/36763847/" target="_blank" rel="noopener">MP-RAVE: IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction</a>.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="cmri-hero cmri-references">
    <h3>Relevant Articles</h3>
    <div class="row g-3" style="row-gap: 1.5rem;">
      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/36763847/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
          </div>
          <div>
            <h5>MP-RAVE: IR-Prepared T1-Weighted Radial Stack-of-Stars 3D GRE imaging with retrospective motion correction</h5>
            <p>Magnetic Resonance in Medicine, 2023</p>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
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

      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/40511639/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-book"></i>
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
