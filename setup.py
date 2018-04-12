#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2018 Cyril Desjouy <ipselium@free.fr>
#
# This file is part of {name}
#
# {name} is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {name} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with {name}. If not, see <http://www.gnu.org/licenses/>.
#
#
# Creation Date : mar. 10 avril 2018 17:52:42 CEST
# Last Modified : jeu. 12 avril 2018 09:59:34 CEST
"""
-----------
DOCSTRING

@author: Cyril Desjouy
"""

from setuptools import setup, find_packages
import mpltools

setup(

    name='mpltools',
    description="Tools for matplotlib",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version=mpltools.__version__,
    license="GPL",
    url='http://github.com/ipselium/mpltools',
    author="Cyril Desjouy",
    author_email="ipselium@free.fr",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "matplotlib"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ]
)
