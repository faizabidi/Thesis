#!/bin/bash

# We need to start 8 servers on different DISPLAYS on viz1.sv.vt.edu

# First, kill all existing vncservers on viz1
KILL_VNCSERVER="ps -ef | grep vnc | awk '{print $2}' | xargs -n1 -t kill"
ssh viz1.sv.vt.edu "$KILL_VNCSERVER"

# Start 8 vncservers on viz1
START_VNCSERVER="/opt/TurboVNC/bin/vncserver -geometry 12560x1600"
set -ex
for i in {1..8}; do
    if echo $START_VNCSERVER :$i | ssh viz1.sv.vt.edu bash; then
        echo "VNC server successfully started on viz1.sv.vt.edu:$i"
    else
        echo "Failed to start VNC server on viz1.sv.vt.edu:$i"
    fi
done
    

