# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:04:03 2020

@author: rosie
"""



import os, sys
from time import time
from pydfnworks import *
import subprocess
from numpy import *

define_paths()
main_time = time()
DFN = create_dfn()

##dfnGen
DFN.make_working_directory()
DFN.check_input()
DFN.create_network()
DFN.mesh_network(visual_mode=False)

##dfnFlow
#DFN.pflotran()
#DFN.parse.pflotran_vtk_python()
#DFN.pflotran_cleanup()

DFN.dfn_flow()

##dfnTrans
#DFN.copy_dfn_trans_files()
#DFN.check_dfn_trans_run_files()
#DFN.run_dfn_trans()

DFN.dfn_trans()

