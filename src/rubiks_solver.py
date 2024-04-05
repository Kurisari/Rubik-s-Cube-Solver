import os
import sys
from collections import deque
import copy
from queue import PriorityQueue
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
    
    def best_first_search(self): # Mejor de los casos 6 movimientos Heuristica 1
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, [], self.cube))
        while not priority_queue.empty():
            _, moves, current_cube = priority_queue.get()
            if self.is_solved(current_cube):
                return len(moves), moves
            if current_cube not in visited:
                visited.add(current_cube)
                for move in self.movements:
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.move(move)
                    if new_cube not in visited:
                        priority = hr.Heuristics.estimate_moves_to_solve(new_cube)
                        priority_queue.put((priority, moves + [move], new_cube))
        return None

    def a_star_search(self): # Mejor de los casos 7 movimientos Heuristica 1
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, [], self.cube))
        while not priority_queue.empty():
            _, moves, current_cube = priority_queue.get()
            if self.is_solved(current_cube):
                return len(moves), moves
            if current_cube not in visited:
                visited.add(current_cube)
                for move in self.movements:
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.move(move)
                    if new_cube not in visited:
                        priority = len(moves) + hr.Heuristics.estimate_moves_to_solve(new_cube)
                        priority_queue.put((priority, moves + [move], new_cube))
        return None
    
    def ida_star_search(self): # 7 movimientos con 6 movements heuristica 2
        threshold = hr.Heuristics.estimate_moves_to_solve1(self.cube)
        while True:
            result = self.search_depth_limit(self.cube, [], threshold)
            if result is not None:
                return len(result), result
            threshold += 1
    
    def search_depth_limit(self, current_cube, moves, threshold):
        cost = len(moves) + hr.Heuristics.estimate_moves_to_solve1(current_cube)
        if cost > threshold:
            return None
        if self.is_solved(current_cube):
            return moves
        min_cost = float('inf')
        best_moves = None
        for move in self.movements:
            new_cube = copy.deepcopy(current_cube)
            new_cube.move(move)
            new_moves = moves + [move]
            result = self.search_depth_limit(new_cube, new_moves, threshold)
            if result is not None:
                if min_cost == float('inf') or len(result) < min_cost:
                    min_cost = len(result)
                    best_moves = result
        return best_moves

    def print_cube(self):
        self.cube.print_cube()

lista = [["x", "D", "L"], ["y", "U", "L"], ["x", "U", "L"], ["y", "U", "R"], ["x", "D", "R"]]
prueba = RubiksSolver()
prueba.shuffle_cube(5)
prueba.print_cube()
start = time.time()
print(prueba.breadth_first_search())
end = time.time()
print(end - start)