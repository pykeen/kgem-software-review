# Awesome Graph Machine Learning [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This list contains awesome code for graph machine learning, with a big
focus on knowledge graph embedding models (KGEMs).

## Contents

{% for entry in kgem_software_data %}
1. [{{ entry.name }}](#{{ entry.name.lower().replace(" ", "-") }})
{% endfor %}

{% for entry in kgem_software_data %}
## <a href="{% if entry.homepage %}{{ entry.homepage }}{% else %}https://github.com/{{ entry.github }}{% endif %}">{{ entry.name }}</a>

{% if entry.citation %}

> [{{ entry.citation.title }}]({{ entry.citation.url }})
> {{ entry.citation.author }} *et al.*, {{ entry.citation.year }}
{% endif %}

[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github.replace("-", "") }}-black?logo=github)](https://github.com/{{ entry.github }})
{% if entry.docs  %}
[![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)]({{ entry.docs }})
{% else %}
![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook)
{% endif %}
{% if entry.ci  %}
[![CI](https://img.shields.io/badge/CI-{{ entry.ci.type }}-green?logo={{ entry.ci.type }})]({{ entry.ci.link }})
{% else %}
![CI](https://img.shields.io/badge/CI-missing-red)
{% endif %}
{% if entry.pypi %}
![PyPI - License](https://img.shields.io/pypi/l/{{ entry.pypi }})
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ entry.pypi }})
![PyPI - Software Version](https://img.shields.io/pypi/v/{{ entry.pypi }})

```shell
$ # {{ entry.name }} can be installed directly with:
$ pip install {{ entry.pypi }}
```
{% else %}

Can't install {{ entry.name }} directly from PyPI with `pip`. See their [installation docs]({{ entry.installation }}) instead.

{% endif %}
{% endfor %}

## Footnotes

The full list can be downloaded in YAML
[here](https://raw.githubusercontent.com/pykeen/kgem-software-review/main/_data/software.yml).
