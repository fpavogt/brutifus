# -*- coding: utf-8 -*-
'''
brutifus: a set of Python modules to process datacubes from integral field spectrographs.\n
Copyright (C) 2018-2020,  F.P.A. Vogt
Copyright (C) 2021, F.P.A. Vogt & J. Suherli
All the contributors are listed in AUTHORS.

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-Identifier: GPL-3.0-or-later

Created November 2018, F.P.A. Vogt - frederic.vogt@alumni.anu.edu.au
'''

import os
from setuptools import setup # Always prefer setuptools over distutils

# Run the version file
v = open(os.path.join('.', 'brutifus', 'brutifus_version.py'))
version = [l.split("'")[1] for l in v.readlines() if '__version__' in l][0]

setup(
    name='brutifus',
    version=version,
    author='F.P.A. Vogt',
    author_email='frederic.vogt@alumni.anu.edu.au',
    packages=['brutifus',],
    url='http://fpavogt.github.io/brutifus/',
    download_url='https://github.com/fpavogt/brutifus/archive/master.zip',
    license='GNU General Public License',
    description='Python module to process IFU datacubes.',
    long_description=open('README').read(),
    python_requires='>=3',
    install_requires=[
        "numpy >= 1.14.2",
        "scipy >= 1.1.0",
        "matplotlib >= 3.0.0",
        "astropy >= 3.0",
        "astroquery >= 0.3.4",
        "statsmodels >= 0.9.0",
        "photutils >= 0.6",
        "PyYAML >=5.1"],

    entry_points={'console_scripts': ['brutifus=brutifus.__main__:main']},

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
        ],

    include_package_data=True, # So that non .py files make it onto pypi, and then back !
    #package_data={
    #     'example_files':['example_files/*'],
    #     'docs':['../docs/build']
    #    }
)
