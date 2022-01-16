"""Generate the README.md file."""

from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

HERE = Path(__file__).parent.resolve()
KGEM_SOFTWARE_PATH = HERE.joinpath("_data", "software.yml")
PATH = HERE.joinpath("README.md")

environment = Environment(autoescape=True, loader=FileSystemLoader(HERE / "templates"), trim_blocks=True)

template = environment.get_template("README.md")


def main():
    kgem_software_data = yaml.safe_load(KGEM_SOFTWARE_PATH.read_text())
    PATH.write_text(template.render(kgem_software_data=kgem_software_data) + "\n")


if __name__ == '__main__':
    main()
