import pygame
import time
import sys

class Events:

    def __init__(self, game):
        self.game = game
        self.settings = self.game.settings


    def check_mouse_main_menu_event(self, event_type):
        if event_type == pygame.MOUSEMOTION and self.game.menu.is_main_menu:

            self.mouse_pos = pygame.mouse.get_pos()

            if self.game.menu.start_game.collidepoint(self.mouse_pos):
                self.game.menu.start_game_color = self.settings.DARK_RED

            else:
                self.game.menu.start_game_color = self.settings.WHITE
            
            if self.game.menu.exit_game.collidepoint(self.mouse_pos):
                self.game.menu.exit_game_color = self.settings.DARK_RED

            else:
                self.game.menu.exit_game_color = self.settings.WHITE

        elif event_type == pygame.MOUSEBUTTONDOWN and self.game.menu.is_main_menu:

            state_of_buttons = pygame.mouse.get_pressed()

            if state_of_buttons[0] == 1 and self.game.menu.start_game.collidepoint(self.mouse_pos):
                self.game.menu.is_main_menu = False

            if state_of_buttons[0] == 1 and self.game.menu.exit_game.collidepoint(self.mouse_pos):
                sys.exit()

    def check_mouse_second_menu_event(self,event_type):
        if event_type == pygame.MOUSEMOTION and self.game.menu.is_2nd_menu:

            self.mouse_pos = pygame.mouse.get_pos()
            if self.game.menu.player_2.collidepoint(self.mouse_pos):
                self.game.menu.two_player_color = self.settings.DARK_RED             
            else:
                self.game.menu.two_player_color = self.settings.BLACK
            
            if self.game.menu.player_3.collidepoint(self.mouse_pos):
                self.game.menu.three_player_color = self.settings.DARK_RED
            else:
                self.game.menu.three_player_color = self.settings.BLACK

            if self.game.menu.player_4.collidepoint(self.mouse_pos):
                self.game.menu.four_player_color = self.settings.DARK_RED
            else:
                self.game.menu.four_player_color = self.settings.BLACK

        elif event_type == pygame.MOUSEBUTTONDOWN and self.game.menu.is_2nd_menu:
            state_of_buttons = pygame.mouse.get_pressed()

            if state_of_buttons[0] == 1 and self.game.menu.player_2.collidepoint(self.mouse_pos):
                self.game.menu.is_2nd_menu = False
                self.game.player.no_of_players = 2
            if state_of_buttons[0] == 1 and self.game.menu.player_3.collidepoint(self.mouse_pos):
                self.game.menu.is_2nd_menu = False
                self.game.player.no_of_players = 3
            if state_of_buttons[0] == 1 and self.game.menu.player_4.collidepoint(self.mouse_pos):
                self.game.menu.is_2nd_menu = False
                self.game.player.no_of_players = 4
    
    def check_mouse_third_menu_event(self, event_type):
        if event_type == pygame.MOUSEMOTION and self.game.menu.is_3rd_menu:
            self.mouse_pos = pygame.mouse.get_pos()
            
            if self.game.menu.dwarf_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_red:
                self.game.menu.dwarf_surface.set_alpha(100)
                self.game.menu.player_text = f"Select dwarf for player {self.game.player.current_player}"
                
            elif self.game.menu.selected_red:
                self.game.menu.dwarf_surface.set_alpha(255)
            
                
            if self.game.menu.orc_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_green:
                self.game.menu.orc_surface.set_alpha(100)
                self.game.menu.player_text = f"Select orc for player {self.game.player.current_player}"

            elif self.game.menu.selected_green:
                self.game.menu.orc_surface.set_alpha(255)
                
                
            
            if self.game.menu.lycan_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_blue:

                self.game.menu.lycan_surface.set_alpha(100)
                self.game.menu.player_text = f"Select lycan for player {self.game.player.current_player}"

            elif self.game.menu.selected_blue:
                self.game.menu.lycan_surface.set_alpha(255)
                
                
            if self.game.menu.elf_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_yellow:

                self.game.menu.elf_surface.set_alpha(100)
                self.game.menu.player_text = f"Select elf for player {self.game.player.current_player}"

            elif self.game.menu.selected_yellow:
                self.game.menu.elf_surface.set_alpha(255)
                
                
        elif event_type == pygame.MOUSEBUTTONDOWN and self.game.menu.is_3rd_menu:

            state_of_buttons = pygame.mouse.get_pressed()

            
            if state_of_buttons[0] == 1 and self.game.menu.dwarf_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_red:
                self.game.menu.dwarf_surface.set_alpha(0)
                self.game.player.color_for_player[self.game.menu.counter] = "red"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_red = False
            

            if state_of_buttons[0] == 1 and self.game.menu.orc_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_green:
                self.game.menu.orc_surface.set_alpha(0)
                self.game.player.color_for_player[self.game.menu.counter] = "green"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_green = False

            if state_of_buttons[0] == 1 and self.game.menu.lycan_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_blue:
                self.game.menu.lycan_surface.set_alpha(0)
                self.game.player.color_for_player[self.game.menu.counter] = "blue"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_blue = False

            if state_of_buttons[0] == 1 and self.game.menu.elf_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_yellow:
                self.game.menu.elf_surface.set_alpha(0)
                self.game.player.color_for_player[self.game.menu.counter] = "yellow"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_yellow = False

    def check_mouse_board_menu_event(self, event_type):
        "Uses buttons on the screen to play the game."

        if event_type == pygame.MOUSEMOTION and self.game.menu.is_board_menu:
            self.mouse_pos = pygame.mouse.get_pos()

            if not self.game.menu.is_turn_skip:

                if self.game.menu.rtd_button.collidepoint(self.mouse_pos):

                    self.game.menu.roll_the_dice_button_color = self.settings.DARK_RED
                else:
                    
                    self.game.menu.roll_the_dice_button_color = self.settings.WHITE
            else:

                if self.game.menu.okay_button.collidepoint(self.mouse_pos):

                    self.game.menu.okay_button_color = self.settings.DARK_RED
                else:

                    self.game.menu.okay_button_color = self.settings.WHITE
       
        
        elif event_type == pygame.MOUSEBUTTONDOWN and self.game.menu.is_board_menu:
            state_of_buttons = pygame.mouse.get_pressed()

            if state_of_buttons[0] == 1 and self.game.menu.rtd_button.collidepoint(self.mouse_pos) and not self.game.menu.is_turn_skip:
                
                self.game.dice.roll_dice()
                self.game.dice.show_dice()
                self.game.dice.dice_reset()
            
            elif state_of_buttons[0] == 1 and self.game.menu.okay_button.collidepoint(self.mouse_pos):
                    self.game.menu.skipped_turn_text = ""
                    self.game.menu.okay_button_color = self.settings.WHITE
                    self.game.menu.is_turn_skip = False
        
    def choose_token_on_board_mouse_event(self):
        "Lets you carry out an action on a token based on which one is chosen."

        self.mouse_pos = pygame.mouse.get_pos()
        state_of_buttons = pygame.mouse.get_pressed()
        
        token_checker = 0
        for self.token_selector, self.ludo_token in enumerate(self.game.player.current_player_token_group):

            # This if condition is just to make sure the same dice value doesn't act on multiple tokens on the same spot
            if token_checker == 1:
                break

            # checking to see if token is clicked on
            if self.ludo_token.rect.collidepoint(self.mouse_pos) and state_of_buttons[0] == 1:
                
                self.placeholder_sprite = self.game.player.current_player_placeholder_group[self.token_selector]
                
                # This if statement checks if you clicked a token which is placed onto a placeholder (and only puts the token onto a starting tile)
                if self.ludo_token.rect.x == self.placeholder_sprite.rect.x and self.ludo_token.rect.y == self.placeholder_sprite.rect.y:
                    
                    if self.game.dice.dice_val < 6:

                        self.settings.draw_text("Sorry you cannot choose this token!", self.settings.MAIN_MENU_FONT_PATH, 20, self.settings.BLACK, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n", True)
                        self.game.dice.current_turn = False
                    else:

                        self.game.player.current_player_on_start_path()
                        self.settings.draw_text(f"Player {self.game.player.current_player} chose their {self.token_selector + 1} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n", True)

                # This else statement controls the movement for the tiles on the path (movement and winning tiles)
                else:
                    self.movement_checker = self.game.dice.dice_val + self.game.player.token_movement_counter[self.game.player.current_player_color][self.token_selector]
                    
                    if self.movement_checker < self.settings.total_movement_steps: # Move on the movement tiles if the winning tiles aren't reached

                        self.game.player.move_on_normal_path()
                        self.settings.draw_text(f"Player {self.game.player.current_player} chose their {self.game.player.current_player_color} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n", True)  
                        
                    else:

                        self.game.player.move_on_winning_path()
                        self.settings.draw_text(f"Player {self.game.player.current_player} chose their {self.game.player.current_player_color} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n", True) 
                
                    token_checker += 1  

                self.game.board.draw_on_tiles = False # To ensure the highlighted tiles don't remain highlighted after turn has completed
                
                self.game.draw_sprites()
                pygame.display.flip()
                time.sleep(1)
                self.game.dice.current_turn = False # To end the turn for the current player
                
    def highlight_token_on_board_mouse_event(self):
        "This function takes care of all the path highlights based on the token that was hovered over."

        self.mouse_pos = pygame.mouse.get_pos()
        for token_selector, ludo_token in enumerate(self.game.player.current_player_token_group):
            
            placeholder_sprite = self.game.player.current_player_placeholder_group[token_selector]
            if not (ludo_token.rect.x == placeholder_sprite.rect.x and ludo_token.rect.y == placeholder_sprite.rect.y):
   
                if ludo_token.rect.collidepoint(self.mouse_pos): # the mouse is hovering over the ludo token that is on the board and not in the base
                    
                    current_token_position = self.game.player.token_movement_counter[self.game.player.current_player_color][token_selector] + 1 # we take the current token position and to exclude it, we add 1 to it
                    move_val = current_token_position + self.game.dice.dice_val # determines all the sprites that are to be highlighted

                    
                    movement_path_indices = self.settings.total_movement_steps - current_token_position if current_token_position < self.settings.total_movement_steps else 0
                    winning_path_indices = move_val - self.settings.total_movement_steps if move_val > self.settings.total_movement_steps else 0

                    
                    if movement_path_indices != 0 and winning_path_indices !=0: # This situation arises if a dice val arrives such that the tiles to move on include both the movement as well as the winning path tiles
                        
                        movement_path_indices_of_tiles_to_highlight = self.game.player.team_path[self.game.player.current_player_color][current_token_position:current_token_position + movement_path_indices]
                        winning_path_indices_of_tiles_to_highlight = self.game.player.winning_path[self.game.player.current_player_color][:winning_path_indices]

                        self.game.board.path_highlight_sprites = [self.game.board.movement_path_sprites[indice] for indice in movement_path_indices_of_tiles_to_highlight]
                        self.game.board.path_highlight_sprites += [self.game.board.winning_path_dict[self.game.player.current_player_color][indice] for indice in winning_path_indices_of_tiles_to_highlight]

                    
                    elif movement_path_indices != 0: # Highlights only the movement path tiles
                        
                        movement_path_indices_of_tiles_to_highlight = self.game.player.team_path[self.game.player.current_player_color][current_token_position:move_val]
                        
                        self.game.board.path_highlight_sprites = [self.game.board.movement_path_sprites[indice] for indice in movement_path_indices_of_tiles_to_highlight]
                        
                    
                    elif winning_path_indices != 0: # Highlights only the winning path tiles
                        current_winning_path_position = current_token_position - self.settings.total_movement_steps # Current position of token on winning path
                        winning_move_val = (current_token_position + self.game.dice.dice_val) - self.settings.total_movement_steps
                        
                        
                        if not winning_move_val > (self.settings.winning_path_threshold - self.settings.total_movement_steps + 1): # The 1 added to the winning path threshold is just to ensure the last token gets highlighted given the dice value isnt too large
                            winning_path_indices_of_tiles_to_highlight = self.game.player.winning_path[self.game.player.current_player_color][current_winning_path_position:winning_move_val]
                            self.game.board.path_highlight_sprites = [self.game.board.winning_path_dict[self.game.player.current_player_color][indice] for indice in winning_path_indices_of_tiles_to_highlight]
                        else:
                            self.game.board.path_highlight_sprites = [] # This statement is just to ensure the tiles don't highlight on winning path if it goes beyond the winning path tiles
                            self.game.board.draw_on_tiles = False
                            
                            return
                    
    
                self.game.board.draw_on_tiles = True
                        
    def check_keyboard_final_menu_event(self):
        if self.game.menu.is_final_menu:
            self.game.menu.is_final_menu = False
