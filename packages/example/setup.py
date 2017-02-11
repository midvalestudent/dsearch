# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='example',
    version='0.0.1',
    description='Example python project with settings, logging, and more',
    long_description=readme,
    author='Roger Donaldson',
    author_email='roger.d.donaldson@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'simple-settings',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

