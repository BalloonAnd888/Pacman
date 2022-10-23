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

        self.pacman_right = [pg.transform.rotozoom(pg.image.load(f'images/PacmanRight-{n}.png'), 0, 0.5) for n in range(3)]
        self.pacman_left = [pg.transform.rotozoom(pg.image.load(f'images/PacmanLeft-{n}.png'), 0, 0.5) for n in range(3)]
        self.pacman_up = [pg.transform.rotozoom(pg.image.load(f'images/PacmanUp-{n}.png'), 0, 0.5) for n in range(3)]
        self.pacman_down = [pg.transform.rotozoom(pg.image.load(f'images/PacmanDown-{n}.png'), 0, 0.5) for n in range(3)]

        self.timer_normal = Timer(self.pacman_right)
        self.timer = self.timer_normal

        self.wallCollide = False

    def spawn(self):
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = self.screen_rect.centery
        # return Vector(self.rect.left, self.rect.top)
        return Vector(30, 48)

    def checkWallCollision(self): pass
        # for x in self.maze.bricks:
        #     if self.rect.colliderect(x):
        #         print("Hi")




        # collide = pg.sprite.spritecollide(self, self.maze.bricks, False)
        # if collide:
        #     print("True")
        #     self.vel = Vector()

        # for p in pg.sprite.spritecollide(self, self.maze.bricks, False):
        #     if self.rect.right == p.rect.left:
        #         print("Hi")
            # if self.rect.right == p.rect.left:
            #     print("P.Right = B.Left")
            # if self.rect.left == p.rect.right:
            #     print("P.Left = B.Right")
            # if self.rect.top == p.rect.bottom:
            #     print("P.Top = B.Bottom")
            # if self.rect.bottom == p.rect.top:
            #     print("P.Bottom = B.Top")

        # if pg.sprite.collide_rect(self, self.maze.rect):
        #     if self.pacmanMovingLeft:
        #         print('Left')

        # if pg.sprite.collide_rect(self, self.maze.rect):
        #     print("Hi")
        # for p in pg.sprite.spritecollide(self, self.maze.bricks, False):
        #     if self.rect.right == p.rect.left:
        #         print("P.Right = B.Left")
        #     if self.rect.left == p.rect.right:
        #         print("P.Left = B.Right")
        #     if self.rect.top == p.rect.bottom:
        #         print("P.Top = B.Bottom")
        #     if self.rect.bottom == p.rect.top:
        #         print("P.Bottom = B.Top")







        # if pg.sprite.spritecollideany(self, self.maze.bricks):
        #     print("Wall")
        #     self.wallCollide = True
            #return True
        #return pg.sprite.spritecollideany(self, self.maze.bricks)

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



