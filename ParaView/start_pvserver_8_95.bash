#!/bin/bash

mpiexec -np 8 vglrun -np 8 -pr -q 95 /home/fabidi89/Paraview-v5.2.0/bin/pvserver ~/git/Thesis/vnc_operations/cave-momo.pvx
