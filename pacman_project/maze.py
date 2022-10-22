import pygame as pg

# list of nodes
# maze = [
#     "|--------|",
#     "|G..|..G.|",
#     "|...PP...|",
#     "|G...@.|.|",
#     "|........|",
#     "|--------|"
# ]

# 01111111111111011111111111110
# 01000010000001010000010000010
# 01000010000001010000010000010
# 01111111111111111111111111110
# 01000010010000000010010000010
# 01000010010000000010010000010
# 01111110011111011110011111110
# 00000010000001010000010000000
#      010011111111110010
#      010011111111110010
#      010010000000010010
# 00000011110000000011110000000
# 11111111110000000011111111111
# 00000010010000000010010000000
#      010011111111110010
#      010011111111110010
#      010010000000010010
# 00000011110000000010010000000
# 01111111111110011111111111110
# 01000010000010010000010000010
# 01000010000010010000010000010
# 01110011111111111111110011110
#   010010010000000010010010
# 01111110011110111110011111110
# 01000000000010100000000000010
# 01000000000010100000000000010
# 01111111111111111111111111110


class Maze:
    def __init__(self, screen, settings, mazefile):
        self.pacman_pos = (200, 400)
        self.screen = screen
        self.settings = settings
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.brick = pg.image.load('images/Block.png')
        self.brick = pg.transform.scale(self.brick, (16, 16))
        self.rect = self.brick.get_rect()

        self.build()

    def build(self):
        b = self.brick.get_rect()
        bw, bh = b.width, b.height

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pg.Rect(ncol, nrow, bw, bh))
    def wall_collide(self): pass


    def draw(self):
        for rect in self.bricks:
            self.screen.blit(self.brick, rect)

    def update(self):
        self.draw()






