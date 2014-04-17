# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wordcensor',
    packages = find_packages(),
    version='0.1',
    description='Django word censoring application',
    long_description=README,
    license='MIT License',
    author="Oliver Gutiérrez",
    author_email="ogutsua@gmail.com",
    url = 'https://github.com/R3v1L/django-wordcensor',
    keywords = ['django', 'censor', ],
    classifiers = [],
    # download_url = '',
)