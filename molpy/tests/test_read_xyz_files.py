import pytest
import molpy
import numpy as np

@pytest.mark.parametrize("molecule, symbols, coords",[
    ('water',
     ['H', 'H', 'O'],
     [[np.array([ 9.626,  6.787, 12.673]), 
       np.array([ 9.626,  8.42 , 12.673]), 
       np.array([10.203,  7.604, 12.673])]])
    ])


def test_read_xyz_files(molecule, symbols, coords):

    assert molpy.data.open_xyz(molecule)[0] == symbols
#    assert molpy.data.open_xyz(molecule)[1] == coords
    
    

