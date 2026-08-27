---
layout: home
title: 首页
permalink: /zh/
lang: zh-CN
alternate_url: /
---

<section class="home-hero">
  <span class="math-watermark hero-math" aria-hidden="true">q<sub>t</sub> = (U − E[I<sub>t+L</sub> | y<sub>t</sub>])<sup>+</sup></span>

  <div class="portrait-frame">
    <picture>
      <source media="(prefers-reduced-motion: reduce)" srcset="/assets/huanyu_ocean_king_with_universities.png" type="image/png">
      <source srcset="/assets/huanyu_ocean_king_animated.webp" type="image/webp">
      <img src="/assets/huanyu_ocean_king_animated.gif" class="profile-photo" alt="印环宇的 Ocean King 动态卡通肖像" width="640" height="960" fetchpriority="high" decoding="async">
    </picture>
  </div>

  <div class="hero-content">
    <p class="hero-kicker">运营管理 · 深圳</p>
    <h1 class="hero-name">Huanyu Yin <span>印环宇</span></h1>
    <p class="hero-role">深圳大学经济学院助理教授</p>
    <p class="hero-role-cn hero-role-secondary">Assistant Professor, School of Economics, Shenzhen University</p>

    <div class="hero-actions">
      <a class="button button-primary" href="/zh/research/">查看研究</a>
      <a class="button button-secondary" href="/assets/cv_cn.pdf">下载中文 CV</a>
    </div>

    <a class="hero-email" href="mailto:huanyu.operationr@gmail.com">huanyu.operationr@gmail.com</a>
  </div>
</section>

<div class="home-overview">
  <section class="home-panel about-panel">
    <span class="math-watermark panel-math" aria-hidden="true">Var(I<sub>t+L</sub>) ≤ L Var(D)</span>
    <p class="section-label">个人简介</p>
    <h2>关于我</h2>
    <p>我现任深圳大学经济学院助理教授。我在 The Chinese University of Hong Kong 获得 Operations Management 博士学位，导师为 Prof. Xiting Gong (龔錫挺)；本科毕业于南京大学，获数学理学学士学位。</p>
    <p>我的研究聚焦库存与供应链管理，尤其关注简单启发式策略的设计及其渐近分析。</p>
  </section>

  <section class="home-panel areas-panel">
    <span class="math-watermark panel-math panel-math-wide" aria-hidden="true">IP<sup>n</sup><sub>t+1</sub> = IP<sup>n</sup><sub>t</sub> + q<sup>n</sup><sub>t+τₙ</sub> − D<sub>t</sub> + ℓ<sub>t</sub></span>
    <p class="section-label">研究方向</p>
    <h2>研究领域</h2>
    <ul class="research-areas">
      <li>库存管理</li>
      <li>供应链管理</li>
      <li>渐近分析</li>
      <li>简单启发式策略</li>
    </ul>
  </section>
</div>

<section class="featured-section">
  <span class="math-watermark featured-math" aria-hidden="true">lim<sub>p→∞</sub> C<sub>p</sub>(π*) / OPT<sub>p</sub> = 1</span>

  <div class="section-heading">
    <div>
      <p class="section-label">代表性工作</p>
      <h2>研究精选</h2>
    </div>
    <a class="section-link" href="/zh/research/">查看全部研究 <span aria-hidden="true">→</span></a>
  </div>

  <div class="featured-grid">
    {% for pub in site.data.publications %}
      {% if pub.featured %}
      <article class="publication-card publication-card-{{ pub.featured_theme }}">
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
