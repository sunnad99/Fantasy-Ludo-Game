import pygame

from tile import *

class Board:

    def __init__(self,game):

        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.initialize_board_vars()



    def load_board(self):
        
        for row, tiles in enumerate(self.settings.grid_data):
            for col, tile in enumerate(tiles):
                if tile == "!" or tile == "@" or tile == "&" or tile == "$" or tile == ">" or tile == "<" or tile == "^" or tile =="v":
                    self.movement_path_sprites.append(Path(self.game, col, row, tile))
                elif tile == "X":
                    self.blank_sprites.add(Blank(self.game, col, row))
                elif tile == "F" or tile == "A" or tile == "J" or tile == "S":
                    self.placeholder_chooser(col, row, tile)
                elif tile == "r" or tile == "b" or tile == "g" or tile == "y":
                    self.winning_path_chooser(col, row, tile)
    
    def load_board_features(self):

        self.gridlines = pygame.image.load(self.settings.GRID_AND_BORDERS_PATH)
        self.base_background = pygame.image.load(self.settings.BASE_BACKGROUND_PATH)
        self.dungeon = pygame.image.load(self.settings.DUNGEON_PATH)
           
    def placeholder_chooser(self, col, row, tile):
        "Chooses the proper placeholder for the respective tiles in the grid and also creates a copy (for drawing!)"
        if tile == "A":
            red_placeholder = PlaceHolder(self.game, col, row, self.settings.LIGHT_RED)
            self.red_placeholder_path_sprites.append(red_placeholder)
            self.red_placeholder_path_sprites_copy.append(red_placeholder)

        elif tile == "F":
            green_placeholder = PlaceHolder(self.game, col, row, self.settings.LIGHT_GREEN)
            self.green_placeholder_path_sprites.append(green_placeholder)
            self.green_placeholder_path_sprites_copy.append(green_placeholder)

        elif tile == "S":
            blue_placeholder = PlaceHolder(self.game, col, row, self.settings.LIGHT_BLUE)
            self.blue_placeholder_path_sprites.append(blue_placeholder)
            self.blue_placeholder_path_sprites_copy.append(blue_placeholder)

        elif tile == "J":
            yellow_placeholder = PlaceHolder(self.game, col, row, self.settings.LIGHT_YELLOW)
            self.yellow_placeholder_path_sprites.append(yellow_placeholder)
            self.yellow_placeholder_path_sprites_copy.append(yellow_placeholder)

    def winning_path_chooser(self, col, row, tile):
        if tile == "r":
            self.red_winning_path_sprites.append(WinningPath(self.game, col, row, self.settings.LIGHT_RED, tile))

        elif tile == "g":
            self.green_winning_path_sprites.append(WinningPath(self.game, col, row, self.settings.LIGHT_GREEN, tile))

        elif tile == "b":
            self.blue_winning_path_sprites.append(WinningPath(self.game, col, row, self.settings.LIGHT_BLUE, tile))

        elif tile == "y":
            self.yellow_winning_path_sprites.append(WinningPath(self.game, col, row, self.settings.LIGHT_YELLOW, tile))

    def initialize_board_vars(self):
        self.total_tokens = 0

        self.movement_path_sprites = []

        self.red_winning_path_sprites = []
        self.green_winning_path_sprites = []
        self.blue_winning_path_sprites = []
        self.yellow_winning_path_sprites = []

        self.red_placeholder_path_sprites = []
        self.green_placeholder_path_sprites = []
        self.blue_placeholder_path_sprites = []
        self.yellow_placeholder_path_sprites = []

        self.red_placeholder_path_sprites_copy = []
        self.green_placeholder_path_sprites_copy = []
        self.blue_placeholder_path_sprites_copy = []
        self.yellow_placeholder_path_sprites_copy = []

        self.blank_sprites = pygame.sprite.Group()
        
    def draw_path_tiles(self, surface):
        
        for path_object in self.movement_path_sprites:
            path_object.draw(surface)

    def draw_placeholder_path_tiles(self, surface):

        for red_placeholder_path_object in self.red_placeholder_path_sprites_copy:
            red_placeholder_path_object.draw(surface)

        for blue_placeholder_path_object in self.blue_placeholder_path_sprites_copy:
            blue_placeholder_path_object.draw(surface)
        
        for green_placeholder_path_object in self.green_placeholder_path_sprites_copy:
            green_placeholder_path_object.draw(surface)
        
        for yellow_placeholder_path_object in self.yellow_placeholder_path_sprites_copy:
            yellow_placeholder_path_object.draw(surface)

    def draw_winning_path_tiles(self, surface):

        for red_winning_path_object in self.red_winning_path_sprites:
            red_winning_path_object.draw(surface)

        for blue_winning_path_object in self.blue_winning_path_sprites:
            blue_winning_path_object.draw(surface)
        
        for green_winning_path_object in self.green_winning_path_sprites:
            green_winning_path_object.draw(surface)
        
        for yellow_winning_path_object in self.yellow_winning_path_sprites:
            yellow_winning_path_object.draw(surface)

    def check_tokens_in_base(self):
        base_token_counter = 0
        if self.game.dice.dice_val < 6:
            # We run a for loop here to prevent taking a turn if dice val is less than 6 while all the tokens are in the base
            self.total_tokens = len(self.game.player.current_player_token_group)
            for token_index in range(self.total_tokens):

                current_token = self.game.player.current_player_token_group[token_index]
                current_placeholder = self.game.player.current_player_placeholder_group[token_index]
                
                if current_token.rect.x == current_placeholder.rect.x and current_token.rect.y == current_placeholder.rect.y:
                    base_token_counter += 1

            return base_token_counter
    
            