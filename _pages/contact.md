---
layout: page
title: Contact Us
permalink: /contact/
description: Get in touch with the AI2MR Lab.
nav: true
nav_order: 5
---

<div class="contact-container mt-4">
  <div class="row">
    <!-- Contact Info Section -->
    <div class="col-md-5 mb-4 mb-md-0">
      <div class="contact-info-card p-4 h-100 glass-box">
        <h3 class="mb-4" style="color: var(--global-theme-color);">Reach Out</h3>
        <p class="text-muted mb-4">
          We are always looking for passionate scientists and engineers to join our team. If you are interested in working at the intersection of AI and MRI, don't hesitate to reach out!
        </p>

        <ul class="list-unstyled mb-0">
          <li class="mb-3 d-flex align-items-center">
            <i class="fa-solid fa-envelope fa-fw mr-3" style="color: var(--global-theme-color); font-size: 1.2rem;"></i>
            <span><a href="mailto:{{ site.email }}">{{ site.email | default: "you@example.com" }}</a></span>
          </li>
          <li class="mb-3 d-flex align-items-center">
            <i class="fa-solid fa-location-dot fa-fw mr-3" style="color: var(--global-theme-color); font-size: 1.2rem;"></i>
            <span>AI2MR Research Lab<br>123 Medical Research Blvd<br>City, State 12345</span>
          </li>
        </ul>

        <div class="mt-4 pt-3 border-top">
          <h5 class="mb-3" style="font-size: 1rem;">Connect with us</h5>
          <div class="social-links contact-socials">
            {% social_links %}
          </div>
        </div>
      </div>
    </div>

    <!-- Contact Form Section -->
    <div class="col-md-7">
      <div class="contact-form-card p-4 glass-box">
        <form action="https://formspree.io/f/placeholder" method="POST" id="contact-form">
          <div class="form-row">
            <div class="form-group col-md-6 mb-3">
              <label for="firstName" class="form-label" style="font-weight: 500;">First Name</label>
              <input type="text" class="form-control" id="firstName" name="firstName" placeholder="John" required style="border-radius: 8px; border: 1px solid var(--global-divider-color); background-color: var(--global-bg-color); color: var(--global-text-color);">
            </div>
            <div class="form-group col-md-6 mb-3">
              <label for="lastName" class="form-label" style="font-weight: 500;">Last Name</label>
              <input type="text" class="form-control" id="lastName" name="lastName" placeholder="Doe" required style="border-radius: 8px; border: 1px solid var(--global-divider-color); background-color: var(--global-bg-color); color: var(--global-text-color);">
            </div>
          </div>
          
          <div class="form-group mb-3">
            <label for="email" class="form-label" style="font-weight: 500;">Email Address</label>
            <input type="email" class="form-control" id="email" name="_replyto" placeholder="john.doe@example.com" required style="border-radius: 8px; border: 1px solid var(--global-divider-color); background-color: var(--global-bg-color); color: var(--global-text-color);">
          </div>
          
          <div class="form-group mb-3">
            <label for="subject" class="form-label" style="font-weight: 500;">Subject</label>
            <select class="form-control custom-select" id="subject" name="subject" required style="border-radius: 8px; border: 1px solid var(--global-divider-color); background-color: var(--global-bg-color); color: var(--global-text-color);">
              <option value="" disabled selected>Select an option...</option>
              <option value="Joining the Lab">Joining the Lab</option>
              <option value="Collaboration">Collaboration Inquiry</option>
              <option value="General Question">General Question</option>
            </select>
          </div>
          
          <div class="form-group mb-4">
            <label for="message" class="form-label" style="font-weight: 500;">Message</label>
            <textarea class="form-control" id="message" name="message" rows="5" placeholder="Tell us how we can help you..." required style="border-radius: 8px; border: 1px solid var(--global-divider-color); background-color: var(--global-bg-color); color: var(--global-text-color); resize: vertical;"></textarea>
          </div>
          
          <button type="submit" class="btn btn-primary btn-block py-2 submit-btn" style="border-radius: 8px; transition: all 0.3s ease;">
            <i class="fa-solid fa-paper-plane mr-2"></i> Send Message
          </button>
        </form>
      </div>
    </div>
  </div>
</div>

<style>
.contact-form-card .form-control:focus {
  box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.25);
  border-color: var(--global-theme-color) !important;
}

[data-theme="dark"] .contact-form-card .form-control option {
  background-color: var(--global-bg-color);
  color: var(--global-text-color);
}

.submit-btn {
  background-color: var(--global-theme-color);
  border-color: var(--global-theme-color);
}

.submit-btn:hover {
  filter: brightness(1.1);
  transform: translateY(-1px);
}

.contact-socials a {
  font-size: 1.5rem;
  margin-right: 1rem;
  color: var(--global-text-color);
  transition: color 0.3s ease;
}

.contact-socials a:hover {
  color: var(--global-theme-color);
}
</style>
