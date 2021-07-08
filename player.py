from ludo_token import LudoToken

class Player:

    def __init__(self, game):
        
        self.game = game
        self.settings = self.game.settings

        self.initialize_player_vars()
    
    def initialize_player_vars(self):
        self.no_of_players = -1
        self.current_player = 1
        self.current_player_color = ""
        self.current_player_token_group = [] 
        self.current_player_placeholder_group = []
        self.current_winning_path_tile_list = []

        self.token_sprite_list = {} # For each respective color, we store a token list consisting of all the tokens present on the board
        self.token_movement_counter = {} # Tracks the total number of steps taken by each token of each color
        self.token_path_indice = {} # Keeps track of which path tile the tokens are currently on (only works for the movement tiles)
        self.team_path = {} # keeps the path laid out for each team
        self.winning_path = {} # stores the indices that will map to the winning path for each team

        self.color_for_player = []

    def initialize_players(self):
        "Initializes the players with their respective tokens"
        for color in self.color_for_player:

            if color == "red":
                self.red_token_sprites = []
                self.add_token_sprites(color)
                self.token_sprite_list[color] = self.red_token_sprites
                self.token_movement_counter[color] = [0, 0, 0, 0]
                self.token_path_indice[color] = [0, 0, 0, 0]

                self.team_path[color] = [4, 6, 8, 10, 12, 19, 20, 21, 22, 23, 24, 26, 38, 37,
                36, 35, 34, 33, 40, 42, 44, 46, 48, 51, 50, 49, 47, 45, 43, 41, 39, 32, 31, 
                30, 29, 28, 27, 25, 13, 14, 15, 16, 17, 18, 11, 9, 7, 5, 3, 0, 1, 2]

                self.winning_path[color] = [0, 1, 2, 3, 4, 5]
                
            elif color == "green":
                self.green_token_sprites = []
                self.add_token_sprites(color)
                self.token_sprite_list[color] = self.green_token_sprites
                self.token_movement_counter[color] = [0, 0, 0, 0]
                self.token_path_indice[color] = [0, 0, 0, 0]

                self.team_path[color] = [14, 15, 16, 17, 18, 11, 9, 7, 5, 3, 0, 1, 2, 4, 6, 8, 
                10, 12, 19, 20, 21, 22, 23, 24, 26, 38, 37, 36, 35, 34, 33, 40, 42, 44, 46, 48,
                51, 50, 49, 47, 45, 43, 41, 39, 32, 31, 30, 29, 28, 27, 25, 13]

                self.winning_path[color] = [0, 1, 2, 3, 4, 5]
                
            elif color == "blue":
                self.blue_token_sprites = []
                self.add_token_sprites(color)
                self.token_sprite_list[color] = self.blue_token_sprites
                self.token_movement_counter[color] = [0, 0, 0, 0]
                self.token_path_indice[color] = [0, 0, 0, 0]

                self.team_path[color] = [37, 36, 35, 34, 33, 40, 42, 44, 46, 48, 51, 50, 49, 47, 
                45, 43, 41, 39, 32, 31, 30, 29, 28, 27, 25, 13, 14, 15, 16, 17, 18, 11, 9, 7, 5, 
                3, 0, 1, 2, 4, 6, 8, 10, 12, 19, 20, 21, 22, 23, 24, 26, 38]

                self.winning_path[color] = [5, 4, 3, 2, 1, 0]
                
            elif color == "yellow":
                self.yellow_token_sprites = []
                self.add_token_sprites(color)
                self.token_sprite_list[color]= self.yellow_token_sprites
                self.token_movement_counter[color] = [0, 0, 0, 0]
                self.token_path_indice[color] = [0, 0, 0, 0]

                self.team_path[color] = [47, 45, 43, 41, 39, 32, 31, 30, 29, 28, 27, 25, 13, 14, 
                15, 16, 17, 18, 11, 9, 7, 5, 3, 0, 1, 2, 4, 6, 8, 10, 12, 19, 20, 21, 22, 23, 24,
                26, 38, 37, 36, 35, 34, 33, 40, 42, 44, 46, 48, 51, 50, 49]

                self.winning_path[color] = [5, 4, 3, 2, 1, 0]

        self.game.menu.is_board_menu = True
            

        # settings the current player back to 1 after settings the sprites
        self.current_player = 1

    def add_token_sprites(self, color):
        if color == "red":
            for sprite in self.game.board.red_placeholder_path_sprites:
                x = sprite.rect.x
                y = sprite.rect.y
                self.red_token_sprites.append(LudoToken(self.game, color, x, y))

        elif color == "green":
            for sprite in self.game.board.green_placeholder_path_sprites:
                x = sprite.rect.x
                y = sprite.rect.y
                self.green_token_sprites.append(LudoToken(self.game, color, x, y))

        elif color == "blue":
            for sprite in self.game.board.blue_placeholder_path_sprites:
                x = sprite.rect.x
                y = sprite.rect.y
                self.blue_token_sprites.append(LudoToken(self.game, color, x, y))

        elif color == "yellow":
            for sprite in self.game.board.yellow_placeholder_path_sprites:
                x = sprite.rect.x
                y = sprite.rect.y
                self.yellow_token_sprites.append(LudoToken(self.game, color, x, y))

    def draw_tokens_on_board(self, surface):

        for sprite_group_key in self.token_sprite_list:
            for token in self.token_sprite_list[sprite_group_key]:
                token.draw(surface)

    def show_current_player(self):
        self.settings.draw_text(f"Player {self.current_player}'s turn", self.settings.MAIN_MENU_FONT_PATH, 25, self.settings.BLACK, self.settings.screen_center, self.settings.box_size, "n", True)
    
    def current_player_properties_initialization(self):
        self.current_player_color = self.color_for_player[self.current_player - 1]
        
        self.current_player_token_group = self.token_sprite_list[self.current_player_color]
        
        self.current_player_placeholder_group_chooser()

    def current_player_placeholder_group_chooser(self):

        if self.current_player_color == "red":
            self.current_player_placeholder_group = self.game.board.red_placeholder_path_sprites

        elif self.current_player_color == "green":
            self.current_player_placeholder_group = self.game.board.green_placeholder_path_sprites

        elif self.current_player_color == "blue":
            self.current_player_placeholder_group = self.game.board.blue_placeholder_path_sprites

        elif self.current_player_color == "yellow":
            self.current_player_placeholder_group = self.game.board.yellow_placeholder_path_sprites
    
    def change_current_player(self):
        if self.current_player == self.no_of_players:
            self.current_player = 1
        else:
            self.current_player += 1

# These are all the movement functions

    def collision_placeholder_chooser(self, color):
        if color == "red":
            return self.game.board.red_placeholder_path_sprites

        elif color == "green":
            return self.game.board.green_placeholder_path_sprites

        elif color == "blue":
            return self.game.board.blue_placeholder_path_sprites

        elif color == "yellow":
            return self.game.board.yellow_placeholder_path_sprites

    def current_player_on_start_path(self):
        if self.current_player_color == "red":
             
            self.starting_path_sprite = self.game.board.movement_path_sprites[self.settings.red_starting_path]

            self.game.events.ludo_token.rect.x =  self.starting_path_sprite.rect.x
            self.game.events.ludo_token.rect.y =  self.starting_path_sprite.rect.y

        elif self.current_player_color == "green":

             
            self.starting_path_sprite = self.game.board.movement_path_sprites[self.settings.green_starting_path]
            
            self.game.events.ludo_token.rect.x =  self.starting_path_sprite.rect.x
            self.game.events.ludo_token.rect.y =  self.starting_path_sprite.rect.y

        elif self.current_player_color == "blue":
            
            self.starting_path_sprite = self.game.board.movement_path_sprites[self.settings.blue_starting_path]
            
            self.game.events.ludo_token.rect.x =  self.starting_path_sprite.rect.x
            self.game.events.ludo_token.rect.y =  self.starting_path_sprite.rect.y

        elif self.current_player_color == "yellow":
            
             
            self.starting_path_sprite = self.game.board.movement_path_sprites[self.settings.yellow_starting_path]

            self.game.events.ludo_token.rect.x =  self.starting_path_sprite.rect.x
            self.game.events.ludo_token.rect.y =  self.starting_path_sprite.rect.y
    
    def move_on_normal_path(self):

        self.move_val = self.token_path_indice[self.current_player_color][self.game.events.token_selector] + self.game.dice.dice_val
        indice_for_tile_to_move_to = self.team_path[self.current_player_color][self.move_val]
        destination_path_tile = self.game.board.movement_path_sprites[indice_for_tile_to_move_to]
        
        #Check for collisions here before changing the coordinates of the token
        self.player_on_player_collision(indice_for_tile_to_move_to)
        
        self.game.events.ludo_token.rect.x = destination_path_tile.rect.x
        self.game.events.ludo_token.rect.y = destination_path_tile.rect.y

        self.token_path_indice[self.current_player_color][self.game.events.token_selector] = self.move_val
        self.token_movement_counter[self.current_player_color][self.game.events.token_selector] = self.game.events.movement_checker
    
    def move_on_winning_path(self):
        if self.game.events.movement_checker > self.settings.winning_path_threshold: # This condition works if the dice value is greater than the amount needed to finish with token

            self.game.events.movement_checker -= self.game.dice.dice_val
            self.token_movement_counter[self.current_player_color][self.game.events.token_selector] = self.game.events.movement_checker

            if len(self.current_player_token_group) == 1:
                self.game.dice.dice_val_holder = [] 
            
            self.game.menu.skipped_turn_text = "Cannot move with steps that are beyond the dungeon, turn skipped..."
            self.game.menu.is_turn_skip = True

        elif self.game.events.movement_checker == self.settings.winning_path_threshold:
            self.current_player_token_group.remove(self.current_player_token_group[self.game.events.token_selector])
            self.token_movement_counter[self.current_player_color].remove(self.token_movement_counter[self.current_player_color][self.game.events.token_selector])
            self.token_path_indice[self.current_player_color].remove(self.token_path_indice[self.current_player_color][self.game.events.token_selector])
            self.current_player_placeholder_group.remove(self.current_player_placeholder_group[self.game.events.token_selector])

            # Check to see if the list is empty for winning
            
            if not self.current_player_token_group:
                temp_color = self.current_player_color
                # Resetting all the players
                self.game.player.initialize_player_vars()
                
                # Resetting all the board elements
                self.game.board.initialize_board_vars()

                # Deleting all the dice elements
                self.game.dice.initialize_dice_vars()

                # Resetting all the menu elements
                self.game.menu.initialize_menu_vars()

                # Setting the following variable to true to access the final menu
                self.game.menu.is_final_menu = True

                self.game.menu.final_menu(temp_color)

                self.game.initialize()
            
            self.game.menu.skipped_turn_text = "Player " + str(self.current_player) + "'s token has reached the dungeon!"
            self.game.menu.is_turn_skip = True

            
        else:
            self.winning_path_mapping_indice = self.game.events.movement_checker - self.settings.total_movement_steps
            destination_winning_path_tile_indice = self.winning_path[self.current_player_color][self.winning_path_mapping_indice]
            
            self.current_winning_path_tile_list = self.game.board.winning_path_dict[self.current_player_color]
            
            destination_winning_path_tile = self.current_winning_path_tile_list[destination_winning_path_tile_indice]
            self.game.events.ludo_token.rect.x, self.game.events.ludo_token.rect.y = destination_winning_path_tile.rect.x, destination_winning_path_tile.rect.y
            self.token_movement_counter[self.current_player_color][self.game.events.token_selector] = self.game.events.movement_checker 

    def player_on_player_collision(self, indice_of_team_path_list):
        
        safe_path_collision_condition = (indice_of_team_path_list == self.settings.red_starting_path) or (indice_of_team_path_list == self.settings.green_starting_path) or (indice_of_team_path_list == self.settings.blue_starting_path) or (indice_of_team_path_list == self.settings.yellow_starting_path)
        
        if not safe_path_collision_condition:
            for enemy_player, color in enumerate(self.color_for_player):

                # This if condition is to ensure we don't encounter with the current player's color (which would be overlapping onto itself if it was considered.)
                if color != self.current_player_color:
                    for current_token_indice, current_token in enumerate(self.token_sprite_list[color]):
                        
                        indice_for_team_path_list = self.token_path_indice[color][current_token_indice]
                        total_step_taken_by_current_token = self.token_movement_counter[color][current_token_indice]

                        current_token_path_indice = self.team_path[color][indice_for_team_path_list]

                        # The collision has taken place
                        if current_token_path_indice == indice_of_team_path_list and (total_step_taken_by_current_token <= self.settings.total_movement_steps):
                            # access the placeholder sprite
                            current_placeholder_sprite = self.collision_placeholder_chooser(color)[current_token_indice]

                            # show the animation of getting destroyed

                            # putting the piece back to base
                            current_token.rect.x, current_token.rect.y = current_placeholder_sprite.rect.x, current_placeholder_sprite.rect.y
                            self.token_sprite_list[color][current_token_indice] = current_token
                            self.token_path_indice[color][current_token_indice] = 0
                            self.token_movement_counter[color][current_token_indice] = 0