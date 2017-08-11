#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup

basedir = path.dirname(path.abspath(__file__))
with open(path.join(basedir, 'README.rst')) as readme_file:
    readme = readme_file.read()


requirements = [
    'wdom',
    'm2r',
    'docutils',
    'pygments',
]

setup(
    name='m2rdemo',
    version='0.1.0',
    description="M2R Demo with WDOM",
    long_description=readme,

    author="Hiroyuki Takagi",
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/m2rdemo',

    packages=[
        'm2rdemo',
    ],
    package_dir={'m2rdemo':
                 'm2rdemo'},
    include_package_data=True,
    install_requires=requirements,

    license="MIT license",
    zip_safe=False,
    keywords='m2rdemo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
