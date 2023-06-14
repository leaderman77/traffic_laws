import subprocess
import os

# change current working directory to binare/linux/mu
os.chdir("binaries/linux/x86_64")

# construct and run the command
command = "PYTHONPATH=$PYTHONPATH:.:../../../python LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH python ../../../samples/python/recognizer/recognizer.py --image ../../../assets/images/lic_us_1280x720.jpg --assets ../../../assets"
subprocess.run(command, shell=True)