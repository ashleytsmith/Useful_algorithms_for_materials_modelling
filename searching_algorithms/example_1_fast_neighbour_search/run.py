import datetime

import os

from ase import Atoms
import numpy as np

from searching_algorithms import input_and_ouput as io
from searching_algorithms import sorting
from searching_algorithms import geometry

from searching_algorithms.example_1_fast_neighbour_search import test


'''
Searches fo the nearest neighbours of each atom in a 3D cell.
'''


def run():

    # input params

    bins_per_dimension = 4

    input_structure = os.getcwd() + "/Input_structures/CHA.traj"
    
    # read infile
    
    atoms,positions,symbols, cell = io.read_trajfile(input_structure)

    # generate some bin positions. Just for visualsing. Not needed for actual computation.
    
    #test.view_the_grid(input_structure)
    bin_positions, edges = geometry.generate_grid(cell,bins_per_dimension)

    # binning procedure
 
    indices = np.arange(len(positions))
    bins_shape = (bins_per_dimension,bins_per_dimension,bins_per_dimension)
    bins = sorting.sort_into_bins(positions,symbols,indices,cell,bins_shape)


    # pad the bin

    
    
    # test the binning procedure

    #test.count_occupied_bins(bins,bins_shape)

    #test.test_bin_assignment_along_first_axis(bins, bin_positions,cell)

    #test.show_atoms_in_each_bin(bins,cell,True)

    #test.test_periodic_boundary_conditions(bins,cell)

    #test.show_neighbours_of_each_bin(bins,cell)






    #save file

    #atoms.extend(bin_atoms)

    #io.save_file(atoms,'test.traj')

    
    

    start = datetime.datetime.now()

    finish = datetime.datetime.now()

  

    print(finish-start)


    





    





