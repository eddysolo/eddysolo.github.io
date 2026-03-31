---
layout: page
title: Tissue Segmentation Model (ELITE)
description: Segmentation-guided reconstruction for accelerated breast DCE MRI.
img: assets/img/breast scan example.png
importance: 1
category: work
related_publications: true
published: false
---

<div class="container-fluid px-0 mx-auto" style="max-width: 90%; width: 90%;">
    <div class="row g-4 mb-4 align-items-stretch">
        <div class="col-lg-7">
            <div class="glass-box p-4 p-md-5 h-100 d-flex flex-column justify-content-center" style="border-radius: 24px; font-size: 1.18rem; line-height: 1.6;">
                <h2 style="font-weight: 800; margin-bottom: 1.25rem; display: flex; align-items: center;">
                    <i class="fa-solid fa-brain fa-lg mr-3" style="color: var(--global-theme-color);"></i>
                    Tissue Segmentation Model for DCE MRI
                </h2>
                <p>
                    This project develops a <strong>segmentation-guided model</strong> that separates tissue compartments in dynamic contrast-enhanced breast MRI and uses those priors to stabilize accelerated reconstruction.
                </p>
                <p class="mb-0">
                    The framework connects segmentation and reconstruction in one workflow so that temporal dynamics are preserved while reducing streaking and noise in highly undersampled acquisitions.
                </p>
            </div>
        </div>

        <div class="col-lg-5">
            <div class="glass-box p-4 h-100 d-flex align-items-center justify-content-center" style="border-radius: 24px; background: rgba(0,0,0,0.05);">
                <img
                    src="{{ '/assets/img/breast%20scan%20example.png' | relative_url }}"
                    alt="Breast tissue segmentation project preview"
                    style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);"
                >
            </div>
        </div>
    </div>

    <div class="row g-4 mb-4 align-items-stretch">
        <div class="col-lg-4">
            <div class="glass-box p-4 h-100" style="border-radius: 20px; border: 1px solid rgba(0,150,199,0.25); background: rgba(0,150,199,0.06);">
                <h4 style="font-weight: 800; margin-bottom: 0.9rem; display: flex; align-items: center;">
                    <i class="fa-solid fa-user-doctor mr-2" style="color: var(--global-theme-color);"></i>
                    Lead Contributor
                </h4>
                <p style="font-size: 1.08rem; margin-bottom: 0.8rem;"><strong>Eddy Solomon</strong> leads this project and its ELITE integration strategy.</p>
                <a href="{{ '/team/eddy-solomon/' | relative_url }}" class="btn btn-outline-primary w-100" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
                    View Research Profile
                </a>
            </div>
        </div>

        <div class="col-lg-8">
            <div class="glass-box p-4 h-100" style="border-radius: 20px;">
                <h4 style="font-weight: 800; margin-bottom: 0.9rem; display: flex; align-items: center;">
                    <i class="fa-solid fa-diagram-project mr-2" style="color: var(--global-theme-color);"></i>
                    Methods
                </h4>
                <div class="row g-3">
                    <div class="col-md-4">
                        <div class="glass-box p-3 h-100" style="border-radius: 14px;">
                            <h6 style="font-weight: 800; margin-bottom: 0.5rem;">Segmentation Priors</h6>
                            <p class="mb-0" style="font-size: 0.98rem;">Generate tissue masks for compartment-aware temporal basis estimation.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="glass-box p-3 h-100" style="border-radius: 14px;">
                            <h6 style="font-weight: 800; margin-bottom: 0.5rem;">ELITE + ResNet</h6>
                            <p class="mb-0" style="font-size: 0.98rem;">Use low-rank ELITE reconstruction with ResNet-enhanced low-resolution guidance.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="glass-box p-3 h-100" style="border-radius: 14px;">
                            <h6 style="font-weight: 800; margin-bottom: 0.5rem;">Clinical Evaluation</h6>
                            <p class="mb-0" style="font-size: 0.98rem;">Assess dynamic fidelity, lesion conspicuity, and artifact suppression.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row g-4 mb-4 align-items-stretch">
        <div class="col-lg-6">
            <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 20px;">
                <h4 style="font-weight: 800; margin-bottom: 1rem; display: flex; align-items: center;">
                    <i class="fa-solid fa-bolt mr-2" style="color: var(--global-theme-color);"></i>
                    Impact
                </h4>
                <p style="font-size: 1.05rem; margin-bottom: 0.8rem;">This work enables faster breast DCE MRI with improved robustness at high acceleration factors.</p>
                <p style="font-size: 1.05rem; margin-bottom: 0;">By combining segmentation with ELITE, the pipeline improves temporal consistency and supports more reliable downstream quantitative analysis.</p>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="glass-box p-4 h-100 d-flex flex-column" style="border-radius: 20px;">
                <h4 style="font-weight: 800; margin-bottom: 1rem; display: flex; align-items: center;">
                    <i class="fa-solid fa-link mr-2" style="color: var(--global-theme-color);"></i>
                    Links
                </h4>
                <a href="https://github.com/eddysolo/ELITE" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px;">
                    <i class="fa-brands fa-github mr-2"></i>
                    ELITE Repository Page
                </a>
                <a href="https://doi.org/10.21203/rs.3.rs-5448452/v1" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-lg mb-3 text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
                    <i class="fa-solid fa-file-lines mr-2"></i>
                    ELITE Article (Preprint)
                </a>
                <a href="{{ '/elite-segmentation-gallery/' | relative_url }}" class="btn btn-outline-primary btn-lg text-left" style="font-weight: 700; border-radius: 12px; border-width: 2px;">
                    <i class="fa-solid fa-images mr-2"></i>
                    Open Image + Links Page
                </a>
            </div>
        </div>
    </div>

    <div class="glass-section mb-5" style="border-radius: 24px; padding: 2.5rem;">
        <h3 style="font-weight: 800; font-size: 1.8rem; margin-bottom: 1rem; display: flex; align-items: center;">
            <i class="fa-solid fa-book-open-reader fa-sm mr-3" style="color: var(--global-theme-color);"></i>
            References
        </h3>
        <ul style="font-size: 1.03rem; margin-bottom: 0; padding-left: 1.2rem; line-height: 1.6;">
            <li>ELITE project preprint: Enhanced Locally low-rank Imaging for Tissue contrast Enhancement (ELITE). DOI: 10.21203/rs.3.rs-5448452/v1.</li>
            <li>fastMRI Breast dataset paper: A publicly available radial k-space dataset of breast dynamic contrast-enhanced MRI. Radiology: Artificial Intelligence (2024). DOI: 10.1148/ryai.240345.</li>
            <li>DRO toolkit reference used in ELITE training context: Digital reference object toolkit of breast DCE MRI for quantitative evaluation of image reconstruction and analysis methods. DOI: 10.1002/mrm.30152.</li>
        </ul>
    </div>
</div>
