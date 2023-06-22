#!/bin/bash
CURRENT_DIR=$(pwd)
echo "The current directory is: $CURRENT_DIR"
cd binaries/linux/x86_64
CURRENT_DIR=$(pwd)
echo "The current directory is: $CURRENT_DIR"
PYTHONPATH=$PYTHONPATH:.:../../../python LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH python ../../../samples/python/recognizer/recognizer.py --image ../../../assets/images/lic_us_1280x720.jpg --assets ../../../assets