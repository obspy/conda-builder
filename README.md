About
=====

This is a repository to build conda packages for ObsPy for use in continuous
integration on Travis and AppVeyor. We build packages and upload them to the
``obspy`` binstar channel.

Forked from [astropy/conda-builder](https://github.com/astropy/conda-builder)

Travis is currently deactivated for this repository because we build Linux
conda packages differently because of #1 (Travis has Ubuntu 12.04 and thus a
more recent libc6, 2.14, than some older distributions).
