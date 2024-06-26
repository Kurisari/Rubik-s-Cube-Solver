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
        self.movements2 = [
            ["x", "U", "L"],
            ["x", "U", "R"],
            ["y", "U", "L"],
            ["y", "U", "R"],
            ["z", "L", "U"],
            ["z", "L", "D"]
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
    
    def breadth_first_search(self):
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
        priority_queue = PriorityQueue()
        priority_queue.put((0, [], self.cube))
        target = rc.RubiksCube()
        while not priority_queue.empty():
            _, moves, current_cube = priority_queue.get()
            if self.is_solved(current_cube):
                return len(moves), moves
            if current_cube not in visited:
                visited.add(current_cube)
                for move in self.movements2:
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.move(move)
                    if new_cube not in visited:
                        priority = hr.Heuristics.count_incorrect_orientations(new_cube)
                        new_cube.heuristic = priority
                        priority_queue.put((priority, moves + [move], new_cube))

    def a_star_search(self):
        visited = set()
        priority_queue = PriorityQueue()
        priority_queue.put((0, [], self.cube))
        target = rc.RubiksCube()
        while not priority_queue.empty():
            _, moves, current_cube = priority_queue.get()
            if self.is_solved(current_cube):
                return len(moves), moves
            if current_cube not in visited:
                visited.add(current_cube)
                for move in self.movements2:
                    new_cube = copy.deepcopy(current_cube)
                    new_cube.move(move)
                    if new_cube not in visited:
                        priority = len(moves) + hr.Heuristics.count_incorrect_orientations(new_cube)
                        new_cube.heuristic = priority
                        priority_queue.put((priority, moves + [move], new_cube))
        return None
    
    def ida_star_search(self):
        target = rc.RubiksCube()
        threshold = hr.Heuristics.count_incorrect_orientations(self.cube)
        while True:
            result = self.search_depth_limit(self.cube, [], threshold)
            if result is not None:
                return len(result), result
            threshold += 1
    
    def search_depth_limit(self, current_cube, moves, threshold):
        target = rc.RubiksCube()
        cost = len(moves) + hr.Heuristics.count_incorrect_orientations(current_cube)
        if cost > threshold:
            return None
        if self.is_solved(current_cube):
            return moves
        min_cost = float('inf')
        best_moves = None
        for move in self.movements2:
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
prueba.shuffle_cube(1)
prueba.print_cube()
start_time = time.time()
print(prueba.ida_star_search())
elapsed_time = time.time() - start_time
print("\rTime elapsed: {:.2f} seconds".format(elapsed_time), end="", flush=True)