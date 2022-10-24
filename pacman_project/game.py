import pygame as pg
from settings import Settings
import game_functions as gf

from pacman import Pacman
from maze import Maze
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman")

        self.maze = Maze(self.screen, self.settings, mazefile='images/mazetest.txt')
        self.pacman = Pacman(game=self)

        self.settings.initialize_speed_settings()

    def play(self):
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, pacman=self.pacman)
            self.screen.fill(self.settings.black)
            self.pacman.checkWallCollision()
            self.pacman.update()
            self.maze.update()
            pg.display.update()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

