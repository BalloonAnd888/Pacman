import pygame as pg
from timer import Timer
from character import Character
from game_functions import clamp
import pygame as pg
from vector import Vector
from pygame.sprite import Sprite
from timer import Timer


class Pacman(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pg.image.load('images/PacmanRight-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        self.position = self.spawn()
        self.color = self.settings.yellow
        self.radius = 10
        self.vel = Vector()

        self.pacmanMovingLeft = False
        self.pacmanMovingRight = False
        self.pacmanMovingUp = False
        self.pacmanMovingDown = False

        self.pacman_right = [pg.transform.rotozoom(pg.image.load(f'images/PacmanRight-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_left = [pg.transform.rotozoom(pg.image.load(f'images/PacmanLeft-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_up = [pg.transform.rotozoom(pg.image.load(f'images/PacmanUp-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_down = [pg.transform.rotozoom(pg.image.load(f'images/PacmanDown-{n}.png'), 0, 1) for n in range(3)]

        self.timer_normal = Timer(self.pacman_right)
        self.timer = self.timer_normal

    def spawn(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        return Vector(self.rect.left, self.rect.top)

    def update(self):
        if self.pacmanMovingLeft:
            self.timer_normal = Timer(frames=self.pacman_left)
            self.timer = self.timer_normal
        if self.pacmanMovingRight:
            self.timer_normal = Timer(frames=self.pacman_right)
            self.timer = self.timer_normal
        if self.pacmanMovingUp:
            self.timer_normal = Timer(frames=self.pacman_up)
            self.timer = self.timer_normal
        if self.pacmanMovingDown:
            self.timer_normal = Timer(frames=self.pacman_down)
            self.timer = self.timer_normal
        self.position += self.vel
        self.position, self.rect = clamp(self.position, self.rect, self.settings)
        self.draw()

    def draw(self):
        image = self.timer.imagerect()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)



