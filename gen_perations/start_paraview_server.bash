#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Enter # of pvservers to start."
	echo "Example: start_pvserver.bash 8"
	exit 1
fi

# Kill any existing running pvservers
ps -ef | grep pvserver | grep -v grep | awk '{print $2}' | xargs kill  

if [ $# -ne 1 ]; then
	echo "Enter # of pvservers to start."
	echo "Example: start_pvserver.bash 8"
fi

SERVER=$1 

# Start new pvservers
mpiexec -np $1 \
	vglrun /home/fabidi89/Paraview-v5.2.0/bin/pvserver \
		/home/fabidi89/git/Thesis/vnc_operations/cave-momo.pvx &

