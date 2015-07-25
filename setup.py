#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
import io

requirements = [
    "pyunpack",
    "requests",
    "pip"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='hallie',
    version='0.1.1',
    description="Like Siri, for the command line.. Forgot a command? Tell Hallie and she'll try to help. Inspired by betty.",
    author="Michael Melchione",
    author_email='michaelmelchione@gmail.com',
    url='https://github.com/mikemelch/hallie',
    packages=find_packages(exclude=["contrib", "docs", "tests*", "tasks"]),
    package_dir={'hallie':
                 'hallie'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='hallie',
    entry_points = {
        'console_scripts': [
            'hallie = hallie.hallie:main',
            'bar = other_module:some_func',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
