# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dsearch',
    version='0.1.0',
    description='A hasher for preparing high-dimensional vectors for search',
    long_description=readme,
    author='Roger Donaldson',
    author_email='roger.d.donaldson@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'numpy==1.9.2',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

