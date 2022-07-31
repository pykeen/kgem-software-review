# Awesome Knowledge Graph Embedding Model Software [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This list contains awesome code for knowledge graph embedding models (KGEMs).
It doesn't contain single model research repositories nor more general graph
machine learning packages like PyTorch-Geometric.

## Contents

{% for entry in kgem_software_data %}
{{ loop.index }}. [{{ entry.name }}](#{{ entry.name.lower().replace(" ", "-") }})
{% endfor %}

{% for entry in kgem_software_data %}
## {{ entry.name }}

[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github.replace("-", "") }}-black?logo=github)](https://github.com/{{ entry.github }}) {% if entry.homepage %}[![Docs](https://img.shields.io/badge/Homepage-black?logo=HomeAdvisor)]({{ entry.homepage }}){% endif %} {% if entry.docs  %}[![Docs](https://img.shields.io/badge/Docs-black?logo=gitbook)]({{ entry.docs }}){% endif %}


{{ entry.description }}

{% if entry.citation %}
{% if entry.citation.url %}
> [{{ entry.citation.title }}]({{ entry.citation.url }})
{% else %}
> **Warning**
> <strong>This manuscript is not yet publicly available</strong>
> <br />{{ entry.citation.title }}
{% endif %}
> <br />{{ entry.citation.authors }}
> <br />*{{ entry.citation.venue }}*, {{ entry.citation.year }}
{% endif %}

{% if entry.pypi %}
Install with:

```shell
$ pip install {{ entry.pypi }}
```

{% else %}

{{ entry.name }} can't currently be installed directly from PyPI *via* `pip`. See its [installation docs]({{ entry.installation }}) instead.

{% endif %}
{% endfor %}

## Footnotes

The full list can be downloaded in YAML
[here](https://raw.githubusercontent.com/pykeen/kgem-software-review/main/_data/software.yml).
