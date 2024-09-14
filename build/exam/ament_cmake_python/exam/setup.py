from setuptools import find_packages
from setuptools import setup

setup(
    name='exam',
    version='0.0.0',
    packages=find_packages(
        include=('exam', 'exam.*')),
)
