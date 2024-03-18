class RubiksCube:
    def __init__(self):
        self.stickers = ['F'] * 9 + ['B'] * 9 + ['U'] * 9 + ['D'] * 9 + ['L'] * 9 + ['R'] * 9

    def print_cube(self):
        print("               ", self.stickers[0:3])
        print("               ", self.stickers[3:6])
        print("               ", self.stickers[6:9])
        print(self.stickers[36:39], self.stickers[9:12], self.stickers[45:48], self.stickers[18:21])
        print(self.stickers[39:42], self.stickers[12:15], self.stickers[48:51], self.stickers[21:24])
        print(self.stickers[42:45], self.stickers[15:18], self.stickers[51:54], self.stickers[24:27])
        print("               ", self.stickers[27:30])
        print("               ", self.stickers[30:33])
        print("               ", self.stickers[33:36])

cube = RubiksCube()
cube.print_cube()