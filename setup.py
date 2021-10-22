import pathlib
import setuptools
from pkg_resources import parse_requirements

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in parse_requirements(requirements_txt)
    ]

setuptools.setup(
    install_requires=install_requires,
)