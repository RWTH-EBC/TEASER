Frequently Asked Questions
=============================

After installing TEASER with pip I get error messages from python packages NumPy or SciPy
-----------------------------------------------------------------------------------------

If you have installed TEASER using pip, it also tries to update all required
packages. This update often fails for NumPy and SciPy. NumPy and SciPy packages
come with some pre-compiled binaries, the installation with pip under windows
does often not work with these binaries (espacially using a 64bit system). You
need to update NumPy and SciPy manually. To do this please select the correct
file from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy and
http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy regarding your system
architecure (32bit or 64bit) and your Python version (e.g. 3.5 or 3.6). Download
the corresponding file, navigate with your Python enabled command line to the
download folder and install the wheel files, in this example we are using python
3.5 and a 64bit architecture::

    pip install numpy-1.12.1+mkl-cp35-cp35m-win_amd64.whl
    pip install scipy-0.19.0-cp35-cp35m-win_amd64.whl
