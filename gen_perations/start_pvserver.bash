#!/bin/bash

# Kill any existing running pvservers
#pkill pvserver

# Start 8 new pvservers
mpiexec -np 8 \
	vglrun pvserver \
	/home/fabidi89/git/Thesis/vnc_operations/cave-momo.pvx &
