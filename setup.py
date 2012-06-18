#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
major, minor = sys.version_info[:2]
kwargs = {}
kwargs['include_package_data'] = True
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup
install_requires = ['Flask']
try:
    import argparse  # python 2.7+ support argparse
except ImportError:
    install_requires.append('argparse')


import feedbundle
from email.utils import parseaddr
author, author_email = parseaddr(feedbundle.__author__)

setup(
    name='feedbundle',
    version=feedbundle.__version__,
    author=author,
    author_email=author_email,
    url=feedbundle.__homepage__,
    packages=['feedbundle'],
    description='FeedBundle',
    license='BSD License',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    **kwargs
)
