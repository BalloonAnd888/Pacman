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
        self.maze = game.maze

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

        self.pacmanMovedLeft = False
        self.pacmanMovedRight = False
        self.pacmanMovedUp = False
        self.pacmanMovedDown = False

        self.pacman_right = [pg.transform.rotozoom(pg.image.load(f'images/PacmanRight-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_left = [pg.transform.rotozoom(pg.image.load(f'images/PacmanLeft-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_up = [pg.transform.rotozoom(pg.image.load(f'images/PacmanUp-{n}.png'), 0, 1) for n in range(3)]
        self.pacman_down = [pg.transform.rotozoom(pg.image.load(f'images/PacmanDown-{n}.png'), 0, 1) for n in range(3)]

        self.timer_normal = Timer(self.pacman_right)
        self.timer = self.timer_normal

        self.wallCollide = False
        self.moving = False

    def spawn(self):
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        # return Vector(self.rect.left, self.rect.top)
        return Vector(30, 48)

    def collisionX(self): pass

    def collisionY(self): pass

    def checkWallCollision(self):
        if self.pacmanMovingLeft or self.pacmanMovedLeft:
            print("PML")
            collide = pg.sprite.spritecollide(self, self.maze.bricks, False)
            if collide:
                self.rect.x = collide[0].rect.right
                self.vel = Vector()

        if self.pacmanMovingRight or self.pacmanMovedRight:
            print("PMR")
            collide = pg.sprite.spritecollide(self, self.maze.bricks, False)
            if collide:
                self.rect.x = collide[0].rect.left - self.rect.width
                self.vel = Vector()



        # collide = pg.Rect.colliderect(self.rect, self.maze.rect)

        #print(collide)
        # self.wallCollide = False
        # if pg.sprite.spritecollide(self, self.maze.bricks, False):
        #     print("Collide")
        #     if self.pacmanMovedUp is True:
        #         self.pacmanMovedUp = False
        #         self.vel = Vector()
        #         self.wallCollide = True
        #         print("UP")
        #     if self.pacmanMovedDown is True:
        #         self.pacmanMovedDown = False
        #         self.vel = Vector()
        #         print("Down")
        #         self.wallCollide = True
        #     if self.pacmanMovedLeft is True:
        #         self.pacmanMovedLeft = False
        #         self.vel = Vector()
        #         print("Left")
        #         self.wallCollide = True
        #     if self.pacmanMovedRight is True:
        #         self.pacmanMovedRight = False
        #         self.vel = Vector()
        #         print("Right")
        #         self.wallCollide = True

        # self.wallCollide = False
        # if self.pacmanMovedUp is True:
        #     if pg.sprite.spritecollide(self, self.maze.bricks, False):
        #         self.pacmanMovedUp = False
        #         self.vel = Vector()
        #         self.wallCollide = True
        # elif self.pacmanMovedDown is True:
        #     if pg.sprite.spritecollide(self, self.maze.bricks, False):
        #         self.pacmanMovedDown = False
        #         self.vel = Vector()
        #         self.wallCollide = True

        # elif self.pacmanMovedLeft is True:
        #     if pg.sprite.spritecollide(self, self.maze.bricks, False):
        #         self.pacmanMovedLeft = False
        #         self.vel = Vector()
        #         self.wallCollide = True
        # if self.pacmanMovedRight is True:
        #     if pg.sprite.spritecollide(self, self.maze.bricks, False):
        #         self.pacmanMovedRight = False
        #         self.vel = Vector()
        #         self.wallCollide = True

    def update(self):
        if self.pacmanMovingLeft:
            # self.wallCollide = False
            self.timer_normal = Timer(frames=self.pacman_left)
            self.timer = self.timer_normal
            #self.vel = self.settings.pacman_speed_factor * Vector(-1,0)
        if self.pacmanMovingRight:
            # self.wallCollide = False
            self.timer_normal = Timer(frames=self.pacman_right)
            self.timer = self.timer_normal
            # self.vel = self.settings.pacman_speed_factor * Vector(1, 0)
        if self.pacmanMovingUp:
            # self.wallCollide = False
            self.timer_normal = Timer(frames=self.pacman_up)
            self.timer = self.timer_normal
        if self.pacmanMovingDown:
            # self.wallCollide = False
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



