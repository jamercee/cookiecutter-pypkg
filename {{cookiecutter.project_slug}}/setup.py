#!/usr/bin/env python
# vim: set fileencoding=utf-8
r"""{{cookiecutter.project_name}} distutils

{{ cookiecutter.copyright}}"""
from setuptools import setup, find_packages

import os
import sys
sys.path.insert(0, os.path.abspath('src'))
import {{cookiecutter.project_slug}}

try:
    # http://bugs.python.org/issue15881#msg170215
    # pylint: disable=W0611
    import multiprocessing
except ImportError:
    pass

long_description = []
try:
    with open('docs/index.rst') as fin:
        for line in fin:
            if line.startswith('Indicies and tables'):
                break
            long_description.append(line)
except IOError:
    pass

setup(
    # Project meta-data

    name = '{{cookiecutter.project_slug}}',
    version = {{cookiecutter.release}},
    packages = ['{{cookiecutter.project_slug}}'],
    package_dir = {'': 'src'},
    zip_safe = False,

    # Testing (assumes you have nose installed)

    test_suite      = 'nose.collector',
    setup_requires  = ['nose>=1.0'],

    # Project details

    description = ('{{cookiecutter.project_short_decription}}'),
    long_description = ''.join(long_description),
    author = '{{cookiecutter.author}}',
    author_email = '{{cookiecutter.email}}',
    #url = 'http://',
    #download_url = 'http://',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        ],
    license = '',
    )
