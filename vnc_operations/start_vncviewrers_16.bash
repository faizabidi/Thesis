#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Enter the VNCSERVER name/IP."
    exit 1
fi

# Kill all existing vncviewers
ps -ef | grep VncViewer | awk '{print $2}' | xargs kill

SERVER=$1

for i in {0..14..2};do
    j1=$(($i+1))
	j2=$(($j1+1))
    DISPLAY=:0.$i vncviewer  -passwd passwd $SERVER:$j1 &
	DISPLAY=:0.$i vncviewer  -passwd passwd $SERVER:$j2 &
done

