import pygame
from screens import BaseScreen
from components import TextBox


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        """
        Initializes the WelcomeScreen. Extends the BaseScreen class for the 
        parameters *args and **kwargs. Creates a group of sprites to store the 
        TextBox object.
        """
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (300, 100), "Press SPACE", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)

    def draw(self):
        """
        Draws the WelcomeScreen window and button by filling the window with white,
        and setting the button coordinates.
        """
        self.window.fill((255, 255, 255))
        self.button.rect.x = 250
        self.button.rect.y = 400
        self.sprites.draw(self.window)

    def update(self):
        """
        Does nothing.
        """
        pass

    def manage_event(self, event):
        """
        Prints the event and checks if the user presses the spacebar. If they do, 
        the next_screen is changed to game and the running flag is set to false.     
        """
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
