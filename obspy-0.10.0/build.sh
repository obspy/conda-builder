# this file gets executed in obspy source root directory
# e.g. C:\Python26_32\conda-bld\work\obspy-a344e2e3cb9a433d8ecc21b0a84a4b5996da7bc9 (for a commit hash tarball checkout)
cp -r $RECIPE_DIR/.. $SRC_DIR
$PYTHON setup.py install
