#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""

import json

from setuptools import setup, find_packages

import versioneer
from setuptools.command.install import install
from setuptools.command.develop import develop
import sys
from pathlib import Path


class CustomDevelopCommand(develop):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        develop.run(self)
        python_path = Path(sys.executable).absolute().parent / "../etc/jupyter"
        python_path.mkdir(parents=True, exist_ok=True)
        print(f"Writing nbconvert config to {python_path / "jupyter_nbconvert_config.json"}")
        with open(python_path / "jupyter_nbconvert_config.json", "w+") as f:
        	try:
        		js = json.load(f)
        	except json.decoder.JSONDecodeError:
        		js = {}
        	executor_config = js.get('Executor', {})
        	existing = set(executor_config.get('preprocessors', []))
        	existing.add("nbconvert_utils.ExecuteWithPreamble")
        	existing.add("nbconvert_utils.ExecuteWithIPythonArgs")
        	js['Executor'] = executor_config
        	js['Executor']['preprocessors'] = list(existing)
        	json.dump(js, f)

class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        install.run(self)
        python_path = Path(sys.executable).absolute().parent / "../etc/jupyter"
        python_path.mkdir(parents=True, exist_ok=True)
        print(f"Writing nbconvert config to {python_path / "jupyter_nbconvert_config.json"}")
        with open(python_path / "jupyter_nbconvert_config.json", "w+") as f:
        	try:
        		js = json.load(f)
        	except json.decoder.JSONDecodeError:
        		js = {}
        	executor_config = js.get('Executor', {})
        	existing = set(executor_config.get('preprocessors', []))
        	existing.add("nbconvert_utils.ExecuteWithPreamble")
        	existing.add("nbconvert_utils.ExecuteWithIPythonArgs")
        	js['Executor'] = executor_config
        	js['Executor']['preprocessors'] = list(existing)
        	json.dump(js, f)

def get_cmd():
	d = versioneer.get_cmdclass()
	d['install'] = CustomInstallCommand
	d['develop'] = CustomDevelopCommand
	return d

setup(
    version=versioneer.get_version(),
    cmdclass=get_cmd(),
    name="nbconvert_utils",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["nbconvert"],
    python_requires=">3.6.0",
)
