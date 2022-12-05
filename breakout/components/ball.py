import pygame
from .sprite import MySprite
import math


class Ball(MySprite):
    """The Ball class - a lot happens here!"""

    def __init__(
        self, width=30, height=30, color=(255, 0, 0), bgcolor=(255, 255, 255), **kwargs
    ):
        super().__init__(**kwargs)
        #This is used for my score
        self.destroyed_tiles = 0

        #This creates a mushroom image ball
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image = pygame.image.load('breakout/components/images/mushroom.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height)) 

        self.speed = 0
        self.angle = 0

        if self.limits:
            self.move_to(self.limits.center[0] - 100, self.limits.bottom - 100)

    def bounce_limits(self):
        """Makes the ball stay within the limits, and bounce from the walls"""
        if self.rect.left < self.limits.left:
            self.rect.x = self.limits.left
            self.angle = math.radians(180) - self.angle

        if self.rect.right > self.limits.right:
            self.rect.x = self.limits.right - self.rect.width
            self.angle = math.radians(180) - self.angle

        if self.rect.top < self.limits.top:
            self.rect.y = self.limits.top
            self.angle = -self.angle

        if self.rect.bottom > self.limits.bottom:
            self.rect.y = self.limits.bottom - self.rect.height
            self.angle = -self.angle

    def bounce_from(self, other):
        """Makes the ball bounce from the `other` object"""
        if self.rect.bottom > other.top or self.rect.top < other.bottom:
            self.angle = -self.angle
        elif self.rect.right > other.left or self.rect.left < other.right:
            self.angle = math.radians(180) - self.angle

    def update(self):
        """Updates the ball position based on its speed"""
        self.rect.x = self.rect.x + self.hspeed
        self.rect.y = self.rect.y + self.vspeed

        self.bounce_limits()

    def collidepaddle(self, other):
        """Convenience method to deal with the event of the ball colliding with the paddle"""
        if self.rect.colliderect(other):
            # We did catch the ball - where did the ball hit relative to the center of the paddle?
            hratio = 2 * (self.rect.center[0] - other.center[0]) / other.width
            # Normalize the hit ratio and calculate the bounce angle based on the max angle = 80 degrees
            self.angle = (hratio - 1) * math.radians(80)
            # Fix the ball location
            self.rect.bottom = other.top - 1
            self.combo = 0
            return True

        # We did not catch the ball - return False
        return False

    def collidetiles(self, tiles):
        """Convenience method to deal with the ball hitting the tiles"""
        collided = pygame.sprite.spritecollide(self, tiles, dokill=True)
        for sprite in collided:
            self.destroyed_tiles = self.destroyed_tiles + 1
            self.bounce_from(sprite.rect)

        return len(collided)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def hspeed(self):
        """The horizontal speed is a dynamic property"""
        return self.speed * math.cos(self._angle)

    @property
    def vspeed(self):
        """The vertical speed is a dynamic property"""
        return self.speed * math.sin(self._angle)
