import pygame as pg
from xsettings import Settings
import xgame_functions as gf
from pacman import Pacman
from ghost import Ghost

from xsound import Sound
from xscoreboard import Scoreboard
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman")

        self.sound = Sound(bg_music="sounds/startrek.wav") #change sooundtrack
        self.scoreboard = Scoreboard(game=self)  

    
        
        self.pacman = Pacman(game=self)
        self.ghosts = Ghost(game=self)
        self.settings.initialize_speed_settings()

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.pacman.reset()
        self.ghosts.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        self.sound.play_bg()
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill(self.settings.bg_color)
            self.pacman.update()
            self.ghosts.update()
            self.scoreboard.update()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
