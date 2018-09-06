#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""

try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup


import versioneer

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name="nbconvert_utils",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["nbconvert"],
    python_requires=">3.6.0",
)
