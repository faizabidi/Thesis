#!/bin/bash

# We need to start 8 servers on different DISPLAYS on console.sv.vt.edu

# First, kill all existing vncservers on viz1
KILL_VNCSERVER="pkill -f vnc"
#echo $KILL_VNCSERVER

ssh console.sv.vt.edu "$KILL_VNCSERVER"

#: <<'END'
# Start 8 vncservers on console
START_VNCSERVER="vncserver -geometry 12560x1600"
set -ex
for i in {1..8}; do
    if echo $START_VNCSERVER :$i | ssh console.sv.vt.edu bash; then
        echo "VNC server successfully started on console.sv.vt.edu:$i"
    else
        echo "Failed to start VNC server on console.sv.vt.edu:$i"
    fi
done
#END
