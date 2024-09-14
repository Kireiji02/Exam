from setuptools import find_packages
from setuptools import setup

setup(
    name='god_turtle',
    version='0.0.0',
    packages=find_packages(
        include=('god_turtle', 'god_turtle.*')),
)
