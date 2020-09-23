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

        self.two_player_color = self.settings.BLACK
        self.three_player_color = self.settings.BLACK
        self.four_player_color = self.settings.BLACK

        self.selected_red = True
        self.selected_blue = True
        self.selected_green = True
        self.selected_yellow = True

        # This counter ensures that the game leaves the third menu after all players have chosen their colors
        self.counter = 0
        
        # To print text to show exactly what color the respective player will be choosing
        self.player_text = ""

    def main_menu(self):
        self.is_main_menu = True
        while self.is_main_menu:
                
            self.screen.fill(self.settings.GREY)
            
            self.draw_main_menu()
            self.start_game = self.settings.draw_text("Start Game", self.settings.MAIN_MENU_FONT_PATH,50, self.start_game_color, self.start_text_coordinates[0], self.start_text_coordinates[1], "center")
            
            self.exit_game = self.settings.draw_text("Exit", self.settings.MAIN_MENU_FONT_PATH,50, self.exit_game_color, self.end_text_coordinates[0], self.end_text_coordinates[1], "center")
                
            #self.settings.draw_text("L", self.settings.LUDO_TITLE_FONT_PATH, 100, self.settings.LIGHT_BLUE, self.screen_rect.midtop[0] - 3*self.settings.box_size, self.screen_rect.midtop[1], "n")
            #self.settings.draw_text("u", self.settings.LUDO_TITLE_FONT_PATH, 100, self.settings.LIGHT_GREEN, self.screen_rect.midtop[0] - self.settings.box_size, self.screen_rect.midtop[1], "n")
            #self.settings.draw_text("d", self.settings.LUDO_TITLE_FONT_PATH, 100, self.settings.LIGHT_RED, self.screen_rect.midtop[0] + 1*self.settings.box_size, self.screen_rect.midtop[1], "n")
            #self.settings.draw_text("o", self.settings.LUDO_TITLE_FONT_PATH, 100, self.settings.LIGHT_YELLOW, self.screen_rect.midtop[0] + 3*self.settings.box_size, self.screen_rect.midtop[1], "n")
            
            self.game._check_events()
            
            pygame.display.flip()

    def second_menu(self):
        "This menu is used to choose the number of players"

        self.is_2nd_menu = True
        while self.is_2nd_menu:
            self.screen.fill(self.settings.GREY)
            self.settings.draw_text("Select number of players", self.settings.LUDO_TITLE_FONT_PATH, 65, self.settings.LIGHT_BLUE, self.screen_rect.midtop[0], self.screen_rect.midtop[1], "n")
            self.player_2 = self.settings.draw_text("II Players", self.settings.MAIN_MENU_FONT_PATH,50, self.two_player_color, self.screen_rect.centerx - 6*self.settings.box_size, self.screen_rect.centery - self.settings.box_size, "center")
            self.player_3 = self.settings.draw_text("III Players", self.settings.MAIN_MENU_FONT_PATH,50, self.three_player_color, self.screen_rect.centerx + 6*self.settings.box_size, self.screen_rect.centery - self.settings.box_size, "center")
            self.player_4 = self.settings.draw_text("IV Players", self.settings.MAIN_MENU_FONT_PATH,50, self.four_player_color, self.screen_rect.centerx, self.screen_rect.centery + self.settings.box_size, "center")
        
            self.game._check_events()

            pygame.display.flip()
        
    def third_menu(self):
        # calls this menu to decide the color choices for each player
        # Breaks out of all the loops then to run the game and calls the function to initialize the tokens for the players
        self.is_3rd_menu = True
        self.game.player.color_for_player = [""]*self.game.player.no_of_players
        

        while self.is_3rd_menu:
            
            if self.counter == self.game.player.no_of_players:
                self.is_3rd_menu = False
            

            # Update the rectangles
            self.game._check_events()
            
            # Draw the rectangles
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
        
        self.main_title_surface = pygame.Surface(self.title_image_rect.size)
        self.main_title_surface.set_alpha(180) 
        self.main_title_surface.fill((0, 0, 0))

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
        # makes rectangles
        self.red_rect = pygame.Rect(0, 0, self.settings.third_menu_rect_width, self.settings.third_menu_rect_height)
        self.green_rect = pygame.Rect(0, 0, self.settings.third_menu_rect_width, self.settings.third_menu_rect_height)
        self.blue_rect = pygame.Rect(0, 0, self.settings.third_menu_rect_width, self.settings.third_menu_rect_height)
        self.yellow_rect = pygame.Rect(0, 0, self.settings.third_menu_rect_width, self.settings.third_menu_rect_height)

        self.red_rect.centerx, self.red_rect.centery = (self.screen_rect.centerx - 3*self.settings.third_menu_rect_space,  self.screen_rect.centery)
        self.green_rect.centerx, self.green_rect.centery = (self.screen_rect.centerx - self.settings.third_menu_rect_space,  self.screen_rect.centery)
        self.blue_rect.centerx, self.blue_rect.centery = (self.screen_rect.centerx + self.settings.third_menu_rect_space, self.screen_rect.centery)
        self.yellow_rect.centerx, self.yellow_rect.centery = (self.screen_rect.centerx + 3*self.settings.third_menu_rect_space, self.screen_rect.centery)         

        self.red_transparent_image = pygame.Surface((self.settings.third_menu_rect_width,self.settings.third_menu_rect_height))
        self.green_transparent_image = pygame.Surface((self.settings.third_menu_rect_width,self.settings.third_menu_rect_height))
        self.blue_transparent_image = pygame.Surface((self.settings.third_menu_rect_width,self.settings.third_menu_rect_height))
        self.yellow_transparent_image = pygame.Surface((self.settings.third_menu_rect_width,self.settings.third_menu_rect_height))

        self.red_transparent_image.fill((0, 0, 0, 0))
        self.green_transparent_image.fill((0, 0, 0, 0))
        self.blue_transparent_image.fill((0, 0, 0, 0))
        self.yellow_transparent_image.fill((0, 0, 0, 0))
    
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
        
        pygame.draw.rect(self.game.screen, self.settings.LIGHT_RED, self.red_rect)
        pygame.draw.rect(self.game.screen, self.settings.LIGHT_GREEN, self.green_rect)
        pygame.draw.rect(self.game.screen, self.settings.LIGHT_BLUE, self.blue_rect)
        pygame.draw.rect(self.game.screen, self.settings.LIGHT_YELLOW, self.yellow_rect)

        self.screen.blit(self.red_transparent_image, self.red_rect)
        self.screen.blit(self.green_transparent_image, self.green_rect)
        self.screen.blit(self.blue_transparent_image, self.blue_rect)
        self.screen.blit(self.yellow_transparent_image, self.yellow_rect)

        self.settings.draw_text(self.player_text, self.settings.MAIN_MENU_FONT_PATH, 25,self.settings.BLACK, self.screen_rect.centerx, self.screen_rect.centery + 4*self.settings.box_size, "center" )

    def draw_final_menu(self, color):

        if color == "red":

            self.screen.blit(self.dwarf_win_screen, self.settings.win_screen_coordinates)
            
            self.settings.draw_text("The dwarfs discover wonderous materials long thought to be lost to the ages in the ruins.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size,
            align = "n")

            self.settings.draw_text("With these materials the Dwarven empire gains technological supremacy over the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size + 20,
            align = "n")

            self.settings.draw_text("You are assigned as the Dwarven High King by the dwarven race.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n")

            self.settings.draw_text("Congratulations stranger, you bring a new age of technological advancements to ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n")

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n")

        elif color == "green":

            self.screen.blit(self.orc_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The Orcs discover the lost art of blood magic in the ancient ruins.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size,
            align = "n")

            self.settings.draw_text("The orcs start using the blood magic to gain physical and mental enhancements, the orc hoard is now unstoppable by the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size + 20,
            align = "n")

            self.settings.draw_text("You are assigned as the HEAD WARCHIEF of the orc hoards.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n")

            self.settings.draw_text("Congratulations stranger, riches await you as you bring endless pillaging and war to ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n")

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n")

        elif color == "blue":

            self.screen.blit(self.lycan_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The Lycans discover the seeds of life in the ancient ruins. They use the seeds to bring back life to their dying continent,",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size,
            align = "n")

            self.settings.draw_text("unfortunately, the cost of using the seeds is at the expense of other continents.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 4*self.settings.box_size + 20,
            align = "n")

            self.settings.draw_text("This brings upon an endless famine and death the lycans were previously suffering to the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size + 10,
            align = "n")

            self.settings.draw_text("You are assigned as the PRIEST OF LIFE by the Lycan packs. Congratulations stranger,",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size,
            align = "n")

            self.settings.draw_text("you bring peace to the lycan continent but mass famine and suffering to the rest of ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2*self.settings.box_size + 20,
            align = "n")

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size + 10,
            align = "n")

        elif color == "yellow":

            self.screen.blit(self.elf_win_screen, self.settings.win_screen_coordinates)

            self.settings.draw_text("The elves use the ancient power from the ruins to bring upon a new age of supremacy over the other primal races.",
            self.settings.LUDO_TITLE_FONT_PATH,15,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 3*self.settings.box_size,
            align = "n")

            self.settings.draw_text("You are assigned as ARCH MAGUS KAISER by the elven race. Congratulations stranger, you are now the iron fist ruler of ARCADIA!",
            self.settings.LUDO_TITLE_FONT_PATH,14,self.settings.WHITE, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - 2.5*self.settings.box_size,
            align = "n")

            # The text that will return you to main menu
            self.settings.draw_text("Press \"Spacebar\" to return back to the main menu...",
            self.settings.LUDO_TITLE_FONT_PATH,13,self.settings.LIGHT_RED, self.settings.final_menu_text_coordinates[0], self.settings.final_menu_text_coordinates[1] - self.settings.box_size - 20,
            align = "n")
        
        
        