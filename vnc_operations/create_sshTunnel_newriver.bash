#!/bin/bash

# We need to forward 8 VNC ports
# They start from 5901

if [ $# -ne 1 ]; then
	echo "Enter the name of the NewRiver node that you got."
	exit 1
fi

NODE=$1
SERVER="fabidi89@newriver3.arc.vt.edu"

ssh -L 5901:$NODE:5901 -L 5902:$NODE:5902 -L 5903:$NODE:5903 \
		-L 5904:$NODE:5904 -L 5905:$NODE:5905 -L 5906:$NODE:5906 \
		-L 5907:$NODE:5907 -L 5908:$NODE:5908 $SERVER

echo "Start VNC viewers to connect to the server like localhost:1".

