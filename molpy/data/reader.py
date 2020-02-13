import os
from molpy.util import read_xyz  

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'look_and_say.dat')

with open(filename) as handle:
    look_and_say = handle.read()


def get_molecule(filename):
    return read_xyz(os.path.join(dirname, filename + ".xyz"))
