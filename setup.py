
config = {
  "name": "bcsv",
  "version": "0.0.1",
  "description": "CSV manipulation tools",
  "url": "https://github.com/BlackEarth/bcsv",
  "author": "Sean Harrison",
  "author_email": "sah@bookgenesis.com",
  "license": "LGPL 3.0",
  "classifiers": [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Programming Language :: Python :: 3"
  ],
  "entry_points": {},
  "install_requires": ["bl"],
  "extras_require": {
    "dev": [],
    "test": []
  },
  "package_data": {
    "bf": []
    },
  "data_files": [],
  "scripts": []
}


import os
from setuptools import setup, find_packages
from codecs import open

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, 'README.md'), encoding='utf-8') as f:
    read_me = f.read()

setup(
    long_description=read_me,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    **config
)