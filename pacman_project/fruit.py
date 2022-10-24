from block import Block
from random import choice
from pygame import Rect
from pygame.sprite import Sprite


class Fruit(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.image = image