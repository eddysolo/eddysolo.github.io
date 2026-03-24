---
layout: default
title: Computational MRI
permalink: /computational-mri/
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
    padding: 0.4rem 0.8rem;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.16);
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1rem;
  }

  .cmri-title {
    font-size: clamp(1.45rem, 2.7vw, 2.15rem);
    line-height: 1.28;
    margin: 0 0 1rem 0;
    font-weight: 800;
    color: #f8fbff;
  }

  .cmri-body {
    margin: 0;
    color: rgba(244, 248, 252, 0.95);
    line-height: 1.72;
    font-size: 1.02rem;
    max-width: 68ch;
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
    background: linear-gradient(150deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.08));
    padding: 1rem;
    color: #f8fbff;
    text-decoration: none;
    display: grid;
    grid-template-columns: auto 1fr;
    column-gap: 0.9rem;
    align-items: flex-start;
    transition: transform 0.22s ease, border-color 0.22s ease, background 0.22s ease;
  }

  .cmri-paper:hover {
    transform: translateY(-4px);
    border-color: rgba(152, 240, 255, 0.5);
    background: linear-gradient(150deg, rgba(255, 255, 255, 0.28), rgba(255, 255, 255, 0.1));
    text-decoration: none;
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
    margin: 0 0 0.4rem 0;
    font-size: 1rem;
    line-height: 1.35;
    font-weight: 700;
    color: #f9fcff;
  }

  .cmri-paper p {
    margin: 0;
    font-size: 0.9rem;
    color: rgba(244, 248, 252, 0.86);
    font-family: monospace;
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
        <span class="cmri-kicker"><i class="fa-solid fa-microchip"></i> Computational MRI</span>
        <h2 class="cmri-title">Novel sampling and reconstruction methods: from accelerated k-space acquisition to diagnostic-quality image.</h2>
        <p class="cmri-body">
          We develop advanced sampling and reconstruction methods for ultrafast dynamic MRI, overcoming traditional trade-offs between spatial resolution, temporal resolution, and scan time. Our methods, such as ELITE, combine locally low-rank subspace modeling, compressed sensing, and deep learning to suppress undersampling artifacts while preserving temporal fidelity. These techniques enable high temporal-resolution imaging that improves lesion characterization, reduce noise, and support reliable quantitative kinetic analysis in applications such as dynamic contrast-enhanced (DCE) breast and abdominal MRI.
        </p>
      </div>

      <div class="col-lg-5">
        <div class="cmri-media-frame">
          <img src="{{ '/assets/img/publication_preview/Dynamic MRI with Locally Low-Rank Subspace Constraint Towards 1-Second Temporal Resolution Aided by Deep Learning.png' | relative_url }}" alt="Figure 1 from the ELITE dynamic MRI publication">
          <p class="cmri-caption">
          From
          <a href="https://pubmed.ncbi.nlm.nih.gov/40060040/" target="_blank" rel="noopener">Dynamic MRI with Locally Low-Rank Subspace Constraint: Towards 1-Second Temporal Resolution Aided by Deep Learning</a>.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="cmri-hero cmri-references">
    <h3><i class="fa-solid fa-book-open"></i> References</h3>
    <div class="row g-3">
      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/40060040/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-file-waveform"></i>
          </div>
          <div>
            <h5>Dynamic MRI with Locally Low-Rank Subspace Constraint: Towards 1-Second Temporal Resolution Aided by Deep Learning</h5>
            <p>Research Square, 2025</p>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/39772976/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-database"></i>
          </div>
          <div>
            <h5>FastMRI Breast: A Publicly Available Radial k-Space Dataset of Breast Dynamic Contrast-enhanced MRI</h5>
            <p>Radiology: Artificial Intelligence, 2025</p>
          </div>
        </a>
      </div>

      <div class="col-lg-4 col-md-6">
        <a href="https://pubmed.ncbi.nlm.nih.gov/37655444/" target="_blank" rel="noopener" class="cmri-paper">
          <div class="cmri-paper-icon">
            <i class="fa-solid fa-layer-group"></i>
          </div>
          <div>
            <h5>mcLARO: Multi-contrast learned acquisition and reconstruction optimization for simultaneous quantitative multi-parametric mapping</h5>
            <p>Magnetic Resonance in Medicine, 2024</p>
          </div>
        </a>
      </div>
    </div>
  </section>
</div>
