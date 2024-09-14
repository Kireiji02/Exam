from setuptools import find_packages
from setuptools import setup

setup(
    name='teleop_turtle',
    version='0.0.0',
    packages=find_packages(
        include=('teleop_turtle', 'teleop_turtle.*')),
)
