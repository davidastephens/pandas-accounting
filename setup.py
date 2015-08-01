#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import parse
import os
from setuptools import setup


NAME = 'pandas-accounting'


def version():
    """Return version string."""
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'pandas_accounting',
                           '__init__.py')) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return parse(line).body[0].value.s


def readme():
    with open('README.md') as f:
        return f.read()

INSTALL_REQUIRES = (
    ['pandas']
)

setup(
    name=NAME,
    version=version(),
    description="Library for modelling financial statements using Pandas",
    long_description=readme(),
    license='MIT License',
    author='David Stephens',
    author_email='david@davidstephens.io',
    url='https://github.com/davidastephens/pandas-accounting',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
    ],
    keywords=['data','accounting','financial'],
    install_requires=INSTALL_REQUIRES,
    packages=['pandas_accounting'],
    test_suite='tests',
    zip_safe=False,
)
