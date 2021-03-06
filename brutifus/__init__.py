# -*- coding: utf-8 -*-
'''
brutifus: a set of Python modules to process datacubes from integral field spectrographs.\n
Copyright (C) 2018-2020,  F.P.A. Vogt
Copyright (C) 2021, F.P.A. Vogt & J. Suherli
All the contributors are listed in AUTHORS.

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-Identifier: GPL-3.0-or-later

This file specifies the kind of functions that are made directly available to the user.

Created November 2018, F.P.A. Vogt - frederic.vogt@alumni.anu.edu.au
'''
# --------------------------------------------------------------------------------------------------

#from .brutifus import * # So that users only need to do import brutifus
from .brutifus import run
from .brutifus_version import __version__ # Gives users easy access to the version
