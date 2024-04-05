class Heuristics:
    @staticmethod
    def estimate_moves_to_solve(cube):
        upper_layer_moves = Heuristics.estimate_moves_for_layer(cube, [18, 19, 20, 21, 22, 23, 24, 25, 26])
        middle_layer_moves = Heuristics.estimate_moves_for_layer(cube, [0, 1, 2, 3, 4, 5, 6, 7, 8])
        lower_layer_moves = Heuristics.estimate_moves_for_layer(cube, [27, 28, 29, 30, 31, 32, 33, 34, 35])
        total_moves = upper_layer_moves + middle_layer_moves + lower_layer_moves
        return total_moves

    @staticmethod
    def estimate_moves_for_layer(cube, stickers_indices):
        correct_stickers = sum(1 for i in stickers_indices if cube.stickers[i] == cube.stickers[i // 9 * 9])
        moves_needed = len(stickers_indices) - correct_stickers
        return moves_needed