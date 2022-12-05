import pygame
from .sprite import MySprite
import random


class Tile(MySprite):
    """Tile - meant to be hit with the ball"""

    def __init__(self, *args, width=100, height=30, color='green', **kwargs):
        super().__init__(*args, **kwargs)
        self.image = pygame.Surface((width, height))
        self.image.fill([random.randint(100, 200) for _ in range(3)])
        self.rect = self.image.get_rect()
