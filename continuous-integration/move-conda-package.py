# this file gets executed in project checkout root directory
# e.g. C:\projects\conda-builder (with "conda-builder" being the github repo name)
import sys
import os
import yaml
import glob
import shutil

try:
    from conda_build.config import config
except ImportError:
    from conda_build import config

with open(os.path.join(sys.argv[1], 'meta.yaml')) as f:
    name = yaml.load(f)['package']['name']

# move conda package
for ext in ['tar.bz2']:
    binary_package_glob = os.path.join(config.bldpkgs_dir, '{0}*.{1}'.format(name, ext))
    print(os.path.abspath(config.bldpkgs_dir))
    # is e.g. C:\Python26_32\conda-bld\win-32
    print(binary_package_glob)
    # is e.g. C:\Python26_32\conda-bld\win-32\obspy*.tar.bz2
    print(dir(config))
    for x in dir(config):
        print(x)
        print(getattr(config, x))
    print("=" * 40)
    print(os.path.abspath(os.getcwd()))
    binary_packages = glob.glob(binary_package_glob)
    for file_ in binary_packages:
        shutil.move(file_, '.')

# move egg/whl/exe, seems the source directory name is nowhere to find in ENV
# variables and conda config, so we have to glob our way in there
#     croot is e.g. 'C:\Python26_32\conda-bld'
#     source dir is eg. 'C:\Python26_32\conda-bld\work\obspy-a069d8c97b2b64a6d9f0231effb260713e342bf4' (for commit hash tarball)
print(glob.glob(os.path.join(config.croot, '*')))
print(glob.glob(os.path.join(config.croot, 'work', '*')))
print(glob.glob(os.path.join(config.croot, 'work', '*', '*')))
print(glob.glob(os.path.join(config.croot, 'work', '*', 'dist', '*')))
dist_package_dir_glob = os.path.join(config.croot, 'work', '*', 'dist')
print(dist_package_dir_glob)
for ext in ['egg', 'whl', 'exe']:
    dist_package_glob = os.path.join(dist_package_dir_glob, "*.%s" % ext)
    print(dist_package_glob)
    dist_packages = glob.glob(dist_package_glob)
    print(dist_packages)
    for file_ in dist_packages:
        print(file_)
        shutil.move(file_, '.')
