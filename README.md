# Rubik-s-Cube-Solver

This project, created for the Data Structures and Algorithms III course [^Disclaimer], uses four algorithms for solving a Rubik's Cube.

## Authors

- [@Kurisari](https://www.github.com/kurisari)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## File Structure

- `rubiks_cube.py`: Defines the `RubiksCube` class representing the Rubik's Cube. Includes methods for cube movements, shuffling, and printing its state.

- `heuristics.py`: Provides heuristic evaluation methods for the Rubik's Cube state, including counting misplaced stickers, Manhattan distance, and incorrect orientations.

- `rubiks_solver.py`: Implements the RubiksSolver class to solve the Rubik's Cube using various search algorithms. Supports shuffling and printing cube state.

## How to Use

To use this Rubik's Cube solver, follow these steps:

1. Instantiate a `RubiksSolver` object.
2. Shuffle the cube using either random shuffling or by providing a list of movements.
3. Choose a search algorithm: breadth-first search, best-first search, A* search, or iterative deepening A* search.
4. Call the corresponding method to solve the cube.
5. Print the cube's state and the solution.

Example Usage:

```python
solver = RubiksSolver()
solver.shuffle_cube(1)  # Shuffle the cube
solver.print_cube()     # Print the shuffled cube
moves, solution = solver.ida_star_search()  # Solve the cube using IDA* search
print("Solution:", solution)  # Print the solution
print("Number of moves:", moves)  # Print the number of moves required to solve
```

## Aditional Information

- This implementation assumes a standard Rubik's Cube with 3x3x3 dimensions.

- Some heuristic functions are provided but currently commented out. You can enable them as needed for experimentation.

- Dependencies: This code has no external dependencies beyond the Python Standard Library.

[^Disclaimer]: This code is provided as an educational resource and may not be optimized for performance or completeness. Use it at your own discretion.