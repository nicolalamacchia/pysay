#!/usr/bin/env python

#
# This file is part of pysay v1.4.3 (GitHub edition)
#

from distutils.core import setup

setup(name='pysay',
      version='1.4.3',
      description='A Python version of cowsay',
      author='Nicola Lamacchia',
      author_email='nicola.lamacchia@gmail.com',
      scripts=['scripts/pysay'],
      url='https://github.com/nicolalamacchia/pysay/',
      data_files=[('share/cows', ['cows/python.cow'])],
      license='Artistic License 2.0')
