#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: setup.py
Description: Setup script to build and distribute sparshik-kyc module.
"""
import re
import os.path
from io import open
from setuptools import find_packages, setup

# Change the PACKAGE_NAME only to change folder and different name
PACKAGE_NAME = "sparshik-kyc"
PACKAGE_PPRINT_NAME = "Sparshik KYC"

# a-b-c => a/b/c
package_folder_path = PACKAGE_NAME.replace('-', '/')
# a-b-c => a.b.c
namespace_name = PACKAGE_NAME.replace('-', '.')

# Version extraction inspired from 'requests'
with open(os.path.join(package_folder_path, 'version.py')
		  if os.path.exists(os.path.join(package_folder_path, 'version.py'))
		  else os.path.join(package_folder_path, '_version.py'), 'r') as fd:
	version = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
						fd.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError('Cannot find version information')

with open('README.md', encoding='utf-8') as f:
	readme = f.read()
with open('CHANGELOG.md', encoding='utf-8') as f:
	changelog = f.read()

setup(
	name=PACKAGE_NAME,
	version=version,
	packages=find_packages(),
	description="Python SDK for Sparshik KYC API",
	long_description=readme + '\n\n' + changelog,
	long_description_content_type="text/markdown",
	url="https://github.com/sparshik/kyc-sdk-python",
	license='MIT License',
	author='Sparshik Technologies',
	author_email='support@sparshik.com',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		'Topic :: Scientific/Engineering :: Image Recognition',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		"Operating System :: OS Independent",
	],
	include_package_data=True,
	install_requires=['requests'],
)
