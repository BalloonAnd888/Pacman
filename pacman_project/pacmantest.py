import pygame as pg
from timer import Timer
from character import Character
from game_functions import clamp
import pygame as pg
from vector import Vector
from pygame.sprite import Sprite


class Pacman(Character):
    def __init__(self, game, position):
        super().__init__(position)
        self.screen = game.screen
        self.settings = game.settings

        self.position = position

    def spawn(self):
        pass

    def update(self):
        #self.position += self.vel
        self.draw()

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.position, self.radius)



