REM this file gets executed in obspy source root directory
REM e.g. C:\Python26_32\conda-bld\work\obspy-a344e2e3cb9a433d8ecc21b0a84a4b5996da7bc9 (for a commit hash tarball checkout)
REM python -c "print('=' * 40)"
REM python -c "import os; print(os.path.abspath(os.getcwd()))"
REM python -c "print('=' * 40)"
python setup.py install
REM the following doesn't work because it gets line-wrapped in the middle of the string?!
REM python -c 'import pip; pip.main(["install", "wheel"])'
python setup.py bdist_egg
python setup.py bdist_wheel
python setup.py bdist_wininst
if errorlevel 1 exit 1
