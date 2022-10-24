import sys
import pygame as pg
from vector import Vector


# class GameFunction:
#     def __init__(self):
#         pass

movement = {pg.K_LEFT: Vector(-1, 0),   # dictionary to map keys to Vector velocities
            pg.K_RIGHT: Vector(1, 0),
            pg.K_UP: Vector(0, -1),
            pg.K_DOWN: Vector(0, 1)
            }


def check_keydown_events(event, settings, pacman):
    key = event.key
    if key in movement.keys():
        if key == pg.K_LEFT:
            pacman.wallCollide = False
            pacman.moving = True
            pacman.pacmanMovingLeft = True
            pacman.pacmanMovingRight = False
            pacman.pacmanMovingUp = False
            pacman.pacmanMovingDown = False
            if not pacman.wallCollide:
                pacman.vel = settings.pacman_speed_factor * movement[key]

        if key == pg.K_RIGHT:
            pacman.wallCollide = False
            pacman.moving = True
            pacman.pacmanMovingLeft = False
            pacman.pacmanMovingRight = True
            pacman.pacmanMovingUp = False
            pacman.pacmanMovingDown = False
            if not pacman.wallCollide:
                pacman.vel = settings.pacman_speed_factor * movement[key]

        if key == pg.K_UP:
            pacman.wallCollide = False
            pacman.pacmanMovingLeft = False
            pacman.moving = True
            pacman.pacmanMovingRight = False
            pacman.pacmanMovingUp = True
            pacman.pacmanMovingDown = False
            if not pacman.wallCollide:
                pacman.vel = settings.pacman_speed_factor * movement[key]

        if key == pg.K_DOWN:
            pacman.wallCollide = False
            pacman.pacmanMovingLeft = False
            pacman.moving = True
            pacman.pacmanMovingRight = False
            pacman.pacmanMovingUp = False
            pacman.pacmanMovingDown = True
            if not pacman.wallCollide:
                pacman.vel = settings.pacman_speed_factor * movement[key]

def check_keyup_events(event, pacman):
    key = event.key
    if key == pg.K_ESCAPE:
        pacman.vel = Vector()   # Note: Escape key stops the ship
    # if key == pg.K_LEFT:
    #     if pacman.checkWallCollision():
    #         pacman.pacmanMovingLeft = False
    #         pacman.vel = Vector()
    #         print("CLF")
    #     else:
    #         pacman.pacmanMovingLeft = False
    #         print("LF")
    # if key == pg.K_RIGHT:
    #     pacman.pacmanMovingRight = False
    # if key == pg.K_UP:
    #     pacman.pacmanMovingUp = False
    # if key == pg.K_DOWN:
    #     pacman.pacmanMovingDown = False

    if key == pg.K_LEFT:
        pacman.pacmanMovingLeft = False
        pacman.pacmanMovedLeft = True
        pacman.pacmanMovedRight = False
        pacman.pacmanMovedUp = False
        pacman.pacmanMovedDown = False
        # pacman.vel = Vector()
        #print("KUL")
    if key == pg.K_RIGHT:
        pacman.pacmanMovingRight = False
        pacman.pacmanMovedRight = True
        pacman.pacmanMovedLeft = False
        pacman.pacmanMovedUp = False
        pacman.pacmanMovedDown = False
        # pacman.vel = Vector()
    if key == pg.K_UP:
        pacman.pacmanMovingUp = False
        pacman.pacmanMovedUp = True
        pacman.pacmanMovedLeft = False
        pacman.pacmanMovedRight = False
        pacman.pacmanMovedDown = False
        #pacman.vel = Vector()
    if key == pg.K_DOWN:
        pacman.pacmanMovingDown = False
        pacman.pacmanMovedDown = True
        pacman.pacmanMovedLeft = False
        pacman.pacmanMovedRight = False
        pacman.pacmanMovedUp = False
        #pacman.vel = Vector()


def check_events(settings, pacman):
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN: check_keydown_events(event=event, settings=settings, pacman=pacman)
        elif event.type == pg.KEYUP:
            check_keyup_events(event=event, pacman=pacman)


def clamp(posn, rect, settings):
    left, top = posn.x, posn.y
    width, height = rect.width, rect.height
    left = max(0, min(left, settings.screen_width - width))
    top = max(0, min(top, settings.screen_height - height))
    return Vector(x=left, y=top), pg.Rect(left, top, width, height)
