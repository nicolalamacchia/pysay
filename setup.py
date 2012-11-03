#!/usr/bin/env python

#
# This file is part of pysay v1.0 (GitHub edition)
#

from distutils.core import setup

setup(name='pysay',
      version='1.0',
      description=' A Python version of cowsay',
      author='Nicola Lamacchia',
      author_email='nicola.lamacchia@gmail.com',
      scripts=['scripts/pysay'],
      url='https://github.com/nicolalamacchia/pysay/',
      data_files=[('share/cows', ['cows/python.cow', 'cows/default.cow']),
                  ('', ['README.md']),
                  ('', ['LICENSE']),
                  ('', ['INSTALL.md'])],
      license='Artistic License 2.0'
     )
