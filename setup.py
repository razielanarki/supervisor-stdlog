#!/usr/bin/env python
import os
from setuptools import setup

setup(
  name = 'supervisor-stdlog',
  version = '0.7.9',
  py_modules = ['supervisor_stdlog'],
  author = 'Raziel Anarki',
  author_email = 'razielanarki@semmi.se',
  description = 'A simple supervisord event listener to relay process stdout and stderr to supervisor\'s stdout.',
  long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
  long_description_content_type = 'text/markdown',
  license = 'License :: OSI Approved :: MIT License',
  keywords = 'supervisord, supervisord-configuration, logging, containerization',
  url = 'http://github.com/razielanarki/supervisor-stdlog',
  install_requires=[
    "supervisor >= 4.2.5"
  ],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
  entry_points = {
    'console_scripts': [
      'supervisor-stdlog = supervisor_stdlog:main',
    ]
  }
)
