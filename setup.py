#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements(os.path.join(os.path.dirname(__file__), "requirements", "base.txt"))


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name = "pyGE",
    version = "0.0.3",
    description = "Small wrapper around some Geekevents API endpoints",
    author = "Kristoffer Dalby",
    author_email = "kradalby@kradalby.no",
    url = "https://github.com/kradalby/pyGE",
    keywords = ["geekevents"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description='\n\n'.join([read('README.md')]),
    test_suite = 'tests',
    install_requires=install_reqs,
    py_modules=['pyGE'],
)
