#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Packing metadata for setuptools."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'appdirs',
    'Click',
    'click-aliases == 0.1',
    # Click color support.
    # http://click.pocoo.org/5/utils/#ansi-colors
    'colorama',
    'configparser >= 3.5.0b2',
    'future',
    'hamster-lib',
    'pyparsing',
    # py27 compatibility related
    'six',
    'tabulate',
]

requirements_links=[
    'https://github.com/hotoffthehamster/click-aliases/tarball/master#egg=click-aliases-0.1',
]

setup(
    name='hamster_cli',
    version='0.12.0',
    description="A basic CLI for the hamster time tracker.",
    long_description=readme + '\n\n' + history,
    author="Eric Goller",
    author_email='Elbenfreund@DenkenInEchtzeit.net',
    url='https://github.com/elbenfreund/hamster_cli',
    packages=[
        'hamster_cli',
    ],
    package_dir={'hamster_cli':
                 'hamster_cli'},
    install_requires=requirements,
    dependency_links=requirements_links,
    license="GPL3",
    zip_safe=False,
    keywords='hamster_cli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points='''
    [console_scripts]
    hamster=hamster_cli.hamster_cli:run
    '''.strip()
)

