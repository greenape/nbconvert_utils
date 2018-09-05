#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""

try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup


setup(
    name="pandas_to_markdown",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "pandas",
        "tabulate",
        "nbconvert"
    ],
)
