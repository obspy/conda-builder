import matplotlib
matplotlib.use("AGG")
from obspy.core import run_tests
run_tests(report=True, hostname="appveyor-conda-builder")
