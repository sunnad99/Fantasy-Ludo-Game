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

        self.menu = Menu(self)
        self.player = Player(self)
        self.board = Board(self)
        self.events = Events(self)
        self.dice = Dice(self)

    

    def initialize(self):

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                self.events.check_mouse_main_menu_event(event.type)
                self.events.check_mouse_second_menu_event(event.type)
                self.events.check_mouse_third_menu_event(event.type)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.events.check_mouse_main_menu_event(event.type)
                self.events.check_mouse_second_menu_event(event.type)
                self.events.check_mouse_third_menu_event(event.type)    
                
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.events.check_keyboard_board_menu_event()
                    self.events.check_keyboard_final_menu_event()
                            
    def draw_sprites(self):
        
        self.board.draw_path_tiles(self.screen)
        self.board.draw_winning_path_tiles(self.screen)

        self.board.blank_sprites.draw(self.screen)
        
        # Draw the base backgrounds
        self.screen.blit(self.board.base_background, self.settings.base_background_coordinates)
        self.board.draw_placeholder_path_tiles(self.screen)

        # Draw the borders
        self.screen.blit(self.board.gridlines, self.settings.grid_and_borders_coordinates)

        # Draw the dungeon
        self.screen.blit(self.board.dungeon, self.settings.dungeon_coordinates)
        self.player.draw_tokens_on_board(self.screen)
        
    def run_game(self):
        while True:

            self.screen.fill(self.settings.board_menu_bg_color)
            self.player.show_current_player()

            self._check_events()
            

            # Draw all the objects onto their respective places
            self.draw_sprites()

            # Update window with new sprite positions of the objects
            pygame.display.flip()         
    
        

ludo_game = Ludo()
ludo_game.initialize()
ludo_game.run_game()