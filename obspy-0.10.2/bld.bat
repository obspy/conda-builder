REM this file gets executed in obspy source root directory
REM e.g. C:\Python26_32\conda-bld\work\obspy-a344e2e3cb9a433d8ecc21b0a84a4b5996da7bc9 (for a commit hash tarball checkout)
"%PYTHON%" -c "print('=' * 40)"
"%PYTHON%" -c "import os; print(os.path.abspath(os.getcwd()))"
"%PYTHON%" -c "print('=' * 40)"
"%PYTHON%" setup.py install
REM the following doesn't work because it gets line-wrapped in the middle of the string?!
REM "%PYTHON%" -c 'import pip; pip.main(["install", "wheel"])'
"%SCRIPTS%\\pip.exe" install wheel
"%PYTHON%" setup.py bdist_egg
"%PYTHON%" setup.py bdist_wheel
"%PYTHON%" setup.py bdist_wininst
if errorlevel 1 exit 1
