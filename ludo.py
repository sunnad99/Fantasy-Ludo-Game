import pygame
import sys

from settings import Settings
from board import Board
from dice import Dice
from player import Player
from menu import Menu
from events import Events


class Ludo:

    def __init__(self):

        pygame.init()

        self.settings = Settings(self)

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        
        pygame.display.set_caption("Ludo")

        self.menu = Menu(self) # Initializes the menu class that takes care of drawing all the menus of the game
        self.player = Player(self) # Initializes the player class that takes care of all the actions that a player can do
        self.board = Board(self) # Intiailizes the board class that takes care of all the entities on the board (tiles, placeholders, path highlighting)
        self.events = Events(self) # Intiailizes the event class that takes care of all the actions dealt with the inputs to the game
        self.dice = Dice(self)

    

    def initialize(self):
        "Initializes all the game elements before it starts"

        self.settings.load_data()
        self.board.load_board()
        self.board.load_board_features()

        self.menu.initialize_main_menu()
        self.menu.initialize_third_menu()
        self.menu.initialize_final_menu()
        
        self.menu.main_menu()
        self.menu.second_menu()
        self.menu.third_menu()

        self.player.initialize_players()
        
    def _check_events(self):
        "General function for handling of all inputs."

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                self.events.check_mouse_main_menu_event(event.type)
                self.events.check_mouse_second_menu_event(event.type)
                self.events.check_mouse_third_menu_event(event.type)
                self.events.check_mouse_board_menu_event(event.type)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.events.check_mouse_main_menu_event(event.type)
                self.events.check_mouse_second_menu_event(event.type)
                self.events.check_mouse_third_menu_event(event.type)
                self.events.check_mouse_board_menu_event(event.type)    
                
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.events.check_keyboard_final_menu_event()
                            
    def draw_sprites(self):
        "General function for drawing all sprites onto the screen."

        # Draws all the path tiles (movement and winning path tiles)
        self.board.draw_path_tiles(self.screen)
        self.board.draw_winning_path_tiles(self.screen)

        # Draws all blank sprites where tokens can't go
        self.board.blank_sprites.draw(self.screen)
        
        # Draw the base backgrounds
        self.screen.blit(self.board.base_background, self.settings.base_background_coordinates)
        self.board.draw_placeholder_path_tiles(self.screen)

        # Draw all the tokens
        self.player.draw_tokens_on_board(self.screen)

        # Draws any path highlights for tokens
        self.board.draw_path_highlights(self.screen)
        
        # Draw the borders
        self.screen.blit(self.board.gridlines, self.settings.grid_and_borders_coordinates)

        # Draw the dungeon
        self.screen.blit(self.board.dungeon, self.settings.dungeon_coordinates)
        
        
    def run_game(self):
        while True:

            self.screen.fill(self.settings.board_menu_bg_color)

            # Displays all the buttons on the screen
            self.menu.show_buttons_on_board_menu()

            # Checks all the inputs for making a move on the board menu
            self._check_events()
            
            # Draw all the objects onto their respective places
            self.draw_sprites()
            
            # Update window with new sprite positions of the objects
            pygame.display.flip()         
    
