'''
teaser
=========

Tool for Energy Analysis and Simulation for Efficient Retrofit
'''
import sys
import os

__version__ = "1.1.0"


new_path = os.path.join(os.path.expanduser('~'), ("TEASEROutput"))
if not os.path.exists(new_path):
    os.makedirs(new_path)

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
