import pygame



class Menu:

    def __init__(self, game):

        self.game = game
        self.settings = self.game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.initialize_menu_vars()
        
    def initialize_menu_vars(self):
        self.is_main_menu = False
        self.is_2nd_menu = False
        self.is_3rd_menu = False
        self.is_board_menu = False
        self.is_final_menu = False

        self.start_game_color = self.settings.WHITE
        self.exit_game_color = self.settings.WHITE
        self.roll_the_dice_button_color = self.settings.WHITE
        self.okay_button_color = self.settings.WHITE

        self.two_player_color = self.settings.BLACK
        self.three_player_color = self.settings.BLACK
        self.four_player_color = self.settings.BLACK

        self.selected_red = True
        self.selected_blue = True
        self.selected_green = True
        self.selected_yellow = True

        # Settings for skipped turns
        self.is_turn_skip = False
        self.skipped_turn_text = ""

        # This counter ensures that the game leaves the third menu after all players have chosen their colors
        self.counter = 0
        
        # To print text to show exactly what color the respective player will be choosing
        self.player_text = ""

        # Initializing the "Roll Dice" button
        self.roll_dice_button_coordinates = (self.settings.screen_center, 2*self.settings.box_size + 7*self.settings.box_size)
        self.roll_dice_button_rect = self.settings.translucent_background_setter(50, "Roll Dice", self.roll_dice_button_coordinates, "n")
        self.roll_dice_button_surface = self.settings.draw_translucent_background(self.roll_dice_button_rect)
        
        # Initialize the "Ok" button
        self.okay_button_coordinates = (self.settings.screen_center, 2*self.settings.box_size + 7*self.settings.box_size)
        self.okay_button_rect = self.settings.translucent_background_setter(50, "Okay", self.okay_button_coordinates, "n")
        self.okay_button_surface = self.settings.draw_translucent_background(self.okay_button_rect)
        self.okay_button = self.settings.draw_text("Okay",self.settings.MAIN_MENU_FONT_PATH, 50, self.okay_button_color, self.okay_button_coordinates[0], self.okay_button_coordinates[1], "n", False)

    def main_menu(self):
        self.is_main_menu = True
        while self.is_main_menu:
                
            self.screen.fill(self.settings.GREY)
            
            self.draw_main_menu()
            self.start_game = self.settings.draw_text("Start Game", self.settings.MAIN_MENU_FONT_PATH,50, self.start_game_color, self.start_text_coordinates[0], self.start_text_coordinates[1], "center", True)
            
            self.exit_game = self.settings.draw_text("Exit", self.settings.MAIN_MENU_FONT_PATH,50, self.exit_game_color, self.end_text_coordinates[0], self.end_text_coordinates[1], "center", True)
                
            self.game._check_events()
            
            pygame.display.flip()

    def second_menu(self):
        "This menu is used to choose the number of players"

        self.is_2nd_menu = True
        while self.is_2nd_menu:
            self.screen.fill(self.settings.GREY)
            self.settings.draw_text("Select number of players", self.settings.LUDO_TITLE_FONT_PATH, 65, self.settings.LIGHT_BLUE, self.screen_rect.midtop[0], self.screen_rect.midtop[1], "n", True)
            self.player_2 = self.settings.draw_text("II Players", self.settings.MAIN_MENU_FONT_PATH,50, self.two_player_color, self.screen_rect.centerx - 6*self.settings.box_size, self.screen_rect.centery - self.settings.box_size, "center", True)
            self.player_3 = self.settings.draw_text("III Players", self.settings.MAIN_MENU_FONT_PATH,50, self.three_player_color, self.screen_rect.centerx + 6*self.settings.box_size, self.screen_rect.centery - self.settings.box_size, "center", True)
            self.player_4 = self.settings.draw_text("IV Players", self.settings.MAIN_MENU_FONT_PATH,50, self.four_player_color, self.screen_rect.centerx, self.screen_rect.centery + self.settings.box_size, "center", True)
        
            self.game._check_events()

            pygame.display.flip()
        
    def third_menu(self):
        "This menu is used to decide the color choices for each player"

        # Breaks out of all the loops then to run the game and calls the function to initialize the tokens for the players
        self.is_3rd_menu = True
        self.game.player.color_for_player = [""]*self.game.player.no_of_players
        

        while self.is_3rd_menu:
            
            if self.counter == self.game.player.no_of_players:
                self.is_3rd_menu = False
            

            # Update the race sprites
            self.game._check_events()
            
            # Draw the race sprites
            self.screen.fill(self.settings.GREY)
            self.draw_third_menu()
            

            
            pygame.display.flip()

    def final_menu(self, color):
        while self.is_final_menu:

            self.game._check_events()

            self.draw_final_menu(color)

            pygame.display.flip()

    def initialize_main_menu(self):
        "Initializes the main menu elements"
        # Initializing the main menu background
        self.main_menu_background = pygame.image.load(self.settings.MAIN_MENU_BACKGROUND_PATH).convert()

        # Initializing the main menu title image
        self.title_image = pygame.image.load(self.settings.MAIN_MENU_TITLE_IMAGE_PATH)

        self.title_image_rect = self.title_image.get_rect()
        
        self.main_title_surface = self.settings.draw_translucent_background(self.title_image_rect)

        self.main_menu_title_image_coordinates = (self.screen_rect.midtop[0] - self.title_image_rect.midtop[0], self.screen_rect.midtop[1] - self.title_image_rect.midtop[1])
        self.title_image_rect.x, self.title_image_rect.y =  self.main_menu_title_image_coordinates

        # Initializng elements for the start and exit buttons
        self.start_text_coordinates = (self.screen_rect.centerx, self.screen_rect.centery - self.settings.box_size)
        self.end_text_coordinates = (self.screen_rect.centerx, self.screen_rect.centery + self.settings.box_size)

        self.start_text_rect = self.settings.translucent_background_setter(50, "Start Game", self.start_text_coordinates, "center")
        self.end_text_rect = self.settings.translucent_background_setter(50, "Exit", self.end_text_coordinates, "center")

        self.start_game_surface = self.settings.draw_translucent_background(self.start_text_rect)
        self.end_game_surface = self.settings.draw_translucent_background(self.end_text_rect)

    def initialize_third_menu(self):
        
        self.dwarf_surface = pygame.transform.scale(pygame.image.load(self.settings.DWARF_CHOOSE_MENU_PATH), (self.settings.third_menu_rect_width,int(1.5*self.settings.third_menu_rect_width)))
        self.orc_surface = pygame.transform.scale(pygame.image.load(self.settings.ORC_CHOOSE_MENU_PATH), (self.settings.third_menu_rect_width,int(1.5*self.settings.third_menu_rect_width)))
        self.lycan_surface = pygame.transform.scale(pygame.image.load(self.settings.LYCAN_CHOOSE_MENU_PATH), (self.settings.third_menu_rect_width,int(1.5*self.settings.third_menu_rect_width)))
        self.elf_surface = pygame.transform.scale(pygame.image.load(self.settings.ELF_CHOOSE_MENU_PATH), (self.settings.third_menu_rect_width,int(1.5*self.settings.third_menu_rect_width)))

        self.dwarf_surface.set_colorkey(self.settings.WHITE)
        self.orc_surface.set_colorkey(self.settings.WHITE)
        self.lycan_surface.set_colorkey(self.settings.WHITE)
        self.elf_surface.set_colorkey(self.settings.WHITE)

        self.dwarf_rect = self.dwarf_surface.get_rect()
        self.orc_rect = self.orc_surface.get_rect()
        self.lycan_rect = self.lycan_surface.get_rect()
        self.elf_rect = self.elf_surface.get_rect()
    
        self.dwarf_rect.centerx, self.dwarf_rect.centery = (self.screen_rect.centerx - 3*self.settings.third_menu_rect_space,  self.screen_rect.centery)
        self.orc_rect.centerx, self.orc_rect.centery = (self.screen_rect.centerx - self.settings.third_menu_rect_space,  self.screen_rect.centery)
        self.lycan_rect.centerx, self.lycan_rect.centery = (self.screen_rect.centerx + self.settings.third_menu_rect_space, self.screen_rect.centery)
        self.elf_rect.centerx, self.elf_rect.centery = (self.screen_rect.centerx + 3*self.settings.third_menu_rect_space, self.screen_rect.centery)         
    
    def initialize_final_menu(self):
        self.dwarf_win_screen = pygame.image.load(self.settings.DWARF_WIN_SCREEN_PATH).convert()
        self.orc_win_screen = pygame.image.load(self.settings.ORC_WIN_SCREEN_PATH).convert()
        self.lycan_win_screen = pygame.image.load(self.settings.LYCAN_WIN_SCREEN_PATH).convert()
        self.elf_win_screen = pygame.image.load(self.settings.ELF_WIN_SCREEN_PATH).convert()

    def draw_main_menu(self):
        self.screen.blit(self.main_menu_background, (0,0))

        self.screen.blit(self.main_title_surface, self.main_menu_title_image_coordinates)
        self.screen.blit(self.title_image, self.title_image_rect)

        self.screen.blit(self.start_game_surface, self.start_text_rect.topleft)
        self.screen.blit(self.end_game_surface, self.end_text_rect.topleft)
        
    def draw_third_menu(self):
        
        self.screen.blit(self.dwarf_surface, self.dwarf_rect)
        self.screen.blit(self.orc_surface, self.orc_rect)
        self.screen.blit(self.lycan_surface, self.lycan_rect)
        self.screen.blit(self.elf_surface, self.elf_rect)

        self.settings.draw_text(self.player_text, self.settings.MAIN_MENU_FONT_PATH, 25,self.settings.BLACK, self.screen_rect.centerx, self.screen_rect.centery + 5*self.settings.box_size, "center", True)

    def draw_final_menu(self, color):

        if color == "red":

            self.screen.blit(self.dwarf_win_screen, self.settings.win_screen_coordinates)
            
            self.settings.draw_text("The dwarfs discover wonderous materials long thought to be lost to the ages in the ruins.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("With these materials the Dwarven empire gains technological supremacy over the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size + 20,
            align = "n", isDraw = True)

            self.settings.draw_text("You are assigned as the Dwarven High King by the dwarven race.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("Congratulations stranger, you bring a new age of technological advancements to ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n", isDraw = True)

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n", isDraw = True)

        elif color == "green":

            self.screen.blit(self.orc_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The Orcs discover the lost art of blood magic in the ancient ruins.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("The orcs start using the blood magic to gain physical and mental enhancements, the orc hoard is now unstoppable by the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size + 20,
            align = "n", isDraw = True)

            self.settings.draw_text("You are assigned as the HEAD WARCHIEF of the orc hoards.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("Congratulations stranger, riches await you as you bring endless pillaging and war to ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n", isDraw = True)

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n", isDraw = True)

        elif color == "blue":

            self.screen.blit(self.lycan_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The Lycans discover the seeds of life in the ancient ruins. They use the seeds to bring back life to their dying continent,",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("unfortunately, the cost of using the seeds is at the expense of other continents.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size + 20,
            align = "n", isDraw = True)

            self.settings.draw_text("This brings upon an endless famine and death the lycans were previously suffering to the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size + 10,
            align = "n", isDraw = True)

            self.settings.draw_text("You are assigned as the PRIEST OF LIFE by the Lycan packs. Congratulations stranger,",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("you bring peace to the lycan continent but mass famine and suffering to the rest of ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n", isDraw = True)

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n", isDraw = True)

        elif color == "yellow":

            self.screen.blit(self.elf_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The elves use the ancient power from the ruins to bring upon a new age of supremacy over the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size,
            align = "n", isDraw = True)

            self.settings.draw_text("You are assigned as ARCH MAGUS KAISER by the elven race. Congratulations stranger, you are now the iron fist ruler of ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,14,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2.5*self.settings.box_size,
            align = "n", isDraw = True)

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size - 20,
            align = "n", isDraw = True)

    def show_buttons_on_board_menu(self):
        "This function takes care of showing the buttons on the board menu."
        
        if self.is_turn_skip:
            turn_skip_text_color = self.settings.token_color_dictionary[self.game.player.current_player_color]
            self.settings.draw_text(f"{self.skipped_turn_text}", self.settings.MAIN_MENU_FONT_PATH, 25, turn_skip_text_color, self.settings.screen_center, 5*self.settings.box_size, "n", True)
            self.screen.blit(self.okay_button_surface, self.okay_button_rect.topleft)
            self.settings.draw_text("Okay",self.settings.MAIN_MENU_FONT_PATH, 50, self.okay_button_color, self.okay_button_coordinates[0], self.okay_button_coordinates[1], "n", True)

        else:
            self.game.player.show_current_player()

            self.screen.blit(self.roll_dice_button_surface, self.roll_dice_button_rect.topleft)
            self.rtd_button = self.settings.draw_text("Roll Dice",self.settings.MAIN_MENU_FONT_PATH, 50, self.roll_the_dice_button_color, self.roll_dice_button_coordinates[0], self.roll_dice_button_coordinates[1], "n", True)           