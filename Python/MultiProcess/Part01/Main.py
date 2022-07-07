import os
import sys
import subprocess

# Get Path
Path = os.path.realpath(__file__)
Path2 = os.path.abspath(__file__)
dirPath = os.path.dirname(Path)
TargetPath = f'{dirPath}\Test.py'

# SubProcess Example 1 : Simple Useage
subprocess.run([sys.executable, TargetPath], shell=True)

# SubProcess Example 2 : With File IO
File = open(f'{dirPath}\OutputTest.txt', 'w')
out = subprocess.check_output([sys.executable, TargetPath], shell=True, encoding='utf-8')
File.write(out)
File.close()
