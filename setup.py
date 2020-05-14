# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ticket_management/__init__.py
from ticket_management import __version__ as version

setup(
	name='ticket_management',
	version=version,
	description='to identify,record,manage,resolve tasks',
	author='Momscode Technologies Pvt.Ltd',
	author_email='info@momscode.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
