#!/bin/bash

qsub -I -l walltime=4:00:00 -l nodes=1:ppn=24:gpus=1 -q vis_q -W group_list=newriver -A arctest -M fabidi89@vt.edu -m bea
