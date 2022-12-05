import pygame
from screens import BaseScreen
from components import TextBox
from ..screens import game


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        """
        Initializes a GameOverScreen object.
        It creates two text boxes with different colors and positions them on the screen.

        Parameters:
        *args (tuple): positional arguments for the super class.
        **kwargs (dict): keyword arguments for the super class.
        """
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (200, 100), "Again", color=(255, 0, 0), bgcolor=(120, 120, 120)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(0, 255, 0), bgcolor=(255, 140, 70)
        )
        self.button1.rect.topleft = (200, 400)
        self.button2.rect.topleft = (500, 400)
        self.sprites.add(self.button1, self.button2)

    def draw(self):
        """
        Draws the game over screen.
        Fills the window with white, draws the text boxes, and then blits the score.
        """
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        #self.window.blit(self.score, (300,300))

    def manage_event(self, event):
        """
        Manages the mouse events.
        When user clicks the Again button, the running flag is set to False and the next_screen is set to "welcome".
        When user clicks the Quit button, the running flag is set to False and the next_screen is set to False.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
