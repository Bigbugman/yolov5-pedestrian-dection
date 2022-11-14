#!/bin/sh

# Author : Chenxiang Wang
# Copyright (c)  COMP9444

sample_usage="Sample Usage: ./run <xxx.yaml>  <epochs> <batch-siz> \nFor instance:\n./run yolov5n.yam 300 128"
if  [ $# -lt 3 ]
then
    echo $sample_usage
    exit 1
fi
#python -v
cd yolov5
nohup python train.py --data data.yaml --cfg $1 --epochs $2 --weights '' --batch-size $3 >/dev/null 2>&1 &
