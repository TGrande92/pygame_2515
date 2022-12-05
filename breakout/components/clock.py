import pygame

class Clock():
    """
    Creates the clock object
    """
    def __init__(self):
        #Creates the clock
        self.clock = pygame.time.Clock()

        #Sets the clock starting time
        self.counter = 20

        #sets the font for the clock
        self.font = pygame.font.SysFont('Consolas', 30)

        #Displays the clock
        self.text = self.font.render(str(self.counter), True, (0, 128, 0))

        #Used to track time to trigger events on the clock
        self.timer_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.timer_event, 1000, loops=10)

    



