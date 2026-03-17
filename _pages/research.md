---
layout: page
title: Research
permalink: /research/
---

# Publications

{% for pub in site.data.publications %}
**{{ pub.authors }}**  
*{{ pub.title }}*  
{{ pub.journal }}, {{ pub.year }}

{% if pub.links %}
{% for link in pub.links %}
[{{ link.name }}]({{ link.url }})
{% endfor %}
{% endif %}

---
{% endfor %}
