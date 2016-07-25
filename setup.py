#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


tests_require = [
    'coverage',
    'pep8',
    'pyflakes',
    'pylint',
    'pytest-cov',
    'pytest-xdist',
]

dev_require = [
    'ipdb',
    'ipython',
]

docs_require = [
    'Sphinx>=1.3.5',
    'sphinx-autobuild',
    'sphinxcontrib-napoleon>=0.4.4',
    'sphinx_rtd_theme',
]


setup(
    name='pytest-rethinkdb',
    version='0.1.1',
    author='Sylvain Bellemare',
    author_email='sylvain@bigchaindb.com',
    maintainer='Sylvain Bellemare',
    maintainer_email='sylvain@bigchaindb.com',
    license='MIT',
    url='https://github.com/bigchaindb/pytest-rethinkdb',
    description='A RethinkDB plugin for pytest.',
    long_description=read('README.rst'),
    py_modules=['pytest_rethinkdb'],
    install_requires=['pytest>=2.9.1', 'rethinkdb>=2.3.0'],
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    extras_require={
        'test': tests_require,
        'dev': dev_require + tests_require + docs_require,
        'docs': docs_require,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'rethinkdb = pytest_rethinkdb',
        ],
    },
)
