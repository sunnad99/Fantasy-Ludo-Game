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

            if self.game.menu.red_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_red:
                self.game.menu.red_transparent_image.set_alpha(180)
                self.game.menu.player_text = f"Select red color for player {self.game.player.current_player}"
                
            elif self.game.menu.selected_red:
                self.game.menu.red_transparent_image.set_alpha(0)
                
            if self.game.menu.green_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_green:
                self.game.menu.green_transparent_image.set_alpha(180)
                self.game.menu.player_text = f"Select green color for player {self.game.player.current_player}"
            elif self.game.menu.selected_green:
                self.game.menu.green_transparent_image.set_alpha(0)
                
            
            if self.game.menu.blue_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_blue:
                self.game.menu.blue_transparent_image.set_alpha(180)
                self.game.menu.player_text = f"Select blue color for player {self.game.player.current_player}"
            elif self.game.menu.selected_blue:
                self.game.menu.blue_transparent_image.set_alpha(0)
                
            if self.game.menu.yellow_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_yellow:
                self.game.menu.yellow_transparent_image.set_alpha(180)
                self.game.menu.player_text = f"Select yellow color for player {self.game.player.current_player}"
            elif self.game.menu.selected_yellow:
                self.game.menu.yellow_transparent_image.set_alpha(0)
                
        elif event_type == pygame.MOUSEBUTTONDOWN and self.game.menu.is_3rd_menu:
            state_of_buttons = pygame.mouse.get_pressed()

            if state_of_buttons[0] == 1 and self.game.menu.red_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_red:
                self.game.menu.red_transparent_image.set_alpha(self.settings.complete_black)
                self.game.player.color_for_player[self.game.menu.counter] = "red"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_red = False

            if state_of_buttons[0] == 1 and self.game.menu.green_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_green:
                self.game.menu.green_transparent_image.set_alpha(self.settings.complete_black)
                self.game.player.color_for_player[self.game.menu.counter] = "green"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_green = False

            if state_of_buttons[0] == 1 and self.game.menu.blue_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_blue:
                self.game.menu.blue_transparent_image.set_alpha(self.settings.complete_black)
                self.game.player.color_for_player[self.game.menu.counter] = "blue"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_blue = False

            if state_of_buttons[0] == 1 and self.game.menu.yellow_rect.collidepoint(self.mouse_pos) and self.game.menu.selected_yellow:
                self.game.menu.yellow_transparent_image.set_alpha(self.settings.complete_black)
                self.game.player.color_for_player[self.game.menu.counter] = "yellow"
                self.game.player.current_player += 1
                self.game.menu.counter += 1
                self.game.menu.selected_yellow = False

    def choose_token_on_board_mouse_event(self):
        "Lets you choose the token based on which token you click."
        self.mouse_pos = pygame.mouse.get_pos()
        state_of_buttons = pygame.mouse.get_pressed()

        token_checker = 0
        for self.token_selector, self.ludo_token in enumerate(self.game.player.current_player_token_group):

            # This if condition is just to make sure the same dice value doesn't act on multiple tokens on the same spot
            if token_checker == 1:
                break

            # checking to see if token is click on
            if self.ludo_token.rect.collidepoint(self.mouse_pos) and state_of_buttons[0] == 1:
                
                self.placeholder_sprite = self.game.player.current_player_placeholder_group[self.token_selector]
                
                # This if statement checks if you clicked a token which is placed onto a placeholder
                if self.ludo_token.rect.x == self.placeholder_sprite.rect.x and self.ludo_token.rect.y == self.placeholder_sprite.rect.y:
                    
                    if self.game.dice.dice_val < 6:
                        self.settings.draw_text("Sorry you cannot choose this token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.settings.BLACK, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n")
                        self.game.dice.current_turn = False
                    else:

                        self.game.player.current_player_on_start_path()

                        self.settings.draw_text(f"Player {self.game.player.current_player} chose his {self.game.player.current_player_color} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n")

                # This else statement controls the movement for the tiles on the path
                else:
                    self.movement_checker = self.game.dice.dice_val + self.game.player.token_movement_counter[self.game.player.current_player_color][self.token_selector]
                    print("Color:", self.game.player.current_player_color, "Indice:", self.token_selector,"Steps taken:", self.movement_checker)
                    if self.movement_checker < self.settings.total_movement_steps:

                        self.game.player.move_on_normal_path()
                        self.settings.draw_text(f"Player {self.game.player.current_player} chose his {self.game.player.current_player_color} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n")  
                        token_checker += 1
                    else:

                        self.game.player.move_on_winning_path()
                        self.settings.draw_text(f"Player {self.game.player.current_player} chose his {self.game.player.current_player_color} token!", self.settings.MAIN_MENU_FONT_PATH, 15, self.game.dice.current_text_color, self.settings.screen_center, self.game.dice.current_dice_rect.y + 5*self.settings.box_size, "n") 
                        token_checker += 1   

                self.game.draw_sprites()
                pygame.display.flip()
                time.sleep(1)
                self.game.dice.current_turn = False

    def check_keyboard_board_menu_event(self):
        if self.game.menu.is_board_menu:
            self.game.dice.roll_dice()
            print("\n","Current_Player:",self.game.player.current_player,"Dice_vals:",self.game.dice.dice_val_holder)
            self.game.dice.show_dice()
            self.game.dice.dice_reset()

    def check_keyboard_final_menu_event(self):
        if self.game.menu.is_final_menu:
            self.game.menu.is_final_menu = False