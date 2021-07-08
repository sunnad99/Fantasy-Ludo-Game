import pygame

from pygame.sprite import Sprite


class Blank(Sprite):
    def __init__(self, game, column, row):
        
        self.game = game
        Sprite.__init__(self)

        self.blank_color = (-1, -1, -1)
        self.blank_color = self.game.settings.BLACK

        self.image = pygame.Surface((self.game.settings.box_size, self.game.settings.box_size))
        self.image.fill(self.blank_color)
        self.rect = self.image.get_rect()
        

        self.rect.x = column * self.game.settings.box_size
        self.rect.y = row * self.game.settings.box_size


class Path:

    def __init__(self, game, column, row, tile):
        
        self.game = game
        self.settings = self.game.settings
        self.tile = tile

        self.path_color = self.game.settings.WHITE

        self.set_image_for_path()
        self.rect = self.image.get_rect()

        self.rect.x = column * self.game.settings.box_size
        self.rect.y = row * self.game.settings.box_size

    def set_image_for_path(self):
        if self.tile == "!":
            self.image = pygame.image.load(self.settings.ELF_TILE_PATH)

        elif self.tile == ">":
            self.image = pygame.image.load(self.settings.WINNING_YELLOW_PATH)

        elif self.tile == "@":
            self.image = pygame.image.load(self.settings.ORC_TILE_PATH)

        elif self.tile == "v":
            self.image = pygame.image.load(self.settings.WINNING_GREEN_PATH)

        elif self.tile == "&":
            self.image = pygame.image.load(self.settings.DWARF_TILE_PATH)

        elif self.tile == "<":
            self.image = pygame.image.load(self.settings.WINNING_RED_PATH)    

        elif self.tile == "$":
            self.image = pygame.image.load(self.settings.LYCAN_TILE_PATH)

        elif self.tile == "^":
            self.image = pygame.image.load(self.settings.WINNING_BLUE_PATH)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class WinningPath:
    def __init__(self, game, column, row, color, tile):
        
        self.game = game
        self.settings = self.game.settings
        self.tile = tile

        self.winning_path_color = color

        self.set_image_for_path()
        self.rect = self.image.get_rect()

        self.rect.x = column * self.game.settings.box_size
        self.rect.y = row * self.game.settings.box_size
    
    def set_image_for_path(self):
        if self.tile == "y":
            self.image = pygame.image.load(self.settings.WINNING_YELLOW_PATH)

        elif self.tile == "g":
            self.image = pygame.image.load(self.settings.WINNING_GREEN_PATH)

        elif self.tile == "r":
            self.image = pygame.image.load(self.settings.WINNING_RED_PATH)
        
        elif self.tile == "b":
            self.image = pygame.image.load(self.settings.WINNING_BLUE_PATH)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class PlaceHolder:
    
    def __init__(self, game, column, row, color):
        
        self.game = game
        self.settings = self.game.settings

        self.placeholder_path_color = color

        self.image = pygame.Surface((self.settings.box_size, self.settings.box_size))
        self.image.fill(self.placeholder_path_color)
        
        self.rect = self.image.get_rect()

        self.rect.x = column * self.game.settings.box_size
        self.rect.y = row * self.game.settings.box_size


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
        
    
