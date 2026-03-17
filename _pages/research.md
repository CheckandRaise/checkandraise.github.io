---
layout: page
title: Research
permalink: /research/
---

# Publications

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
