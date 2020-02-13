import os
import numpy as np

def open_xyz(molecule):
    '''
    Open an xyz file and return symbols and coordinates.

    Parameters
    ----------
    molecule: 
        str
            The name of the xyz file.
    Return
    ------
    symbols:
        list[str]
            The symbol of the molecule
    coords:
        list[float]
            The coords of every atoms of the molecule
    '''
    dirname = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(dirname, molecule+'.xyz')      
    xyz_file = np.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = list(xyz_file[:,0])
    
    coords = []
    for items in xyz_file[:,1:]:
        coords.append(list(items))
    coords = coords.astype(np.float)

    return symbols, coords


