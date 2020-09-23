import pygame


class Settings:

    def __init__(self, game):

        self.game = game

        "Defining the properties for the screen"
        self.screen_width = 1200
        self.screen_height = 750

        self.GREY = (60, 60, 60)
        self.board_menu_bg_color = (131, 129, 131)

        "Defining tile properties"
        # Size of each tile
        self.total_number_of_boxes = 15
        self.box_size = 50

        # color for the blank
        self.BLACK = (0, 0, 0)

        # properties for path tiles
        self.ludo_board_path = "text_files/ludo_grid.txt"
        self.PATH_FILEPATH = "images/path.jpg"

        self.total_movement_steps = 51
        self.winning_path_threshold = 56

        self.WHITE = (255, 255, 255)

        self.ELF_TILE_PATH = "images/tiles/highelf_tile.png"
        self.ORC_TILE_PATH = "images/tiles/orc_tile.png"
        self.DWARF_TILE_PATH = "images/tiles/dwarf_tile.png"
        self.LYCAN_TILE_PATH = "images/tiles/lycan_tile.png"

        # colors for the red token placeholder
        self.LIGHT_RED = (255, 0, 0)
        self.DARK_RED = (104, 0, 0)
        self.WINNING_RED_PATH = "images/tiles/redpath_dwarf_tile.png"

        # colors for the blue token placeholder
        self.LIGHT_BLUE = (0, 0, 255)
        self.DARK_BLUE = (0, 0, 104)
        self.WINNING_BLUE_PATH = "images/tiles/bluepath_lycan_tile.png"
        

        # colors for the green token placeholder
        self.LIGHT_GREEN = (0, 255, 0)
        self.DARK_GREEN = (0, 104, 0)
        self.WINNING_GREEN_PATH = "images/tiles/greenpath_orc_tile.png"

        # colors for the yellow token placeholder
        self.LIGHT_YELLOW = (255,255,0)
        self.DARK_YELLOW = (104, 104, 0)
        self.WINNING_YELLOW_PATH = "images/tiles/yellowpath_highelf_tile.png"

        "Defining the board properties"

        self.board_width = self.box_size * self.total_number_of_boxes
        self.board_height = self.box_size * self.total_number_of_boxes

        self.base_background_coordinates = (0, 0)
        self.grid_and_borders_coordinates = (0, 0)
        self.dungeon_coordinates = (0, 0)
    
        self.BASE_BACKGROUND_PATH = "images/board images/background_racehomworlds.png"
        self.GRID_AND_BORDERS_PATH = "images/board images/gridandborders.png"
        self.DUNGEON_PATH = "images/board images/Dungeon.png"
        
        "Defining all menu properties properties"
        self.MAIN_MENU_FONT_PATH = "fonts/all_text_font.otf"
        
        self.screen_center = (self.board_width + self.screen_width) // 2

        # Defining the properties for the main menu
        self.LUDO_TITLE_FONT_PATH = "fonts/ludo_title.ttf"
        self.MAIN_MENU_TITLE_IMAGE_PATH = "images/menu images/Main Menu Text.png"
        self.MAIN_MENU_BACKGROUND_PATH = "images/menu images/Menu Background.jpg"

        # Defining the properties for the third menu"
        self.third_menu_rect_width = 200
        self.third_menu_rect_height = 200
        self.third_menu_rect_space = 150

        self.complete_black = 255

        # Defining the properties for the final menu"
        self.DWARF_WIN_SCREEN_PATH = "images/menu images/dwarf_ending.png"
        self.ORC_WIN_SCREEN_PATH = "images/menu images/orc_ending.png"
        self.LYCAN_WIN_SCREEN_PATH = "images/menu images/lycan_ending.png"
        self.ELF_WIN_SCREEN_PATH = "images/menu images/elf_ending.png"

        self.final_menu_text_coordinates = (self.screen_width // 2, self.screen_height)

        self.win_screen_coordinates = (0, 0)

        "Defining token properties"

        self.RED_TOKEN_PATH = "images/tokens/red.png"
        self.GREEN_TOKEN_PATH = "images/tokens/green.png" 
        self.BLUE_TOKEN_PATH = "images/tokens/blue.png"
        self.YELLOW_TOKEN_PATH = "images/tokens/yellow.png"

        "Setting the properties for the dice images"
        self.dice_width = 104
        self.dice_height = 104

        self.dice_one = "images/dice/DiceCropped_1.png"
        self.dice_two = "images/dice/DiceCropped_2.png"
        self.dice_three = "images/dice/DiceCropped_3.png"
        self.dice_four = "images/dice/DiceCropped_4.png"
        self.dice_five = "images/dice/DiceCropped_5.png"
        self.dice_six = "images/dice/DiceCropped_6.png"

        "Defining the starting paths for the seperate colors, and for safe spots"

        self.red_starting_path = 4
        self.green_starting_path = 14
        self.blue_starting_path = 37
        self.yellow_starting_path = 47


    def draw_text(self, text, font_path, size, color, x, y, align):
        font = pygame.font.Font(font_path,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()

        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        
        self.game.screen.blit(text_surface, text_rect)
        return text_rect
    
    def load_data(self):
        
        self.grid_data = []
        with open(self.ludo_board_path , 'r') as ludo_file:

            for line in ludo_file:
                self.grid_data.append(line)
    
    def translucent_background_setter(self, font_size, text, coordinates, align):
        text_font = pygame.font.Font(self.MAIN_MENU_FONT_PATH, font_size)
        text_surface = text_font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()

        if align == "nw":
            text_rect.topleft = coordinates
        if align == "ne":
            text_rect.topright = coordinates
        if align == "sw":
            text_rect.bottomleft = coordinates
        if align == "se":
            text_rect.bottomright = coordinates
        if align == "n":
            text_rect.midtop = coordinates
        if align == "s":
            text_rect.midbottom = coordinates
        if align == "e":
            text_rect.midright = coordinates
        if align == "w":
            text_rect.midleft = coordinates
        if align == "center":
            text_rect.center = coordinates

        return text_rect
    
    def draw_translucent_background(self, text_rect):

        background_surface = pygame.Surface(text_rect.size)
        background_surface.set_alpha(180)
        background_surface.fill((0, 0, 0))

        return background_surface
