---
layout: default
title: 摄影
permalink: /zh/photography/
lang: zh-CN
alternate_url: /photography/
---

{% assign album_count = site.data.photography | size %}
{% assign hero_album = site.data.photography | first %}
{% assign photo_count = 0 %}
{% for album in site.data.photography %}
  {% assign album_size = album.photos | size %}
  {% assign photo_count = photo_count | plus: album_size %}
{% endfor %}

<div class="photo-page">
  <header class="photo-hero">
    <img
      class="photo-hero-image"
      src="{{ hero_album.cover_src }}"
      width="2000"
      height="1164"
      alt=""
      fetchpriority="high"
    >
    <div class="photo-hero-shade" aria-hidden="true"></div>
    <div class="photo-hero-content">
      <p class="photo-kicker">远方的片段</p>
      <h1>摄影</h1>
      <p class="photo-intro">一本关于海岸、城市光影，以及旅途中安静瞬间的视觉笔记。</p>
      <div class="photo-hero-stats" aria-label="摄影集概况">
        <span><strong>{{ album_count }}</strong> 个地点</span>
        <span><strong>{{ photo_count }}</strong> 张照片</span>
        <span><strong>EXIF</strong> 已保留</span>
      </div>
    </div>
    <span class="photo-viewfinder photo-viewfinder-top" aria-hidden="true"></span>
    <span class="photo-viewfinder photo-viewfinder-bottom" aria-hidden="true"></span>
  </header>

  <nav class="photo-location-nav" aria-label="摄影地点">
    {% for album in site.data.photography %}
    {% assign zh_album = site.data.photography_zh[album.slug] %}
    <a class="photo-location-card" href="#{{ album.slug }}">
      <img
        src="{{ album.cover_thumb }}"
        alt=""
        width="900"
        height="600"
        loading="lazy"
      >
      <span class="photo-location-copy">
        <small>0{{ forloop.index }}</small>
        <strong>{{ zh_album.title }}</strong>
        <span>{{ album.photos | size }} 张照片</span>
      </span>
    </a>
    {% endfor %}
  </nav>

  {% for album in site.data.photography %}
  {% assign zh_album = site.data.photography_zh[album.slug] %}
  <section class="photo-album" id="{{ album.slug }}">
    <header class="photo-album-heading">
      <span class="photo-album-number" aria-hidden="true">0{{ forloop.index }}</span>
      <div>
        <p class="photo-kicker">{{ zh_album.eyebrow }}</p>
        <h2>{{ zh_album.title }}</h2>
      </div>
      <p>{{ zh_album.description }}</p>
    </header>

    <div class="photo-wall{% if album.photos.size == 2 %} photo-wall-short{% endif %}">
      {% for photo in album.photos %}
      {% assign zh_photo = zh_album.photos[photo.id] %}
      <figure class="photo-card photo-card-{{ photo.orientation }}">
        <button
          class="photo-open"
          type="button"
          aria-label="放大查看：{{ zh_photo.caption | escape }}"
          data-full="{{ photo.src }}"
          data-alt="{{ zh_photo.alt | escape }}"
          data-caption="{{ zh_photo.caption | escape }}"
          data-location="{{ zh_photo.sublocation | escape }}"
          data-date="{{ zh_photo.date | escape }}"
          data-camera="{{ photo.camera | escape }}"
          data-lens="{{ photo.lens | escape }}"
          data-focal="{{ photo.focal_length | escape }}"
          data-aperture="{{ photo.aperture | escape }}"
          data-shutter="{{ photo.shutter | escape }}"
          data-iso="{{ photo.iso | escape }}"
        >
          <img
            src="{{ photo.thumb }}"
            alt="{{ zh_photo.alt | escape }}"
            width="{{ photo.thumb_width }}"
            height="{{ photo.thumb_height }}"
            loading="lazy"
          >
          <span class="photo-enlarge" aria-hidden="true">查看</span>
        </button>

        <figcaption>
          <div class="photo-caption-heading">
            <div>
              <p>{{ zh_photo.sublocation }}</p>
              <h3>{{ zh_photo.caption }}</h3>
            </div>
            <time>{{ zh_photo.date }}</time>
          </div>

          <div class="photo-gear">
            <span>{{ photo.camera }}</span>
            <span>{{ photo.lens }}</span>
          </div>

          <ul class="photo-settings" aria-label="拍摄参数">
            <li><small>焦距</small><strong>{{ photo.focal_length }}</strong></li>
            <li><small>光圈</small><strong>{{ photo.aperture }}</strong></li>
            <li><small>快门</small><strong>{{ photo.shutter }}</strong></li>
            <li><small>感光度</small><strong>{{ photo.iso }}</strong></li>
          </ul>
        </figcaption>
      </figure>
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <p class="photo-privacy-note">相机与曝光参数来自原始文件；网站发布版本已移除内嵌 GPS 信息。</p>
</div>

<dialog class="photo-lightbox" id="photo-lightbox" aria-label="摄影作品查看器">
  <div class="photo-lightbox-shell">
    <div class="photo-lightbox-stage">
      <img class="photo-lightbox-image" alt="">
      <button class="photo-lightbox-nav photo-lightbox-prev" type="button" aria-label="上一张照片">‹</button>
      <button class="photo-lightbox-nav photo-lightbox-next" type="button" aria-label="下一张照片">›</button>
    </div>

    <aside class="photo-lightbox-details">
      <button class="photo-lightbox-close" type="button" aria-label="关闭查看器">×</button>
      <p class="photo-kicker photo-lightbox-location"></p>
      <h2 class="photo-lightbox-caption"></h2>
      <p class="photo-lightbox-date"></p>
      <dl>
        <div><dt>相机</dt><dd class="photo-lightbox-camera"></dd></div>
        <div><dt>镜头</dt><dd class="photo-lightbox-lens"></dd></div>
        <div><dt>焦距</dt><dd class="photo-lightbox-focal"></dd></div>
        <div><dt>光圈</dt><dd class="photo-lightbox-aperture"></dd></div>
        <div><dt>快门</dt><dd class="photo-lightbox-shutter"></dd></div>
        <div><dt>ISO</dt><dd class="photo-lightbox-iso"></dd></div>
      </dl>
      <p class="photo-lightbox-count" aria-live="polite"></p>
    </aside>
  </div>
</dialog>

<script src="/assets/photography-gallery.js" defer></script>
