# -*- coding: utf-8 -*-
# 2017/1/3 14:35
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

from setuptools import setup, find_packages

setup(
    name = 'porndetective',
    version = '1.0.6',
    keywords = (' detect porn', 'Pattern recognition'),
    description = 'provide service for detecting porn picture',
    license = 'Apache License',
    install_requires = ['requests'],

    author = 'LouisSong',
    author_email = 'slysly759@gmail.com',

    packages = find_packages(),
    package_data = {
        # If any package contains *.txt files, include them:
        '': ['*'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
    },


    platforms = 'Python3.x',
)