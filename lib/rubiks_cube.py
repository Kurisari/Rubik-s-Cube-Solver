class RubiksCube:
    def __init__(self):
        self.stickers = ['W'] * 9 + ['Y'] * 9 + ['O'] * 9 + ['R'] * 9 + ['G'] * 9  + ['B'] * 9
    
    def x_movement(self, direction, position):
        if position == "L":
            plus = 0
        elif position == "R":
            plus = 2
        if direction == "U":
                temp = self.stickers[6+plus], self.stickers[3+plus], self.stickers[0+plus]
                self.stickers[6+plus], self.stickers[3+plus], self.stickers[0+plus] = self.stickers[33+plus], self.stickers[30+plus], self.stickers[27+plus]
                self.stickers[33+plus], self.stickers[30+plus], self.stickers[27+plus] = self.stickers[11-plus], self.stickers[14-plus], self.stickers[17-plus]
                self.stickers[17-plus], self.stickers[14-plus], self.stickers[11-plus] = self.stickers[18+plus], self.stickers[21+plus], self.stickers[24+plus]
                self.stickers[24+plus], self.stickers[21+plus], self.stickers[18+plus] = temp
                if position == "L":
                    self.x_rotation("CCW", position)
                elif position == "R":
                    self.x_rotation("CW", position)
        elif direction == "D":
            temp = self.stickers[0+plus], self.stickers[3+plus], self.stickers[6+plus]
            self.stickers[0+plus], self.stickers[3+plus], self.stickers[6+plus] = self.stickers[18+plus], self.stickers[21+plus], self.stickers[24+plus]
            self.stickers[18+plus], self.stickers[21+plus], self.stickers[24+plus] = self.stickers[17-plus], self.stickers[14-plus], self.stickers[11-plus]
            self.stickers[11-plus], self.stickers[14-plus], self.stickers[17-plus] = self.stickers[33+plus], self.stickers[30+plus], self.stickers[27+plus]
            self.stickers[27+plus], self.stickers[30+plus], self.stickers[33+plus] = temp
            if position == "L":
                self.x_rotation("CW", position)
            elif position == "R":
                self.x_rotation("CCW", position)
    def x_rotation(self, direction, position):
        if position == "L":
            plus = 0
        elif position == "R":
            plus = 9
        if direction == "CW":
            temp = self.stickers[36+plus]
            self.stickers[36+plus] = self.stickers[42+plus]
            self.stickers[42+plus] = self.stickers[44+plus]
            self.stickers[44+plus] = self.stickers[38+plus]
            self.stickers[38+plus] = temp
            temp = self.stickers[37+plus]
            self.stickers[37+plus] = self.stickers[39+plus]
            self.stickers[39+plus] = self.stickers[43+plus]
            self.stickers[43+plus] = self.stickers[41+plus]
            self.stickers[41+plus] = temp
        elif direction == "CCW":
            temp = self.stickers[36+plus]
            self.stickers[36+plus] = self.stickers[38+plus]
            self.stickers[38+plus] = self.stickers[44+plus]
            self.stickers[44+plus] = self.stickers[42+plus]
            self.stickers[42+plus] = temp
            temp = self.stickers[37+plus]
            self.stickers[37+plus] = self.stickers[41+plus]
            self.stickers[41+plus] = self.stickers[43+plus]
            self.stickers[43+plus] = self.stickers[39+plus]
            self.stickers[39+plus] = temp
    
    def y_movement(self, direction, position):
        if position == "L":
            plus = 0
            plus2 = 0
        elif position == "R":
            plus = 2
            plus2 = 6
        if direction == "U":
            temp = self.stickers[51+plus], self.stickers[48+plus], self.stickers[45+plus]
            self.stickers[51+plus], self.stickers[48+plus], self.stickers[45+plus] = self.stickers[29+plus2], self.stickers[28+plus2], self.stickers[27+plus2]
            self.stickers[29+plus2], self.stickers[28+plus2], self.stickers[27+plus2] = self.stickers[38-plus], self.stickers[41-plus], self.stickers[44-plus]
            self.stickers[38-plus], self.stickers[41-plus], self.stickers[44-plus] = self.stickers[26-plus2], self.stickers[25-plus2], self.stickers[24-plus2]
            self.stickers[26-plus2], self.stickers[25-plus2], self.stickers[24-plus2] = temp
            if position == "L":
                self.y_rotation("CCW", position)
            elif position == "R":
                self.y_rotation("CW", position)
        elif direction == "D":
            temp = self.stickers[45+plus], self.stickers[48+plus], self.stickers[51+plus]
            self.stickers[45+plus], self.stickers[48+plus], self.stickers[51+plus] = self.stickers[24-plus2], self.stickers[25-plus2], self.stickers[26-plus2]
            self.stickers[24-plus2], self.stickers[25-plus2], self.stickers[26-plus2] = self.stickers[44-plus], self.stickers[41-plus], self.stickers[38-plus]
            self.stickers[44-plus], self.stickers[41-plus], self.stickers[38-plus] = self.stickers[29+plus2], self.stickers[28+plus2], self.stickers[27+plus2]
            self.stickers[29+plus2], self.stickers[28+plus2], self.stickers[27+plus2] = temp
            if position == "L":
                self.y_rotation("CW", position)
            elif position == "R":
                self.y_rotation("CCW", position)
    
    def y_rotation(self, direction, position):
        if position == "L":
            plus = 0
        elif position == "R":
            plus = 9
        if direction == "CW":
            temp = self.stickers[0+plus]
            self.stickers[0+plus] = self.stickers[6+plus]
            self.stickers[6+plus] = self.stickers[8+plus]
            self.stickers[8+plus] = self.stickers[2+plus]
            self.stickers[2+plus] = temp
            temp = self.stickers[1+plus]
            self.stickers[1+plus] = self.stickers[3+plus]
            self.stickers[3+plus] = self.stickers[7+plus]
            self.stickers[7+plus] = self.stickers[5+plus]
            self.stickers[5+plus] = temp
        elif direction == "CCW":
            temp = self.stickers[0+plus]
            self.stickers[0+plus] = self.stickers[2+plus]
            self.stickers[2+plus] = self.stickers[8+plus]
            self.stickers[8+plus] = self.stickers[6+plus]
            self.stickers[6+plus] = temp
            temp = self.stickers[1+plus]
            self.stickers[1+plus] = self.stickers[5+plus]
            self.stickers[5+plus] = self.stickers[7+plus]
            self.stickers[7+plus] = self.stickers[3+plus]
            self.stickers[3+plus] = temp
    
    def z_movement(self, direction, position):
        if position == "U":
            plus = 0
            plus2 = 0
        elif position == "D":
            plus = 6
            plus2 = 6
        if direction == "L":
            temp = self.stickers[0+plus], self.stickers[1+plus], self.stickers[2+plus]
            self.stickers[0+plus], self.stickers[1+plus], self.stickers[2+plus] = self.stickers[45+plus2], self.stickers[46+plus2], self.stickers[47+plus2]
            self.stickers[45+plus2], self.stickers[46+plus2], self.stickers[47+plus2] = self.stickers[9+plus], self.stickers[10+plus], self.stickers[11+plus]
            self.stickers[9+plus], self.stickers[10+plus], self.stickers[11+plus] = self.stickers[36+plus], self.stickers[37+plus], self.stickers[38+plus]
            self.stickers[36+plus], self.stickers[37+plus], self.stickers[38+plus] = temp
            if position == "U":
                self.z_rotation("CW", position)
            elif position == "D":
                self.z_rotation("CCW", position)
        elif direction == "R":
            temp = self.stickers[0+plus], self.stickers[1+plus], self.stickers[2+plus]
            self.stickers[0+plus], self.stickers[1+plus], self.stickers[2+plus] = self.stickers[36+plus], self.stickers[37+plus], self.stickers[38+plus]
            self.stickers[36+plus], self.stickers[37+plus], self.stickers[38+plus] = self.stickers[9+plus], self.stickers[10+plus], self.stickers[11+plus]
            self.stickers[9+plus], self.stickers[10+plus], self.stickers[11+plus] = self.stickers[45+plus2], self.stickers[46+plus2], self.stickers[47+plus2]
            self.stickers[45+plus2], self.stickers[46+plus2], self.stickers[47+plus2] = temp
            if position == "U":
                self.z_rotation("CCW", position)
            elif position == "D":
                self.z_rotation("CW", position)
    
    def z_rotation(self, direction, position):
        if position == "U":
            plus = 0
        elif position == "D":
            plus = 9
        if direction == "CW":
            temp = self.stickers[18+plus]
            self.stickers[18+plus] = self.stickers[24+plus]
            self.stickers[24+plus] = self.stickers[26+plus]
            self.stickers[26+plus] = self.stickers[20+plus]
            self.stickers[20+plus] = temp
            temp = self.stickers[19+plus]
            self.stickers[19+plus] = self.stickers[21+plus]
            self.stickers[21+plus] = self.stickers[25+plus]
            self.stickers[25+plus] = self.stickers[23+plus]
            self.stickers[23+plus] = temp
        elif direction == "CCW":
            temp = self.stickers[18+plus]
            self.stickers[18+plus] = self.stickers[20+plus]
            self.stickers[20+plus] = self.stickers[26+plus]
            self.stickers[26+plus] = self.stickers[24+plus]
            self.stickers[24+plus] = temp
            temp = self.stickers[19+plus]
            self.stickers[19+plus] = self.stickers[23+plus]
            self.stickers[23+plus] = self.stickers[25+plus]
            self.stickers[25+plus] = self.stickers[21+plus]
            self.stickers[21+plus] = temp
    
    def count_stickers(self):
        sticker_count = {}
        for sticker in self.stickers:
            if sticker in sticker_count:
                sticker_count[sticker] += 1
            else:
                sticker_count[sticker] = 1
        return sticker_count
    
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
        print("Sticker count:", self.count_stickers())
    
    def random_shuffle(self, movements):
        import random
        for _ in range(movements):
            movement = random.choice(["x","y","z"])
            if movement == "z":
                position = random.choice(["U","D"])
                direction = random.choice(["L","R"])
                self.z_movement(direction, position)
            else:
                position = random.choice(["L","R"])
                direction = random.choice(["U","D"])
            if movement == "x":
                self.x_movement(direction, position)
            elif movement == "y":
                self.y_movement(direction, position)
    
    def list_shuffle(self, movements):
        for movement in movements:
            movement_axis = movement[0]
            movement_direction = movement[1]
            movement_position = movement[2]
            print(movement_axis, movement_direction, movement_position)
            if movement_axis == "z":
                self.z_movement(movement_direction, movement_position)
            elif movement_axis == "x":
                self.x_movement(movement_direction, movement_position)
            elif movement_axis == "y":
                self.y_movement(movement_direction, movement_position)
            self.print_cube()

list_movements = [ ["y", "D", "R"], ["y", "D", "L"], ["x", "D", "L"], ["x", "D", "R"], ["z", "L", "U"], ["z", "R", "D"]]
cube = RubiksCube()
cube.print_cube()
print()
cube.list_shuffle(list_movements)
cube.print_cube()
# cube.x_movement("D","R")
# cube.z_movement("L", "D")
# cube.x_movement("U","R")

# cube.x_movement("U","L")
# cube.x_movement("U","L")
# cube.z_movement("R", "D")
# cube.random_shuffle(1000)
# print()
# cube.print_cube()