import random
import pygame
from screens import BaseScreen
import json
import requests

from ..components import Paddle, Ball, TileGroup, Clock, Score
from components import TextBox

FLASK_URL = "http://127.0.0.1:5000"

class GameScreen(BaseScreen):
    """
    This class initializes the game screen and creates the paddle, ball, tiles, sprite group, 
    countdown clock, and score. It also updates the image for paddle movement, the score text 
    for every collided tile, and the best score if the combo is greater than the previous one. 
    The draw method is used to populate all of the images on the screen. The manage_event method 
    is used to handle events such as the mouse button being pressed, the space bar being pressed, 
    and the quit event.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the paddle
        self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8
        self.ball.angle = -1.5

        # Create the tiles
        self.tiles = TileGroup()

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)

        # Create a countdown clock
        self.clock = Clock()
        
        # Creates the score
        self.score = Score()

        #Sets the best score to 0
        self.best_score = 0

    def update(self):
        #updates the image for paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        self.sprites.update()

        #This was here to begin with and i'm afraid to remove it
        collided = self.ball.collidetiles(self.tiles)

        #Updates the score text for every collided tile
        self.score.score = self.ball.destroyed_tiles
        self.score.text = self.score.font.render(str(self.score.score), True, (0, 128, 0))

        
        #Resets the combo to 0 if the ball hits the paddle
        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)
        if caught_the_ball:
            self.ball.destroyed_tiles = 0
            self.score.score = 0
        
        #Keeps the best combo if the combo is greater than the previous one
        if self.score.score > self.best_score:
            self.best_score = self.score.score

        #Game over if the ball goes below the paddle
        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            r = requests.post(FLASK_URL + "/add_score", json={"Score": self.best_score})
            self.running = False
            self.next_screen = "game_over"

        #Game over if the clock reaches 0 and then sends a flask request
        if self.clock.counter == 0:
            r = requests.post(FLASK_URL + "/add_score", json={"Score": self.best_score})
            self.next_screen = "game_over"
            self.running = False
            pygame.time.set_timer(self.clock.timer_event, 0)
        
    def draw(self):
        """During the game this method is used to populate all of the images on the screen"""
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)
        self.window.blit(self.clock.text, (500,500))
        self.window.blit(self.score.text, (300,500))


    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = -1.5
        if event.type == pygame.QUIT:
            run = False

        elif event.type == self.clock.timer_event:
            self.clock.counter -= 1
            self.clock.text = self.clock.font.render(str(self.clock.counter), True, (0, 128, 0))