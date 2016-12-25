#!/bin/bash

for i in {0..14};do
    DISPLAY=:0.$i vncviewer -fullscreen -passwd passwd viz1.sv.vt.edu:1 &
    i = i + 2
done

