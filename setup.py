#!/usr/bin/env python

from setuptools import setup

setup(
    name='help_pronounce',
    version='1.0',
    description='',
    author='Dave Morrissey',
    author_email='20507948+mcyph@users.noreply.github.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
    packages = ['help_pronounce'],
)
