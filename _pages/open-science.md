---
layout: default
title: Open Science
permalink: /open-science/
description: A showcase of our best work and open science contributions.
nav: false
nav_order: 5
fluid: true
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
  <div class="glass-section w-100 d-flex flex-column justify-content-center align-items-center text-center mb-5" style="border-radius: 24px; padding: 4rem 3rem;">
    <h1 style="font-weight: 800; font-size: 3rem; margin-bottom: 0.75rem;">Open Science</h1>
    <h3 style="font-weight: 600; font-size: 1.5rem; color: var(--global-theme-color); margin-bottom: 0;">Our open science contributions and resources</h3>
  </div>

  <ul class="nav nav-pills justify-content-center mb-4" id="open-science-tabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="code-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#code-pane" data-bs-target="#code-pane" type="button" role="tab" aria-controls="code-pane" aria-selected="true" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Code &amp; Repositories</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="popular-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#popular-pane" data-bs-target="#popular-pane" type="button" role="tab" aria-controls="popular-pane" aria-selected="false" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Popular Science</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="patents-tab" data-toggle="pill" data-bs-toggle="pill" data-target="#patents-pane" data-bs-target="#patents-pane" type="button" role="tab" aria-controls="patents-pane" aria-selected="false" style="border-radius: 999px; padding: 0.75rem 1.5rem; font-weight: 600; margin: 0 0.5rem;">Patents</button>
    </li>
  </ul>

  <div class="tab-content" id="open-science-content">
    <div class="tab-pane fade show active" id="code-pane" role="tabpanel" aria-labelledby="code-tab">
      <div class="row g-4">
        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px; color: inherit;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-database fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">
                <a href="{{ '/fastmri-dataset/' | relative_url }}" class="text-decoration-none" style="color: inherit;">FastMRI &amp; Breast DCE MRI Dataset</a>
              </h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Open-source MRI dataset support for reconstruction and machine learning research.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">We contributed Breast DCE MRI data to the NYU FastMRI ecosystem to support robust reconstruction benchmarks and reproducible algorithm development.</p>
            <img src="{{ '/assets/img/publication_preview/breast%20scan%20example.png' | relative_url }}" alt="fastMRI breast dataset preview" class="mt-3 w-100" style="border-radius: 16px; object-fit: cover;">
          </div>
        </div>

        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-brands fa-github fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">Lab Repositories</h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Curated software and reproducible pipelines.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">Source code, experiment scripts, and implementation notes for our MRI reconstruction and motion-robust imaging studies.</p>
            <a href="{{ '/repositories/' | relative_url }}" class="btn btn-outline-primary mt-2 align-self-start">View Repositories</a>
          </div>
        </div>
      </div>
    </div>

    <div class="tab-pane fade" id="popular-pane" role="tabpanel" aria-labelledby="popular-tab">
      <div class="row g-4">
        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-newspaper fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">Public Outreach</h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Explaining MRI innovation for broader audiences.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">Interviews, explainers, and educational pieces that translate advanced imaging research into practical, patient-centered language.</p>
            <span class="btn btn-outline-primary disabled mt-2 align-self-start" aria-disabled="true">Coming Soon</span>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-circle-play fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">Talks &amp; Media</h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Videos and talks for non-specialist viewers.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">A home for seminars, short videos, and media content that communicate how faster MRI can improve real clinical workflows.</p>
            <span class="btn btn-outline-primary disabled mt-2 align-self-start" aria-disabled="true">Coming Soon</span>
          </div>
        </div>
      </div>
    </div>

    <div class="tab-pane fade" id="patents-pane" role="tabpanel" aria-labelledby="patents-tab">
      <div class="row g-4">
        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-file-signature fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">Patent Portfolio</h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Translational IP from MRI methods and systems.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">Filed and granted innovations that support clinical deployment of our reconstruction, acquisition, and hardware-integrated imaging technologies.</p>
            <span class="btn btn-outline-primary disabled mt-2 align-self-start" aria-disabled="true">Add Patent Entries</span>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 24px;">
            <div class="d-flex align-items-center mb-3">
              <i class="fa-solid fa-lightbulb fa-2x mr-3" style="color: var(--global-text-color);"></i>
              <h3 style="font-weight: 800; margin: 0;">Invention Pipeline</h3>
            </div>
            <p style="font-size: 1.1rem; color: var(--global-theme-color); font-weight: 700;">Emerging ideas moving toward protection.</p>
            <p style="font-size: 1.05rem; flex-grow: 1;">Track pending invention disclosures and future patent-ready concepts connected to acceleration, robustness, and multimodal sensing in MRI.</p>
            <span class="btn btn-outline-primary disabled mt-2 align-self-start" aria-disabled="true">Coming Soon</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
