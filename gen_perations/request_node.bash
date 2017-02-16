#!/bin/bash

qsub -I -l walltime=2:00:00 -l nodes=1:ppn=24:gpus=2 -q vis_q -W group_list=newriver -A arctest -M fabidi89@vt.edu -m bea
