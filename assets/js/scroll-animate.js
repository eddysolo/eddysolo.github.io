// Scroll-triggered fade-in animations using Intersection Observer
// Applied to cards, section headers, and publication entries

document.addEventListener("DOMContentLoaded", function () {
  const animatedEls = document.querySelectorAll(
    ".card, .section-heading, .publication-entry, .post-header h1, .hero-banner, article > p:first-of-type, .profile-grid-item"
  );

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("fade-in-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  animatedEls.forEach((el) => {
    el.classList.add("fade-in-hidden");
    observer.observe(el);
  });
});
