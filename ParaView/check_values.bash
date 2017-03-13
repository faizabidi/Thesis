#!/bin/bash

FILENAME=$1

# Make sure all values are float
awk '$1 + 0 == $1 && $2 + 0 == $2 && $3 + 0 == $3 && $4 + 0 == $4' $FILENAME > temp

# Move the temp file back to its parent name
mv temp  $FILENAME

