#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "pillow",
    "scipy",
    "numpy",
    "tensorflow-gpu",
    "keras",
    "h5py",
    "numba",
]

test_requirements = [
    "pytest",
]

setup(
    name='zoo_attack',
    version='0.1.0',
    description="ZOO-Attack",
    long_description=readme,
    url='https://github.com/mschrimpf/ZOO-Attack',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
