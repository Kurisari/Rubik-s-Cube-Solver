class Heuristics:
    @staticmethod
    def count_misplaced_stickers(cube, target):
        misplaced = 0
        for i in range(len(cube.stickers)):
            if cube.stickers[i] != target.stickers[i]:
                misplaced += 1
        return misplaced
    
    @staticmethod
    def manhattan_distance(cube, target):
        distance = 0
        for i in range(len(cube.stickers)):
            current_sticker = cube.stickers[i]
            target_index = target.stickers.index(current_sticker)
            current_row, current_col = i // 3, i % 3
            target_row, target_col = target_index // 3, target_index % 3
            distance += abs(current_row - target_row) + abs(current_col - target_col)
        return distance
    
    @staticmethod
    def count_incorrect_orientations(cube):
        incorrect_orientations = 0
        for i in range(9):
            if cube.stickers[i] != cube.stickers[4]:
                incorrect_orientations += 1
            if cube.stickers[i+18] != cube.stickers[22]:
                incorrect_orientations += 1
            if i % 3 != 1:
                if cube.stickers[i*3] != cube.stickers[i*3+1]:
                    incorrect_orientations += 1
                if cube.stickers[i*3+2] != cube.stickers[i*3+1]:
                    incorrect_orientations += 1
        return incorrect_orientations
    
    # Heuristica 1
    # @staticmethod
    # def estimate_moves_to_solve(cube):
    #     upper_layer_moves = Heuristics.estimate_moves_for_layer(cube, [18, 19, 20, 21, 22, 23, 24, 25, 26])
    #     middle_layer_moves = Heuristics.estimate_moves_for_layer(cube, [0, 1, 2, 3, 4, 5, 6, 7, 8])
    #     lower_layer_moves = Heuristics.estimate_moves_for_layer(cube, [27, 28, 29, 30, 31, 32, 33, 34, 35])
    #     total_moves = upper_layer_moves + middle_layer_moves + lower_layer_moves
    #     return total_moves

    # @staticmethod
    # def estimate_moves_for_layer(cube, stickers_indices):
    #     correct_stickers = sum(1 for i in stickers_indices if cube.stickers[i] == cube.stickers[i // 9 * 9])
    #     moves_needed = len(stickers_indices) - correct_stickers
    #     return moves_needed
    
    # Heuristica 2
    # @staticmethod
    # def estimate_moves_to_solve1(cube):
    #     misplaced_stickers = Heuristics.count_misplaced_stickers(cube)
    #     return misplaced_stickers
    
    # @staticmethod
    # def count_misplaced_stickers(cube):
    #     misplaced = 0
    #     for i in range(9):
    #         if cube.stickers[i] != cube.stickers[4]:
    #             misplaced += 1
    #         if cube.stickers[i+18] != cube.stickers[22]:
    #             misplaced += 1
    #         if i % 3 != 1:
    #             if cube.stickers[i*3] != cube.stickers[i*3+1]:
    #                 misplaced += 1
    #             if cube.stickers[i*3+2] != cube.stickers[i*3+1]:
    #                 misplaced += 1
    #     return misplaced