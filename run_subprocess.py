import subprocess
import os

# change current working directory to binare/linux/mu
os.chdir("binaries/linux/x86_64")

# construct and run the command
command = "PYTHONPATH=$PYTHONPATH:.:../../../python LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH python ../../../samples/python/recognizer/recognizer.py --image ../../../assets/images/lic_us_1280x720.jpg --assets ../../../assets"
process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)

# send newline character to standard input
process.communicate(input='\n'.encode())

# wait for the subprocess to exit
process.wait()