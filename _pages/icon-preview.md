---
layout: default
permalink: /icon-preview/
title: 100+ Icon Alternatives
no_hero: true
---

<style>
.icon-box {
  border: 1px solid rgba(0, 150, 199, 0.2);
  border-radius: 12px;
  padding: 1.25rem 0.5rem;
  text-align: center;
  background: var(--global-bg-color);
  margin-bottom: 0.5rem;
  transition: transform 0.2s ease, border-color 0.2s;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.icon-box:hover {
  transform: translateY(-4px);
  border-color: rgba(0, 150, 199, 0.6);
  box-shadow: 0 4px 12px rgba(0, 150, 199, 0.1);
}
.icon-box i {
  font-size: 2rem;
  color: var(--global-theme-color);
  margin-bottom: 0.75rem;
}
.icon-box h4 {
  font-size: 0.8rem;
  margin: 0;
  font-weight: 600;
  word-wrap: break-word;
}
</style>

<div class="container mt-5 mb-5" style="max-width: 1400px;">
  <h1 class="mb-4 text-center">Icon Directory (140+ Research Subpage Options)</h1>
  <p class="text-center mb-5">Browse these medical, AI, physics, and hardware icons. Just pick the names of the ones you like!</p>
  
  <h2 class="mt-5 mb-4 border-bottom pb-2">1. Computing, AI, Data & Hardware</h2>
  <div class="row g-3">
    {% assign comp_icons = "microchip,network-wired,laptop-medical,database,server,memory,gears,code-branch,diagram-project,sitemap,cube,cubes,cubes-stacked,laptop-code,code,terminal,bug,wifi,tower-broadcast,satellite-dish,robot,satellite,plug,plug-circle-bolt,plug-circle-check,bolt,bolt-lightning,power-off,battery-full,battery-three-quarters,car-battery,gear,wrench,screwdriver-wrench,desktop,mobile-screen-button,tablet-screen-button,tv,keyboard,mouse,stopwatch,clock,hourglass,hourglass-half,chart-pie,chart-bar,chart-line,chart-simple,wave-square,podcast,signal,tower-cell,globe,earth-americas" | split: "," %}
    {% for icon in comp_icons %}
    <div class="col-6 col-sm-4 col-md-3 col-lg-2">
      <div class="icon-box"><i class="fa-solid fa-{{ icon }}"></i><h4>{{ icon }}</h4></div>
    </div>
    {% endfor %}
  </div>

  <h2 class="mt-5 mb-4 border-bottom pb-2">2. Medicine, Neuro, Biology & Genetics</h2>
  <div class="row g-3">
    {% assign med_icons = "brain,lungs,heart-pulse,heart,shield-heart,x-ray,dna,disease,viruses,bacterium,vial,vial-virus,vials,flask,flask-vial,microscope,prescription-bottle,prescription-bottle-medical,pills,capsules,stethoscope,syringe,hospital,user-doctor,user-nurse,hospital-user,bed-pulse,tooth,bone,droplet,pump-medical,truck-medical,staff-snake,briefcase-medical,star-of-life,crutch,radiation,biohazard,virus-covid,virus-covid-slash,head-side-virus,head-side-mask,head-side-cough,eye,eye-low-vision" | split: "," %}
    {% for icon in med_icons %}
    <div class="col-6 col-sm-4 col-md-3 col-lg-2">
      <div class="icon-box"><i class="fa-solid fa-{{ icon }}"></i><h4>{{ icon }}</h4></div>
    </div>
    {% endfor %}
  </div>

  <h2 class="mt-5 mb-4 border-bottom pb-2">3. Physics, Motion, Geometry & Abstract</h2>
  <div class="row g-3">
    {% assign phys_icons = "wind,tornado,water,fire,snowflake,temperature-half,temperature-high,temperature-low,meteor,cloud,sun,moon,planet-ringed,atom,magnet,burst,camera,video,film,magnifying-glass,magnifying-glass-chart,compress,expand,arrows-to-circle,arrows-to-dot,arrows-spin,rotate,rotate-right,retweet,shuffle,person-running,person-walking,person-biking,person-swimming,infinity,layer-group,object-group,object-ungroup,draw-polygon,vector-square,crosshairs,location-crosshairs,bullseye,compass,filter,circle-nodes,share-nodes,timeline,route,bezier-curve" | split: "," %}
    {% for icon in phys_icons %}
    <div class="col-6 col-sm-4 col-md-3 col-lg-2">
      <div class="icon-box"><i class="fa-solid fa-{{ icon }}"></i><h4>{{ icon }}</h4></div>
    </div>
    {% endfor %}
  </div>

  <h2 class="mt-5 mb-4 border-bottom pb-2">4. Motion & Robustness Options</h2>
  <div class="row g-3">
    {% assign motion_icons = "shield-heart,shield,anchor,heart-pulse,wave-square,water,person-running,camera-rotate,arrows-spin,heart-circle-check,scale-balanced,user-shield,ban,circle-stop,lungs,wind,hurricane,shield-halved,hand-holding-heart,anchor-circle-check,circle-notch,compass,dharmachakra,fan,fire-burner,life-ring" | split: "," %}
    {% for icon in motion_icons %}
    <div class="col-6 col-sm-4 col-md-3 col-lg-2">
      <div class="icon-box"><i class="fa-solid fa-{{ icon }}"></i><h4>{{ icon }}</h4></div>
    </div>
    {% endfor %}
  </div>
</div>
