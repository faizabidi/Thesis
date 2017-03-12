#!/bin/bash

FILENAME=$1

if [ $# != 1 ]; then
	echo "Please provide eactly 1 argument, which is the name of the file to process" 
	exit 1
fi

# Remove anything beyond 4 columns
awk -v FS=" " 'NF<=4' $FILENAME > temp_$FILENAME

# Move it back to its original name
mv temp_$FILENAME $FILENAME

