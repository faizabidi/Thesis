#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Enter the server on which to start VNCSERVER."
    exit 1
fi

SERVER=$1

# We need to start 8 servers on different DISPLAYS on $SERVER

# First, kill all existing vncservers on $SERVER
KILL_VNCSERVER="pkill -f vnc"

ssh $SERVER "$KILL_VNCSERVER"

START_VNCSERVER="vncserver -geometry 12560x1600"
set -ex
for i in {1..8}; do
    if echo $START_VNCSERVER :$i | ssh $SERVER bash; then
        echo "VNC server successfully started on $SERVER:$i"
    else
        echo "Failed to start VNC server on $SERVER:$i"
    fi
done
