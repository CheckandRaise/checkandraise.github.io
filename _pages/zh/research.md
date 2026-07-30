---
layout: page
title: 研究
permalink: /zh/research/
lang: zh-CN
alternate_url: /research/
---

<div class="academic-page research-page" markdown="1">
<span class="math-watermark page-math page-math-top" aria-hidden="true">OPT<sup>φ</sup> = inf<sub>π∈Πφ</sub> C<sup>φ,π</sup></span>
<span class="math-watermark page-math research-math-middle" aria-hidden="true">U<sub>n</sub>(β) = F<sup>−1</sup><sub>τ̂ₙ+1</sub>(β) − τ̂<sub>n</sub>μ</span>

# 学术论文

{% for pub in site.data.publications %}

<p>

<strong>{{ pub.authors }}</strong><br>

{% if pub.url %}
<em><a href="{{ pub.url }}">{{ pub.title }}</a></em><br>
{% else %}
<em>{{ pub.title }}</em><br>
{% endif %}

{{ pub.journal }}, {{ pub.year }}

</p>

<hr>

{% endfor %}

</div>
