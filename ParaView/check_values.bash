#!/bin/bash

FILENAME=$1

awk '$1 + 0 == $1 && $2 + 0 == $2 && $3 + 0 == $3 && $4 + 0 == $4' $FILENAME

