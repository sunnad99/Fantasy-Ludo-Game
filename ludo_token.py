import pygame

class LudoToken:

    def __init__(self, game, color, x, y):

        self.game = game
        self.settings = self.game.settings


        self.color_chooser(color)
            
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def color_chooser(self, color):
        if color == "red":
            self.image = pygame.image.load(self.settings.RED_TOKEN_PATH).convert()

        elif color == "green":
            self.image = pygame.image.load(self.settings.GREEN_TOKEN_PATH).convert()

        elif color == "blue":
            self.image = pygame.image.load(self.settings.BLUE_TOKEN_PATH).convert()

        elif color == "yellow":
            self.image = pygame.image.load(self.settings.YELLOW_TOKEN_PATH).convert()
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)        
    

        
        