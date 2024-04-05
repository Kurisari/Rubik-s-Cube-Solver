import os
import sys
from collections import deque
import copy
import heapq
import time
script_dir = os.getcwd()
func_dir = os.path.join(script_dir)
sys.path.append(func_dir)
from lib import rubiks_cube as rc
from lib import heuristics as hr

class RubiksSolver:
    def __init__(self):
        self.cube = rc.RubiksCube()
        self.movements = [
            ["x", "U", "L"],
            ["x", "U", "R"],
            ["x", "D", "L"],
            ["x", "D", "R"], 
            ["y", "U", "L"],
            ["y", "U", "R"],
            ["y", "D", "L"],
            ["y", "D", "R"],
            ["z", "L", "U"],
            ["z", "L", "D"],
            ["z", "R", "U"],
            ["z", "R", "D"]
        ]
    
    def is_solved(self, cube):
        for i in range(0, 45, 9):
            face_color = cube.stickers[i]
            if any(sticker != face_color for sticker in cube.stickers[i:i+9]):
                return False
        return True

    def shuffle_cube(self, n=None, movement_list=None):
        if movement_list is None:
            self.cube.random_shuffle(n)
        else:
            self.cube.list_shuffle(movement_list)
    
    def breadth_first_search(self): # Máximo 5 movimientos
        queue = deque([(self.cube, [])])
        visited = set()
        while queue:
            current_cube, moves = queue.popleft()
            if self.is_solved(current_cube):
                return len(moves), moves
            for move in self.movements:
                new_cube = copy.deepcopy(current_cube)
                new_cube.move(move)
                
                if new_cube not in visited:
                    queue.append((new_cube, moves + [move]))
                    visited.add(new_cube)
    
    def best_first_search(self):
        visited = set()
        priority_queue = []
        heapq.heappush(priority_queue, (0, [], self.cube))
        while priority_queue:
            _, moves, current_cube = heapq.heappop(priority_queue)
            if self.is_solved(current_cube):
                return len(moves), moves
            if current_cube not in visited:
                visited.add(current_cube)
                for move in self.movements:
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.move(move)
                    if new_cube not in visited:
                        priority = len(moves) + hr.Heuristics.estimate_moves_to_solve(new_cube)
                        heapq.heappush(priority_queue, (priority, moves + [move], new_cube))

        return None  # Si no se encuentra una solución


    
    def a_star_search(self):
        pass

    def print_cube(self):
        self.cube.print_cube()

# lista = [["x", "U", "L"], ["y", "D", "L"], ["z", "L", "D"]]
lista = [["x", "D", "L"], ["y", "U", "L"], ["x", "U", "L"], ["y", "U", "R"], ["x", "D", "R"]]
prueba = RubiksSolver()
prueba.print_cube()
prueba.shuffle_cube(5)
prueba.print_cube()
# time1 = time.time()
# print(prueba.breadth_first_search())
# time2 = time.time()
# print(time2 - time1)
# print()
# prueba.shuffle_cube(movement_list=lista)
start = time.time()
print(prueba.best_first_search())
end = time.time()
print(end - start)