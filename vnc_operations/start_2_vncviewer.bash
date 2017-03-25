#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Enter the VNCSERVER name/IP."
    exit 1
fi

# Kill all existing vncviewers
ps -ef | grep VncViewer | awk '{print $2}' | xargs kill

SERVER=$1

for i in {4..6};do
    j=$((($i/2)+1))
    DISPLAY=:0.$i vncviewer -fullscreen -passwd passwd $SERVER:$j &
done

