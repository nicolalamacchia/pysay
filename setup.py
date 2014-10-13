#!/usr/bin/env python

# This file is part of pysay v2.0.0 (GitHub edition)

from distutils.core import setup

setup(name='pysay',
      version='2.0.0',
      description='A Python version of cowsay',
      author='Nicola Lamacchia',
      author_email='nicola.lamacchia@gmail.com',
      scripts=['scripts/pysay', 'scripts/pythink'],
      url='https://github.com/nicolalamacchia/pysay/',
      data_files=[('share/cows', ['cows/python.cow'])],
      license='Artistic License 2.0',
      keywords='fortune cowsay terminal',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Topic :: Games/Entertainment',
          'Topic :: Terminals',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: Artistic License',
          'Intended Audience :: Other Audience',
          'Intended Audience :: End Users/Desktop',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
      ])
