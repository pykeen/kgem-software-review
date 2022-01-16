"""Generate the README.md file."""

from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

HERE = Path(__file__).parent.resolve()
DATA = HERE.joinpath("_data", "software.yml")
PATH = HERE.joinpath("README.md")

environment = Environment(autoescape=True, loader=FileSystemLoader(HERE / "templates"), trim_blocks=True)

template = environment.get_template("README.md")


def main():
    data = yaml.safe_load(DATA.read_text())
    PATH.write_text(template.render(data=data))


if __name__ == '__main__':
    main()
