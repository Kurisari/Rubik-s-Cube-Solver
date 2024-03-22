import os
import sys
script_dir = os.getcwd()
func_dir = os.path.join(script_dir)
sys.path.append(func_dir)
from lib import rubiks_cube as rc

class RubiksSolver:
    def __init__(self):
        self.cube = rc.RubiksCube()

    def solve(self):
        pass

    def print_cube(self):
        self.cube.print_cube()

prueba = RubiksSolver()
prueba.print_cube()