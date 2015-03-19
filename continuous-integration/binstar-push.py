# this file gets executed in project checkout root directory
# e.g. C:\projects\conda-builder (with "conda-builder" being the github repo name)
import os
import glob
import subprocess
import traceback

token = os.environ['BINSTAR_TOKEN']


def upload_files(filenames, channels=None, package_type=None):
    if channels is None:
        channels = ['appveyor', 'main']
    cmd = ['binstar', '-t', token, 'upload', '--force']
    for channel in channels:
        cmd.extend(['--channel', channel])
    if package_type is not None:
        cmd.extend(['--package-type', package_type])
    if not isinstance(filenames, (list, tuple)):
        filenames = [filenames]
    # avoid uploads of Miniconda executable
    filenames = [filename for filename in filenames
                 if "miniconda" not in filename.lower()]
    cmd.extend(filenames)
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        traceback.print_exc()


files = glob.glob('*.tar.bz2')
print(files)
upload_files(files)

files = []
for ext in ['egg', 'whl', 'exe']:
    files.extend(glob.glob('*.%s' % ext))
print(files)
upload_files(files, package_type="pypi")
