---
layout: home
---
This page contains a list of software packages for knowledge graph embedding models (KGEMs). It's generated with GitHub
Pages from <a href="https://github.com/pykeen/kgem-software-review"><img alt="GitHub logo"
src="img/github-icon.svg" width="16" height="16" /> pykeen/kgem-software-review</a>. Content on this site
is available under the [CC0 1.0 Universal](https://github.com/pykeen/kgem-software-review/blob/main/LICENSE)
license. Download the full data
[here](https://raw.githubusercontent.com/pykeen/kgem-software-review/main/_data/software.yml).

## Contributing

You can contribute to this list in one of the following ways:

1. [Fill out an issue](https://github.com/pykeen/kgem-software-review/issues/new?assignees=cthoyt&labels=enhancement&template=new-software-package.md&title=) on the GitHub issue tracker.
2. [Make an edit](https://github.com/pykeen/kgem-software-review/edit/main/_data/software.yml) through the web-based GitHub editor which automatically forks the repository and generates a pull request.
3. [Fork the repository](https://github.com/pykeen/kgem-software-review/) from GitHub and send a pull request.

## The List

{% for entry in site.data.software %}
<strong><a href="{% if entry.homepage %}{{ entry.homepage }}{% else %}https://github.com/{{ entry.github }}{% endif %}">{{ entry.name }}</a></strong>

[![GitHub](https://img.shields.io/badge/GitHub-{{ entry.github | replace: "-", ""}}-black?logo=github)](https://github.com/{{ entry.github }})
{% if entry contains "docs" %}[![Docs](https://img.shields.io/badge/Docs-available-green?logo=gitbook)]({{ entry.docs }}){% else %}[![Docs](https://img.shields.io/badge/Docs-missing-red?logo=gitbook)](){% endif %}
{% if entry contains "ci" %}[![CI](https://img.shields.io/badge/CI-{{ entry.ci.type }}-green?logo={{ entry.ci.type }})]({{ entry.ci.link }}){% else %}[![CI](https://img.shields.io/badge/CI-missing-red)](){% endif %}
{% if entry contains "pypi" %}[![PyPI - License](https://img.shields.io/pypi/l/{{ entry.pypi }})](https://pypi.org/project/{{ entry.pypi }})
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ entry.pypi }})](https://pypi.org/project/{{ entry.pypi }})
[![PyPI - Software Version](https://img.shields.io/pypi/v/{{ entry.pypi }})](https://pypi.org/project/{{ entry.pypi }})

```shell
$ # {{ entry.name }} can be installed directly with:
$ pip install {{ entry.pypi }}
```
{% else %}
Can't install {{ entry.name }} directly from PyPI with `pip`. See their [installation docs]({{ entry.installation }}) instead.
{% endif %}

{% endfor %}
