import matplotlib
matplotlib.use("AGG")
from obspy.core import run_tests
#run_tests(report=True, hostname="appveyor-conda-builder", verbosity=2)
errors = run_tests(report=True, tests=["core"], hostname="appveyor-conda-builder", verbosity=2)
import sys
if errors:
    sys.exit(1)
else:
    sys.exit(0)
