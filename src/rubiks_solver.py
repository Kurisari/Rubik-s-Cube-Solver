import os
import sys
script_dir = os.getcwd()
func_dir = os.path.join(script_dir)
sys.path.append(func_dir)
from lib import rubiks_cube as rc

class RubiksSolver:
    def __init__(self):
        self.cube = rc.RubiksCube()

    def shuffle_cube(self, n=None, movement_list=None):
        if movement_list is None:
            self.cube.random_shuffle(n)
        else:
            self.cube.list_shuffle(movement_list)
    
    def breadth_first_search(self):
        pass
    
    def best_first_search(self):
        pass
    
    def a_star_search(self):
        pass

    def print_cube(self):
        self.cube.print_cube()

lista = [["x", "U", "L"], ["y", "D", "L"], ["z", "L", "D"]]
prueba = RubiksSolver()
prueba.print_cube()
prueba.shuffle_cube(movement_list=lista)
prueba.print_cube()