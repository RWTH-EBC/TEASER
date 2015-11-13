'''
teaser
=========
  
Tool for Energy Analysis and Simulation for Efficient Retrofit 
'''
import sys
import teaser.Logic.Utilis as utilis
import os

v = sys.version_info
if v >= (3, 3):
    py33 = True
    py27 = False
elif v >= (2, 7) and v < (3,):
    py33 = False
    py27 = True
else:
    raise Exception('This software runs on python versions 2.7 or >=3.3 only!')

new_path = utilis.get_full_path("OutputData\\")

dire = os.path.dirname(new_path)

try:
    os.stat(dire)
except:
    os.mkdir(dire) 
    
if sys.platform.startswith('win'):
    def read_file(path, mode='r'):
        fp = open(path, mode)
        try:
            data = fp.read()
            return data
        finally:
            fp.close()
    # hot patch loaded module :-)
    import mako.util
    mako.util.read_file = read_file
    del read_file
