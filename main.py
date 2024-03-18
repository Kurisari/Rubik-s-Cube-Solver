class RubiksCube:
    def __init__(self):
        self.stickers = ['F'] * 9 + ['B'] * 9 + ['U'] * 9 + ['D'] * 9 + ['L1'] + ['L'] * 8 + ['R'] * 9
    
    def x_movement(self, direction):
        if direction == "up":
            pass
        elif direction == "down":
            temp = self.stickers[0], self.stickers[3], self.stickers[6]
            self.stickers[0], self.stickers[3], self.stickers[6] = self.stickers[18], self.stickers[21], self.stickers[24]
            self.stickers[18], self.stickers[21], self.stickers[24] = self.stickers[11], self.stickers[14], self.stickers[17]
            self.stickers[11], self.stickers[14], self.stickers[17] = self.stickers[27], self.stickers[30], self.stickers[33]
            self.stickers[27], self.stickers[30], self.stickers[33] = temp
            self.left_rotation("clockwise")
    
    def left_rotation(self, direction):
        if direction == "clockwise":
            temp = self.stickers[36]
            self.stickers[36] = self.stickers[39]
            self.stickers[39] = self.stickers[42]
            self.stickers[42] = self.stickers[43]
            self.stickers[43] = self.stickers[44]
            self.stickers[44] = self.stickers[41]
            self.stickers[41] = self.stickers[38]
            self.stickers[38] = self.stickers[37]
            self.stickers[37] = temp
        elif direction == "counterclockwise":
            pass
    
    def print_cube(self):
        print("               ", self.stickers[18:21])
        print("               ", self.stickers[21:24])
        print("               ", self.stickers[24:27])
        print(self.stickers[36:39], self.stickers[0:3], self.stickers[45:48], self.stickers[9:12])
        print(self.stickers[39:42], self.stickers[3:6], self.stickers[48:51], self.stickers[12:15])
        print(self.stickers[42:45], self.stickers[6:9], self.stickers[51:54], self.stickers[15:18])
        print("               ", self.stickers[27:30])
        print("               ", self.stickers[30:33])
        print("               ", self.stickers[33:36])

cube = RubiksCube()
cube.print_cube()

# cube.x_movement("up")
# print("\nEstado después de mover hacia arriba:")
# cube.print_cube()

cube.x_movement("down")
print("\nEstado después de mover hacia abajo:")
cube.print_cube()