#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Werkzeug RFC 7xx
----------------

Additional abort() codes and exceptions for werkzeug according to RFC 7xx
"""
from setuptools import setup


name = 'werkzeug-rfc7xx'
version = '1.0.0'

setup(
    name=name,
    version=version,
    url='https://github.com/onjin/werkzeug-rfc7xx',
    license='MIT',
    author='Marek Wywiał',
    author_email='onjinx@gmail.com',
    description=(
        'Abort codes and exceptions for werkzeug according to RFC 7xx'
    ),
    long_description=__doc__,
    packages=['werkzeug_rfc7xx'],
    zip_safe=False,
    include_package_data=True,
    install_requires=['werkzeug'],
    extra_require=dict(
        tests=[
            'pytest', 'pytest-sugar'
        ]
    ),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
