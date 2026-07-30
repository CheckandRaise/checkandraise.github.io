---
layout: default
title: Photography
permalink: /photography/
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
      <p class="photo-kicker">Frames from Elsewhere</p>
      <h1>Photography</h1>
      <p class="photo-intro">A visual notebook of coastlines, city light, and quiet moments encountered between places.</p>
      <div class="photo-hero-stats" aria-label="Collection summary">
        <span><strong>{{ album_count }}</strong> Places</span>
        <span><strong>{{ photo_count }}</strong> Frames</span>
        <span><strong>EXIF</strong> Preserved</span>
      </div>
    </div>
    <span class="photo-viewfinder photo-viewfinder-top" aria-hidden="true"></span>
    <span class="photo-viewfinder photo-viewfinder-bottom" aria-hidden="true"></span>
  </header>

  <nav class="photo-location-nav" aria-label="Photography locations">
    {% for album in site.data.photography %}
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
        <strong>{{ album.title }}</strong>
        <span>{{ album.photos | size }} frames</span>
      </span>
    </a>
    {% endfor %}
  </nav>

  {% for album in site.data.photography %}
  <section class="photo-album" id="{{ album.slug }}">
    <header class="photo-album-heading">
      <span class="photo-album-number" aria-hidden="true">0{{ forloop.index }}</span>
      <div>
        <p class="photo-kicker">{{ album.eyebrow }}</p>
        <h2>{{ album.title }}</h2>
      </div>
      <p>{{ album.description }}</p>
    </header>

    <div class="photo-wall{% if album.photos.size == 2 %} photo-wall-short{% endif %}">
      {% for photo in album.photos %}
      <figure class="photo-card photo-card-{{ photo.orientation }}">
        <button
          class="photo-open"
          type="button"
          aria-label="View {{ photo.caption | escape }} larger"
          data-full="{{ photo.src }}"
          data-alt="{{ photo.alt | escape }}"
          data-caption="{{ photo.caption | escape }}"
          data-location="{{ photo.sublocation | escape }}"
          data-date="{{ photo.date | escape }}"
          data-camera="{{ photo.camera | escape }}"
          data-lens="{{ photo.lens | escape }}"
          data-focal="{{ photo.focal_length | escape }}"
          data-aperture="{{ photo.aperture | escape }}"
          data-shutter="{{ photo.shutter | escape }}"
          data-iso="{{ photo.iso | escape }}"
        >
          <img
            src="{{ photo.thumb }}"
            alt="{{ photo.alt | escape }}"
            width="{{ photo.thumb_width }}"
            height="{{ photo.thumb_height }}"
            loading="lazy"
          >
          <span class="photo-enlarge" aria-hidden="true">View</span>
        </button>

        <figcaption>
          <div class="photo-caption-heading">
            <div>
              <p>{{ photo.sublocation }}</p>
              <h3>{{ photo.caption }}</h3>
            </div>
            <time>{{ photo.date }}</time>
          </div>

          <div class="photo-gear">
            <span>{{ photo.camera }}</span>
            <span>{{ photo.lens }}</span>
          </div>

          <ul class="photo-settings" aria-label="Exposure settings">
            <li><small>Focal</small><strong>{{ photo.focal_length }}</strong></li>
            <li><small>Aperture</small><strong>{{ photo.aperture }}</strong></li>
            <li><small>Shutter</small><strong>{{ photo.shutter }}</strong></li>
            <li><small>Sensitivity</small><strong>{{ photo.iso }}</strong></li>
          </ul>
        </figcaption>
      </figure>
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <p class="photo-privacy-note">Camera and exposure information is retained from the original files. Published images omit embedded GPS metadata.</p>
</div>

<dialog class="photo-lightbox" id="photo-lightbox" aria-label="Photography viewer">
  <div class="photo-lightbox-shell">
    <div class="photo-lightbox-stage">
      <img class="photo-lightbox-image" alt="">
      <button class="photo-lightbox-nav photo-lightbox-prev" type="button" aria-label="Previous photograph">‹</button>
      <button class="photo-lightbox-nav photo-lightbox-next" type="button" aria-label="Next photograph">›</button>
    </div>

    <aside class="photo-lightbox-details">
      <button class="photo-lightbox-close" type="button" aria-label="Close viewer">×</button>
      <p class="photo-kicker photo-lightbox-location"></p>
      <h2 class="photo-lightbox-caption"></h2>
      <p class="photo-lightbox-date"></p>
      <dl>
        <div><dt>Camera</dt><dd class="photo-lightbox-camera"></dd></div>
        <div><dt>Lens</dt><dd class="photo-lightbox-lens"></dd></div>
        <div><dt>Focal Length</dt><dd class="photo-lightbox-focal"></dd></div>
        <div><dt>Aperture</dt><dd class="photo-lightbox-aperture"></dd></div>
        <div><dt>Shutter</dt><dd class="photo-lightbox-shutter"></dd></div>
        <div><dt>ISO</dt><dd class="photo-lightbox-iso"></dd></div>
      </dl>
      <p class="photo-lightbox-count" aria-live="polite"></p>
    </aside>
  </div>
</dialog>

<script src="/assets/photography-gallery.js" defer></script>
