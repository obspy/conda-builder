# this file gets executed in project checkout root directory
# e.g. C:\projects\conda-builder (with "conda-builder" being the github repo name)
import os
import glob
import subprocess
import traceback

token = os.environ['BINSTAR_TOKEN']


def upload_file(filename, channels=None, package_type=None, version=None):
    # avoid uploads of Miniconda executable
    if "miniconda" in filename.lower():
        return
    if channels is None:
        channels = ['appveyor', 'main']
    cmd = ['anaconda', '-t', token, 'upload', '--force','--no-progress']
    for channel in channels:
        cmd.extend(['--channel', channel])
    if package_type is not None:
        cmd.extend(['--package-type', package_type])
    if version is not None:
        cmd.extend(['--version', version])
    cmd.append(filename)
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError:
        traceback.print_exc()


files = glob.glob('*.tar.bz2')
# version number has to be specified manually for package type "pypi" uploads
# unfortunately it is not set in any env variable (only during bld.bat/build.sh run itself),
# so we have to extract it from built conda package filename
version = files[0].split("-")[1]
for file_ in files:
    print(file_)
    upload_file(file_)

for ext in ['egg', 'whl', 'exe']:
    for file_ in glob.glob('*.%s' % ext):
        print(file_)
        upload_file(file_, package_type="pypi", version=version)
