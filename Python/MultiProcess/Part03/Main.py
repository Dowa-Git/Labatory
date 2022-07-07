import os
import sys
import subprocess

# Get Path
Path = os.path.realpath(__file__)
Path2 = os.path.abspath(__file__)
dirPath = os.path.dirname(Path)
Test02TargetPath = f'{dirPath}\\Test_02.py'

# p1 = subprocess.run(args=['dir'], shell=True, capture_output=True)

# print(p1)

p1 = subprocess.Popen(args=[sys.executable, Test02TargetPath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
print('main')

# print(p1.communicate(input='test'))

for i in range(0, 100):
    print(p1.communicate('input\n'))
    p1.wait()