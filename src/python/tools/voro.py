#! /usr/bin/env python

# ======================================================================
# Atomistica - Interatomic potential library
# https://github.com/pastewka/atomistica
# Lars Pastewka, lars.pastewka@iwm.fraunhofer.de, and others.
# See the AUTHORS file in the top-level Atomistica directory.
#
# Copyright (2005-2013) Fraunhofer IWM
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ======================================================================

"""
Run Voronoi analysis of a trajectory, and store the results into that
trajectory.
"""

import os
import sys

from atomistica.analysis import voropp
from atomistica.io import NetCDFTrajectory

###

traj = NetCDFTrajectory(sys.argv[1], 'a')

for i, a in enumerate(traj):
    print 'Frame {0}...'.format(i)

    vol, area = voropp(a, q='%v %F', fast=True)

    a.set_array('voronoi_volume', vol)
    a.set_array('voronoi_surface_area', area)

    traj.write_arrays(a, i, ['voronoi_volume', 'voronoi_surface_area'])
traj.close()