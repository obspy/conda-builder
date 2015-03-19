import matplotlib
matplotlib.use("AGG")
from obspy.core import runTests
runTests(report=True, hostname="appveyor-conda-builder")
