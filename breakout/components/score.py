import pygame

class Score():
    def __init__(self, score=0):
        """
        Creates the score object
        """
        #Sets the font for the score
        self.font = pygame.font.SysFont('Consolas', 30)

        #Sets the starting score to 0
        self.score = score

        #Displays the score
        self.text = self.font.render(str(self.score), True, (0, 128, 0))

    