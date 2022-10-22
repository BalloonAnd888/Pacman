from pygame.sprite import Sprite
from vector import Vector


class Character:
    def __init__(self, game, position, color, radius):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.position = position

        self.color = color
        self.radius = radius
        self.vel = Vector(1, 0)




    def spawn(self): pass
    def die(self):pass
    def update(self): pass
    def draw(self): pass