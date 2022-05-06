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

# assign hydraulic properties by family

variable = "aperture"
function = "constant"
params = {"mu":1*10**-3}
b1,perm1,T1 = DFN.generate_hydraulic_values(variable,function,params,family_id=0)

function = "constant"
params = {"mu":1*10**-3}
b2,perm2,T2 = DFN.generate_hydraulic_values(variable,function,params,family_id=0)

function = "constant"
params = {"mu":1*10**-3}
b3,perm3,T3 = DFN.generate_hydraulic_values(variable,function,params,family_id=0)

function = "constant"
params = {"mu":5*10**-4}
b4,perm4,T4 = DFN.generate_hydraulic_values(variable,function,params,family_id=0)

variable = "transmissivity"
function = "correlated"
params = {"alpha":2.2*10**-9, "beta":0.8}
b5,perm5,T5 = DFN.generate_hydraulic_values(variable,function,params,family_id=1)

function = "correlated"
params = {"alpha":2.2*10**-9, "beta":0.8}
b6,perm6,T6 = DFN.generate_hydraulic_values(variable,function,params,family_id=2)

function = "correlated"
params = {"alpha":2.2*10**-9, "beta":0.8}
b7,perm7,T7 = DFN.generate_hydraulic_values(variable,function,params,family_id=3)



T = T1 + T2 + T3 + T4 + T5 + T6 + T7

b = b1 + b2 + b3+ b4 + b5 + b6 + b7

perm = perm1 + perm2 + perm3 + perm4 + perm5 + perm6 + perm7

DFN.dump_hydraulic_values(b,perm,T)

# Add transmissivity values to the mesh for visualization
DFN.add_variable_to_mesh("trans,", "transmissivity.dat", "full_mesh.inp")

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

