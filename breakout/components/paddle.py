import pygame

from .sprite import MySprite


class Paddle(MySprite):
    """Represents the game paddle"""

    def __init__(self, width, height, color=(0, 0, 0), **kwargs):
        super().__init__(**kwargs)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        if self.limits:
            self.move_to(
                self.limits.center[0] - self.rect.width / 2,
                self.limits.bottom - self.rect.height,
            )
