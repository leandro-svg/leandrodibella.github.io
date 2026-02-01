---
layout: single
title: "Leandro Di Bella"
permalink: /
author_profile: true
classes: wide home
excerpt: "Computer vision & generative AI for autonomous perception (detection, tracking, VLMs) in driving & drones."
redirect_from:
  - /about/
---

<div class="bento-grid">
  <section class="bento-card bento-hero">
    <div class="bento-kicker">3rd-year PhD student · ETRO, Vrije Universiteit Brussel (VUB)</div>
    <h1 class="bento-title">Autonomous perception</h1>
    <p class="bento-subtitle">Computer vision &amp; generative AI for driving &amp; drones.</p>

    <div class="bento-hero__split" aria-label="Research interests">
      <div class="bento-hero__blurb">
        <p class="bento-muted" style="margin: 0">
          I work on deployable perception systems with strong temporal consistency and practical robustness.
        </p>
      </div>
      <ul class="bento-mini-list" aria-label="Focus areas">
        <li><strong>Multi-object tracking:</strong> stable 3D MOT for autonomy.</li>
        <li><strong>Vision-language:</strong> grounding &amp; reasoning for perception.</li>
        <li><strong>Forecasting:</strong> generative motion prediction in complex scenes.</li>
      </ul>
    </div>
    <div class="bento-actions">
      <a class="btn btn--primary" href="/cv/">CV</a>
      <a class="btn btn--inverse" href="/publications/">Publications</a>
      <a class="btn btn--inverse" href="/portfolio/">Projects</a>
    </div>
  </section>

  <aside class="bento-card bento-avatar">
    <a class="js-lightbox" href="{{ '/images/AD_DRONE.png' | relative_url }}" aria-label="Open drone image">
      <img class="bento-avatar__img" src="{{ '/images/AD_DRONE.png' | relative_url }}" alt="Autonomous drone" loading="lazy" />
    </a>
  </aside>

  <section class="bento-card bento-list">
    <div class="bento-card__header">
      <h2 class="bento-card__title">Featured publications</h2>
      <a class="bento-card__link" href="/publications/">All →</a>
    </div>
    <div class="bento-list__items">
      {% assign featured_slugs = '2025-hybridtrack,2025-refergpt,2024-deepkalpose,2025-chronofusion' | split: ',' %}
      {% for slug in featured_slugs %}
        {% for post in site.publications %}
          {% if post.url contains slug and post.published != false %}
            <a class="bento-list__row" href="{{ post.url | relative_url }}">
              {% if post.header.teaser %}
                <img class="bento-list__thumb" src="{{ '/images/' | append: post.header.teaser | relative_url }}" alt="" loading="lazy" />
              {% endif %}
              <span class="bento-list__title">{{ post.title }}</span>
              <span class="bento-list__meta">{{ post.venue }}</span>
            </a>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </div>
  </section>

  <section class="bento-card bento-work">
    <h2 class="bento-card__title">What I work on</h2>
    <div class="bento-tags">
      <span class="bento-tag">Autonomous perception</span>
      <span class="bento-tag">Multi-object tracking</span>
      <span class="bento-tag">Vision-language models</span>
      <span class="bento-tag">Generative forecasting</span>
      <span class="bento-tag">Autonomous driving</span>
      <span class="bento-tag">Autonomous drones</span>
      <span class="bento-tag">Sensor fusion</span>
    </div>
    <p class="bento-muted" style="margin-top: 0.7rem">
        Current focus: real-time robustness, temporal consistency, and reliable behavior under distribution shift.
    </p>
  </section>

  <section class="bento-card bento-project">
    <div class="bento-card__header">
      <h2 class="bento-card__title">Personal project</h2>
      <a class="bento-card__link" href="https://mappx.app">mappx.app →</a>
    </div>
    <h3 class="bento-project__title">Mappx</h3>
    <p class="bento-muted">Map-centric social travel app (1000+ users).</p>
    <div class="bento-tags" style="margin-top: 0.7rem">
      <span class="bento-tag">Flutter</span>
      <span class="bento-tag">FastAPI</span>
      <span class="bento-tag">PostgreSQL</span>
      <span class="bento-tag">Azure</span>
      <span class="bento-tag">Mapbox</span>
    </div>
  </section>

  <section class="bento-card bento-contact">
    <div class="bento-card__header">
      <h2 class="bento-card__title">Contact</h2>
      <a class="bento-card__link" href="mailto:leandro.dibella@gmail.com">Email →</a>
    </div>
    <p class="bento-muted">Open to full-time roles in Belgium’s research &amp; engineering ecosystem.</p>
    <div class="bento-actions" style="margin-top: 0.8rem">
      <a class="btn btn--primary" href="mailto:leandro.dibella@gmail.com">leandro.dibella@gmail.com</a>
      <a class="btn btn--inverse" href="https://github.com/leandro-svg">GitHub</a>
      <a class="btn btn--inverse" href="https://www.linkedin.com/in/leandro-di-bella-62381413b/">LinkedIn</a>
      <a class="btn btn--inverse" href="https://scholar.google.de/citations?user=f7IDHsgAAAAJ&hl=en">Scholar</a>
    </div>
  </section>
</div>
