#!/bin/bash

FILE=$1

cat $FILE | grep "Still Render" | awk '{sum += $3; n++} END { if (n > 0) print sum / n; }'
cat $FILE | grep "Interactive Render" | awk '{sum += $3; n++} END { if (n > 0) print sum / n; }'
