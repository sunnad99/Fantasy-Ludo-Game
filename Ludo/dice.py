import random
import pygame
import sys

"This class is used for the rolling of a dice, treating it as a seperate entity!"
class Dice:

    def __init__(self, game):
        
        self.game = game
        self.settings = self.game.settings
        self.screen = self.game.screen

        self.initialize_dice_vars()

    def roll_dice(self):
        random.seed()
        dice_val = random.randint(1,6)

        if dice_val != 6:
            self.dice_val_holder.append(dice_val)
        elif dice_val == 6 and self.roll_check >= self.total_rolls - 1:
            self.dice_reset()
        elif dice_val == 6 and self.roll_check < self.total_rolls:
            self.dice_val_holder.append(dice_val)
            self.roll_check += 1
            self.roll_dice()
        
    def dice_reset(self):
        self.roll_check = 0
        self.dice_val_holder = []
    
    def initialize_dice_vars(self):
        "Initializes all the dice variables for use in the game"

        self.total_rolls = 3
        self.roll_check = 0
        self.dice_val_holder = []
        self.dice_image_holder = []

        self.dice_one_image = pygame.image.load(self.settings.dice_one).convert()
        self.dice_two_image = pygame.image.load(self.settings.dice_two).convert()
        self.dice_three_image = pygame.image.load(self.settings.dice_three).convert()
        self.dice_four_image = pygame.image.load(self.settings.dice_four).convert()
        self.dice_five_image = pygame.image.load(self.settings.dice_five).convert()
        self.dice_six_image = pygame.image.load(self.settings.dice_six).convert()

        #self.dice_one_image.set_colorkey(self.settings.board_menu_bg_color)
        #self.dice_two_image.set_colorkey(self.settings.board_menu_bg_color)
        #self.dice_three_image.set_colorkey(self.settings.board_menu_bg_color)
        #self.dice_four_image.set_colorkey(self.settings.board_menu_bg_color)
        #self.dice_five_image.set_colorkey(self.settings.board_menu_bg_color)
        #self.dice_six_image.set_colorkey(self.settings.board_menu_bg_color)

        self.dice_one_image = pygame.transform.scale(self.dice_one_image, (self.settings.dice_width, self.settings.dice_height))
        self.dice_two_image = pygame.transform.scale(self.dice_two_image, (self.settings.dice_width, self.settings.dice_height))
        self.dice_three_image = pygame.transform.scale(self.dice_three_image, (self.settings.dice_width, self.settings.dice_height))
        self.dice_four_image = pygame.transform.scale(self.dice_four_image, (self.settings.dice_width, self.settings.dice_height))
        self.dice_five_image = pygame.transform.scale(self.dice_five_image, (self.settings.dice_width, self.settings.dice_height))
        self.dice_six_image = pygame.transform.scale(self.dice_six_image, (self.settings.dice_width, self.settings.dice_height))

        self.dice_one_rect = self.dice_one_image.get_rect()
        self.dice_two_rect = self.dice_two_image.get_rect()
        self.dice_three_rect = self.dice_three_image.get_rect()
        self.dice_four_rect = self.dice_four_image.get_rect()
        self.dice_five_rect = self.dice_five_image.get_rect()
        self.dice_six_rect = self.dice_six_image.get_rect()

        self.dice_one_rect.centerx, self.dice_one_rect.y = self.settings.screen_center, 2*self.settings.box_size
        self.dice_two_rect.centerx, self.dice_two_rect.y = self.settings.screen_center, 2*self.settings.box_size
        self.dice_three_rect.centerx, self.dice_three_rect.y = self.settings.screen_center, 2*self.settings.box_size
        self.dice_four_rect.centerx, self.dice_four_rect.y = self.settings.screen_center, 2*self.settings.box_size
        self.dice_five_rect.centerx, self.dice_five_rect.y = self.settings.screen_center, 2*self.settings.box_size
        self.dice_six_rect.centerx, self.dice_six_rect.y = self.settings.screen_center, 2*self.settings.box_size
        
        self.dice_image_holder.extend([
            (self.dice_one_image, self.dice_one_rect), 
            (self.dice_two_image, self.dice_two_rect), 
            (self.dice_three_image,self.dice_three_rect), 
            (self.dice_four_image, self.dice_four_rect), 
            (self.dice_five_image, self.dice_five_rect), 
            (self.dice_six_image, self.dice_six_rect)]
        )

    def show_dice(self):
        
        
        # This for loop is iterating through all the dice values
        for self.dice_val in self.dice_val_holder:
            # Draw the dice
            self.current_dice_image, self.current_dice_rect = self.dice_image_holder[self.dice_val - 1]

            # chooses the color, tokens and placeholders for the current player to be used in the events class
            self.game.player.current_player_properties_initialization()

            # This function and the condition is just to see when the value of the dice is less than 6 and if all the tokens are in their respective placeholder positions, a turn shouldnt take place
            base_token_counter = self.game.board.check_tokens_in_base()
            if base_token_counter == self.game.board.total_tokens:
                print("Should display on the screen that the turn is canceled")
                continue     

            self.current_text_color = self.player_text_color_chooser()
                

            self.current_turn = True            
            while self.current_turn:
                self.game.screen.fill(self.settings.board_menu_bg_color)


                # Drawing the text before actually drawing the dice_shower_text
                dice_shower_coordinates = (self.settings.screen_center, self.current_dice_rect.y + 3*self.settings.box_size)
                dice_shower_rect = self.settings.translucent_background_setter(25, f"Player {self.game.player.current_player} drew a {self.dice_val}.", dice_shower_coordinates, "n")
                dice_shower_background_surface = self.settings.draw_translucent_background(dice_shower_rect)
                self.screen.blit(dice_shower_background_surface, dice_shower_rect.topleft)

                self.settings.draw_text(f"Player {self.game.player.current_player} drew a {self.dice_val}.",self.settings.MAIN_MENU_FONT_PATH, 25, self.current_text_color, dice_shower_coordinates[0], dice_shower_coordinates[1], "n")
                self.game.screen.blit(self.current_dice_image, self.current_dice_rect)
                
                # Draw the translucent background before drawing token_chooser_text
                token_chooser_coordinates = (self.settings.screen_center, self.current_dice_rect.y + 4*self.settings.box_size)
                token_chooser_rect = self.settings.translucent_background_setter(20, "Please choose your token!", token_chooser_coordinates, "n")
                token_chooser_background_surface = self.settings.draw_translucent_background(token_chooser_rect)
                self.screen.blit(token_chooser_background_surface, token_chooser_rect.topleft) 

                self.settings.draw_text("Please choose your token!",self.settings.MAIN_MENU_FONT_PATH, 20, self.current_text_color, token_chooser_coordinates[0], token_chooser_coordinates[1], "n")

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game.events.choose_token_on_board_mouse_event()    
                    elif event.type == pygame.QUIT:
                        sys.exit()

                self.game.draw_sprites()
                pygame.display.flip()
                        
        
        self.game.player.change_current_player()

    def player_text_color_chooser(self):
        if self.game.player.current_player_color == "red":
            return self.settings.LIGHT_RED

        elif self.game.player.current_player_color == "green":
            return self.settings.LIGHT_GREEN

        elif self.game.player.current_player_color == "blue":
            return self.settings.LIGHT_BLUE

        elif self.game.player.current_player_color == "yellow":
            return self.settings.LIGHT_YELLOW
    