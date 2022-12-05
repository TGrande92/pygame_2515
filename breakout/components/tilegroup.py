import pygame
from .tile import Tile


class TileGroup(pygame.sprite.Group):
    def __init__(self, stage="breakout/components/stages/stage1.txt"):
        """
        Initializes the tile group object. 
        """
        super().__init__()
        # Sets default stage to stage 1
        self.stage = stage
        self.tilex = 0
        self.tiley = 0

        # Reads tile data from .txt file
        with open(self.stage, "r") as file:
            layout = file.read()

        # Creates a layout, _ for spaces, x for tiles, and E for next line of tiles
        for letter in layout:
            if letter == '_':
                self.tilex = self.tilex + 52.5
            if letter == 'x':
                self.add(self.create_tile())
                self.tilex = self.tilex + 52.5
            if letter == 'E':
                self.tiley = self.tiley + 32.5
                self.tilex = 0

    def create_tile(self, tile_width=50, tile_height=30):
        """
        Creates a tile object. 
        """
        tile = Tile(width=tile_width, height=tile_height)
        tile.move_to(self.tilex, self.tiley)
        return tile