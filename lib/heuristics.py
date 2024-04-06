class Heuristics:
    # Heuristica 1
    @staticmethod
    def estimate_moves_to_solve(cube):
        total_moves = 0
        # Caras fronal, trasera y superior respectivamente
        for layer in [cube.stickers[0:9], cube.stickers[9:18], cube.stickers[18:27]]:
            incorrect_blocks = sum(1 for i, sticker in enumerate(layer) if sticker != layer[i // 3 * 3])
            incorrect_orientation = sum(1 for i, sticker in enumerate(layer) if i % 3 != 1 and sticker != layer[i // 3 * 3 + 1])
            distances = [abs(i // 3 - i % 3) for i, sticker in enumerate(layer)]
            total_distance = sum(distances)
            total_moves += incorrect_blocks + incorrect_orientation + total_distance
        return total_moves
    
    # Heuristica 2
    @staticmethod
    def estimate_moves_to_solve1(cube):
        misplaced_stickers = Heuristics.count_misplaced_stickers(cube)
        return misplaced_stickers
    
    @staticmethod
    def count_misplaced_stickers(cube):
        misplaced = 0
        for i in range(9):
            if cube.stickers[i] != cube.stickers[4]:
                misplaced += 1
            if cube.stickers[i+18] != cube.stickers[22]:
                misplaced += 1
            if i % 3 != 1:
                if cube.stickers[i*3] != cube.stickers[i*3+1]:
                    misplaced += 1
                if cube.stickers[i*3+2] != cube.stickers[i*3+1]:
                    misplaced += 1
        return misplaced