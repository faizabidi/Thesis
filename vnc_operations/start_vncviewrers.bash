#!/bin/bash

for i in {0..14..2};do
    j=$((($i/2)+1))
    DISPLAY=:0.$i vncviewer -fullscreen -passwd passwd console.sv.vt.edu:$j &
done

