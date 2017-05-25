#!/bin/bash
if [ $# -ne 7 ]; then
    echo "Enter encoding type(use Tight), jpeg (0 or 1), quality(0 to 100), chrominance subsampling (1x, 2x, etc.), compression level(0 to 9), VNCSERVER name/IP, and fullscreen (0 or 1)"
    exit 1
fi

ENCODING=$1
JPEG=$2
QUALITY=$3
SUBSAMPLING=$4
COMPRESS_LEVEL=$5
SERVER=$6
FULLSCREEN=$7

# Kill all existing vncviewers
ps -ef | grep VncViewer | awk '{print $2}' | xargs kill

for i in {0..14..2};do
    j1=$(($i+1))
	j2=$(($j1+1))
    DISPLAY=:0.$i vncviewer -fullscreen=$7 -passwd=passwd -encoding $ENCODING -jpeg=$JPEG -quality $QUALITY -subsampling $SUBSAMPLING -compresslevel $COMPRESS_LEVEL $SERVER:$j1 &
	#DISPLAY=:0.$i vncviewer -fullscreen=$7 -passwd=passwd -encoding $ENCODING -jpeg=$JPEG -quality $QUALITY -subsampling $SUBSAMPLING -compresslevel $COMPRESS_LEVEL $SERVER:$j2 &
done

