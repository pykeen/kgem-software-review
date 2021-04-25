---
layout: home
---
This page contains a list of software packages for knowledge graph embedding models (KGEM). You can contribute to this
list by [adding a benchmark](https://github.com/pykeen/kgem-software-review/edit/main/_data/software.yml) or through the
GitHub editor or by forking the repository and sending a pull request. Content on this site is available under
the [CC0 1.0 Universal](https://github.com/pykeen/kgem-software-review/blob/main/LICENSE) license.

{% for entry in site.data.software %}
<strong><a href="{{ entry.homepage }}">{{ entry.name }}</a></strong>
{% if entry contains "github" %}[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }}){% endif %}
{% endfor %}
