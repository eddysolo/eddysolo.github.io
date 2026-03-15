---
layout: page
title: projects
permalink: /projects/
description: A growing collection of your cool projects.
nav: false
nav_order: 3
display_categories: [work, fun]
horizontal: false
---

{% assign sorted_projects = site.projects | sort: 'importance' %}
{% assign featured_project = sorted_projects | first %}

<div class="projects">
  <div class="row row-cols-1 row-cols-md-2">
    {% if featured_project %}
      {% assign project = featured_project %}
      {% include projects.liquid %}
    {% endif %}

    <div class="col">
      <div class="card h-100 hoverable glass-box">
        <div class="card-body d-flex flex-column">
          <h2 class="card-title">Future Project Slot</h2>
          <p class="card-text mb-2">This space is intentionally reserved for your next project.</p>
          <p class="card-text" style="opacity: 0.8;">Use this box later for title, short description, and relevant links once the new project is ready.</p>
          <span class="btn btn-outline-primary disabled mt-auto" aria-disabled="true">Coming Soon</span>
        </div>
      </div>
    </div>
  </div>
</div>
