# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='postcode_latlng',
    version='0.0.1',
    author=u'Gareth Lloyd',
    author_email='glloyd@gmail.com',
    packages=find_packages(),
    url='https://github.com/gareth-lloyd/postcode_latlng',
    license='BSD licence, see LICENCE.txt',
    description='Parse Ordnance Survey Code-Point Open dataset',
    long_description=open('README.md').read(),
    include_package_data=True,
)
