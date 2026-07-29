---
layout: home
title: Home
--- 

<section class="home-hero">
  <div class="portrait-frame">
    <img src="/assets/profile.jpg" class="profile-photo" alt="Portrait of Huanyu Yin">
  </div>

  <div class="hero-content">
    <p class="hero-kicker">Operations Management · Shenzhen</p>
    <h1 class="hero-name">Huanyu Yin <span>印环宇</span></h1>
    <p class="hero-role">Assistant Professor, School of Economics, Shenzhen University</p>
    <p class="hero-role-cn">深圳大学经济学院助理教授</p>

    <div class="hero-actions">
      <a class="button button-primary" href="/research/">View Research</a>
      <a class="button button-secondary" href="/assets/cv.pdf">Download CV</a>
    </div>

    <a class="hero-email" href="mailto:huanyu.operationr@gmail.com">huanyu.operationr@gmail.com</a>
  </div>
</section>

<div class="home-overview">
  <section class="home-panel about-panel">
    <p class="section-label">Profile</p>
    <h2>About</h2>
    <p>I am an Assistant Professor at the School of Economics, Shenzhen University. I received my Ph.D. in Operations Management from The Chinese University of Hong Kong under the supervision of Prof. Xiting Gong (龔錫挺), and my B.Sc. in Mathematics from Nanjing University.</p>
    <p>My research focuses on inventory and supply chain management, especially the design of simple heuristic policies and their asymptotic analysis.</p>
  </section>

  <section class="home-panel areas-panel">
    <p class="section-label">Focus</p>
    <h2>Research Areas</h2>
    <ul class="research-areas">
      <li>Inventory Management</li>
      <li>Supply Chain Management</li>
      <li>Asymptotic Analysis</li>
      <li>Simple Heuristic Policies</li>
    </ul>
  </section>
</div>

<section class="featured-section">
  <div class="section-heading">
    <div>
      <p class="section-label">Selected Work</p>
      <h2>Research Highlights</h2>
    </div>
    <a class="section-link" href="/research/">View all research <span aria-hidden="true">→</span></a>
  </div>

  <div class="featured-grid">
    {% for pub in site.data.publications %}
      {% if pub.featured %}
      <article class="publication-card">
        <p class="publication-venue">{{ pub.journal }}</p>
        <h3>
          {% if pub.url %}
          <a href="{{ pub.url }}">{{ pub.title }}</a>
          {% else %}
          {{ pub.title }}
          {% endif %}
        </h3>
        <p class="publication-authors">{{ pub.authors }}</p>
      </article>
      {% endif %}
    {% endfor %}
  </div>
</section>
