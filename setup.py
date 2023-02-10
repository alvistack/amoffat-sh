# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sh']
setup_kwargs = {
    'name': 'sh',
    'version': '2.0.0',
    'description': 'Python subprocess replacement',
    'author': 'Andrew Moffat',
    'author_email': 'arwmoffat@gmail.com',
    'maintainer': 'Andrew Moffat',
    'maintainer_email': 'arwmoffat@gmail.com',
    'url': 'https://amoffat.github.io/sh/',
    'py_modules': modules,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
