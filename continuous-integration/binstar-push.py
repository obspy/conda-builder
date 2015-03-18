# this file gets executed in project checkout root directory
# e.g. C:\projects\conda-builder (with "conda-builder" being the github repo name)
import os
import glob
import subprocess
import traceback

token = os.environ['BINSTAR_TOKEN']
cmd = ['binstar', '-t', token, 'upload',
       '--channel', 'appveyor', '--channel', 'main', '--force']
files = [glob.glob('*.%s' % ext) for ext in ['tar.bz2', 'egg', 'whl', 'exe']]
print(files)
for files_ in files:
    print(files_)
    for file_ in files_:
        print(file_)
        if file_.startswith("Miniconda-"):
            continue
        print(file_)
        cmd.append(file_)
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError:
    traceback.print_exc()
