#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:04:03 2020

@author: rosie
"""

import os, sys
from time import time
from pydfnworks import * 
from numpy import *
        
        
define_paths()
main_time = time()
DFN = create_dfn()

DFN.set_flow_solver("PFLOTRAN")

DFN.make_working_directory()
DFN.check_input()
DFN.create_network()
DFN.mesh_network(uniform_mesh=True)


DFN.dfn_flow()

