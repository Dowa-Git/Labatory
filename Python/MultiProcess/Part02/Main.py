import os
import sys
import subprocess

# Get Path
Path = os.path.realpath(__file__)
Path2 = os.path.abspath(__file__)
dirPath = os.path.dirname(Path)
TargetPath = f'{dirPath}\\test_01.py'
TargetPath2 = f'{dirPath}\\test_02.py'
ResultPath = f'{dirPath}\\result.txt'
FileSavePath = f'{dirPath}\\FileSaveResult.txt'

# Simple Use
# subprocess.run(args=[sys.executable, TargetPath])
# subprocess.run(args=[sys.executable, TargetPath2])


# Storage the process result
p1 = subprocess.run(args=[sys.executable, TargetPath], capture_output=True)
print(p1.stdout.decode())
# Same with up on code
# p1 = subprocess.run(args=[sys.executable, TargetPath], capture_output=True, text=True)
# print(p1.stdout)

p2 = subprocess.run(args=[sys.executable, TargetPath2, p1.stdout])

p3 = subprocess.run(args=["type", ResultPath], shell=True, capture_output=True, encoding='utf8')
p4 = subprocess.run(args=['findstr', '-n', '19'], shell=True, capture_output=True, encoding='utf8', text=True, input=p3.stdout)
print(p4.stdout)


with open(FileSavePath, 'w', encoding='utf8') as FileResult:
    p5 = subprocess.run(args=[sys.executable, TargetPath], capture_output=True, text=True, encoding='utf8')
    p6 = subprocess.run(args=[sys.executable, TargetPath2, p1.stdout], capture_output=True, text=True, encoding='utf8')
    FileResult.write(p6.stdout)