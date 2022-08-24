### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###

### This program will continue to work until https://keyvalue.immanuel.co stops working ###

import time
import pygame
import sys
import requests
import urllib
pygame.init()
# pygame.key.set_repeat(500, 50)
# Imports ^

# Class to interact with the online database
class KVScore:
    BASE_URL = "https://keyvalue.immanuel.co/api/KeyVal/"
 
    def __init__(self, app_key=None):
        if app_key:
            self.app_key = app_key
        else:
            self.get_app_key()
 
    def get_app_key(self):
        resp = requests.get(f"{self.BASE_URL}/GetAppKey")
        print(resp.status_code)
        self.app_key = resp.text[1:-1]
 
    def set_value(self, key, value):
        encoded_value = urllib.parse.quote(value)
        resp = requests.post(
            f"{self.BASE_URL}/UpdateValue/{self.app_key}/{key}/{encoded_value}"
        )
        return resp
 
    def get_value(self, key):
        resp = requests.get(
            f"{self.BASE_URL}/GetValue/{self.app_key}/{key}"
        )
        if not resp.ok:
            return
        return resp.text[1:-1]
 
    def encode_data(self, grid, playersign):
        s = ""
        for x in range(0, 6):
            s += "".join(grid[f"row{x}"])
        s += playersign
        return s
 
    def decode_data(self, data):
        try:
            grid = {}
            for x in range(0, 6):
                grid[f"row{x}"] = list(data[x*7:(x+1)*7])
    
            playersign = data[-1]
            return grid, playersign
        except IndexError:
            grid = 'FAILED'
            playersign = 'FAILED'
            return grid, playersign
 
    def store_game(self, game_id, grid, playersign):
        self.set_value(game_id, self.encode_data(grid, playersign))
 
    def get_game(self, game_id):
        data = self.get_value(game_id)
        if data is None:
            return 'FAILED', 'FAILED'
        return self.decode_data(data)


# Logic functions
def reset_grid():
    grid_dictionary = {} # Dictionary
    for x in range(0, 6): # Dynamic variable which automatically rewrites the grid
        grid_dictionary["row{0}".format(x)] = ['-', '-', '-', '-', '-', '-', '-']
    return(grid_dictionary) # Returns dictionary
    # print(grid_dictionary["row2"][2]) # Debug


def current_player(playersign): # Switches the current player
    if playersign == 'S' or playersign == 'Y':
        return 'X'
    elif playersign == 'X':
        return 'Y'


def place_counter(playersign, grid, column):
    if (grid["row{row}".format(row = 5)][column] != '-'): # Checks for if the column is already full
        print('That column is full, please choose another column')
        return False
    row = 0
    while True:
        if (grid["row{row}".format(row = row)][column] != '-'): # Automatically finds the lowest point in the grid
            row += 1
        else:
            grid["row{row}".format(row = row)][column] = playersign # Replaces the current value with the current player's sign
            return grid


def check_winner(grid, playersign):
    diagonal = False # While loop
    counter = 0 # Counter

    Drow = 0
    Dcolumn = 0
    while (diagonal == False): # Diagonal check
        if Drow == 3: # Checks if no more checks need to be done
            diagonal = True # Ends the loop
            counter = 0
            break
        if Dcolumn in [0, 1, 2]: # Checks right diagonal
            Rrow = Drow
            Rcolumn = Dcolumn
            for x in range(4):
                if (grid["row{row}".format(row = Rrow)][Rcolumn] == playersign): # Checks if the current counter is the same as the current player's
                    counter += 1
                    Rrow += 1 # Moves on to the next counter
                    Rcolumn += 1
                else:
                    break

        if Dcolumn == 3: #Checks middle diagonal
            MrowRight = Drow
            McolumnRight = Dcolumn
            MrowLeft = Drow
            McolumnLeft = Dcolumn
            for x in range(4):
                if (grid["row{row}".format(row = MrowRight)][McolumnRight] == playersign): # Checks if the current counter is the same as the current player's
                    counter += 1
                    MrowRight += 1 # Moves on to the next counter
                    McolumnRight += 1
                else:
                    counter = 0
                    break
            if counter == 4:
                return True
            for x in range(4):
                if (grid["row{row}".format(row = MrowLeft)][McolumnLeft] == playersign):
                    counter += 1
                    MrowLeft += 1 # Moves on to the next counter
                    McolumnLeft -= 1
                else:
                    break
        
        if Dcolumn in [4, 5, 6]: # Checks left diagonal
            Lrow = Drow
            Lcolumn = Dcolumn
            for x in range(4):
                if (grid["row{row}".format(row = Lrow)][Lcolumn] == playersign): # Checks if the current counter is the same as the current player's
                    counter += 1
                    Lrow += 1 # Moves on to the next counter
                    Lcolumn -= 1
                else:
                    break
            
        if counter == 4: # Checks for if the current player has won
            return True
        else:
            counter = 0
            Dcolumn += 1 # Resets counter and moves onto the next column

        if Dcolumn == 8:
            Dcolumn = 0 # Resets the column and moves onto the next row
            Drow += 1
    
    for Vcolumn in range(7):
        s = ""
        for Vrow in range(6):
            s += grid["row{row}".format(row = Vrow)][Vcolumn]
        if playersign * 4 in s:
            return True
    
    for Hrow in range(6):
        row_1 = grid["row{row}".format(row = Hrow)]
        row_str = "".join(row_1)
        if playersign * 4 in row_str:
            return True

    return False # Returns false if there isn't 4 in a row


# Pygame-related functions and classes
class gamecolours():
    global red, blue, lightblue, yellow, white, slate, black
    red = (255, 0, 0)
    blue = (0, 0, 255)
    lightblue = (111, 187, 211)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
    slate = (112, 128, 144)
    black = (0, 0, 0)


class gamescreen():
    global screen
    screen = pygame.display.set_mode((740, 740)) #width, height
    pygame.display.set_caption('Connect 4')


def draw_board(grid):
    global board
    board = pygame.Surface((screen.get_size()))
    board.fill(slate)
    pygame.draw.rect(board, lightblue, [0, 0, 740, 640])
    radius = 40
    xoffset = 70
    yoffset = 70
    circlewidth = 100
    circleheight = 100
    colour = white
    for x in range(7):
        for y in range(6):
            sign = grid["row{row}".format(row = 5 - y)][x]
            if sign == 'X':
                colour = red
            elif sign == 'Y':
                colour = yellow
            else:
                colour = white
            pygame.draw.circle(board, colour, (xoffset + (x * circlewidth), yoffset + (y * circleheight)), radius)


def draw_carot(column):
    pygame.draw.line(board, red, [44 + (column * 100), 680], [69 + (column * 100), 630], 10) # make a carot
    pygame.draw.line(board, red, [94 + (column * 100), 680], [69 + (column * 100), 630], 10)


def create_message(message, x, y, fontstyle=None):
    if fontstyle is None:
        fontstyle = pygame.font.SysFont(None, 70) # Defaults to a size 70 font
    messageid = fontstyle.render(message, True, white)
    message_rectid = messageid.get_rect(center = (x, y)) # Message container
    screen.blit(messageid, message_rectid)
    pygame.display.flip()
    return message_rectid


def winner_message(playersign, chosenplayer):
    font_style = pygame.font.SysFont(None, 50)
    if playersign == chosenplayer:
        create_message('Congratulations, you won!', 370, 320, font_style)
    else:
        create_message('Unfortunately, you lost :(', 370, 320, font_style)
    time.sleep(3)


def winner_messagelocal(playersign):
    if playersign == 'X':
        player = 'red'
    else:
        player = 'yellow'
    font_style = pygame.font.SysFont(None, 50)
    create_message('Congratulations, {} player, you won!'.format(player), 370, 320, font_style)
    time.sleep(3)

# Pygame gameplay loops
def main_menu():
    def clear():
        menu.fill(black)
        screen.blit(menu, (0,0))
        pygame.display.flip()

    mouse = pygame.mouse.get_pos() # mouse
    menu = pygame.Surface((screen.get_size()))
    font_style = pygame.font.SysFont(None, 50)
    font_style_title = pygame.font.SysFont(None, 100)
    create_message('CONNECT 4', 370, 100, font_style_title)
    message_rectlocal = create_message('Local play', 370, 270, font_style)
    message_rectcreate = create_message('Create a game', 370, 370, font_style)
    message_rectjoin = create_message('Join a game', 370, 470, font_style)
    x = False
    while x == False:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos() # mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if message_rectlocal.collidepoint(mouse[0], mouse[1]):
                            clear()
                            return 'LOCAL'
                        elif message_rectcreate.collidepoint(mouse[0], mouse[1]):
                            clear()
                            return 'CREATE'
                        elif message_rectjoin.collidepoint(mouse[0], mouse[1]):
                            clear()
                            return 'JOIN'
            pygame.display.flip()
            if event.type == pygame.QUIT:
                x = True


def game_create(grid, playersign):
    game_id = 'CONNECT4'
    kv_store = KVScore()
    kv_store.store_game(game_id, grid, playersign)
    menu = pygame.Surface((screen.get_size()))
    create_message('Your ID is "{}"'.format(kv_store.app_key), 370, 170)
    create_message('share this with the other player', 370, 230)
    create_message('Game will start upon', 370, 430)
    create_message('second player joining', 370, 490)
    wait = False
    while wait == False:
        grid, playersign = kv_store.get_game(game_id)
        print(playersign)
        if playersign != 'S':
            print('Game start')
            wait = True
            menu.fill(black)
            screen.blit(menu, (0,0))
            pygame.display.flip()
        pygame.event.pump()
        pygame.time.wait(3000)
    return kv_store.app_key


def game_join():
    def check_real(text):
        game_id = 'CONNECT4'
        kv_store = KVScore(app_key = text)
        grid, playersign = kv_store.get_game(game_id)
        print(playersign)
        if grid == 'FAILED' and playersign == 'FAILED':
            create_message('Invalid ID, please check', 370, 420)
            create_message('if the ID is correct', 370, 480)
            pygame.event.pump()
            pygame.time.wait(2000)
            return False
        else:
            return True
    menu = pygame.Surface((screen.get_size()))
    join = False
    text = ''
    menu.fill(black)
    screen.blit(menu, (0,0))
    create_message('Please enter the game ID', 370, 130)
    while join == False:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                if event.key == pygame.K_RETURN:
                    print(text)
                    isreal = check_real(text)
                    if isreal == True:
                        print('Game joined')
                        kv_store = KVScore(app_key = text)
                        game_id = 'CONNECT4'
                        grid, playersign = kv_store.get_game(game_id)
                        playersign = current_player(playersign)
                        kv_store.store_game(game_id, grid, playersign)
                        menu.fill(black)
                        screen.blit(menu, (0,0))
                        pygame.display.flip()
                        join = True
                        break
                    else:
                        menu.fill(black)
                        create_message('Please enter the game ID', 370, 130)
                        text = ''
                else:
                    menu.fill(black)
                    screen.blit(menu, (0,0))
                    text += event.unicode
                    create_message('Please enter the game ID', 370, 130)
                    create_message('{}'.format(text), 370, 220)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    return kv_store.app_key


def game_local(grid, playersign):
    x = False
    column = 0
    while x == False:
        for event in pygame.event.get():
            draw_board(grid)
            win = check_winner(grid, playersign)
            if win == True:
                screen.blit(board, (0,0))
                pygame.display.flip()
                winner_messagelocal(playersign)
                x = True
                break        
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if column == 0:
                            pass
                        else:
                            column -= 1
                    elif event.key == pygame.K_RIGHT:
                        if column == 6:
                            pass
                        else:
                            column += 1
                    elif event.key == pygame.K_RETURN:
                        playersign = current_player(playersign)
                        grid_temp = grid
                        grid = place_counter(playersign, grid, column)
                        if grid == False:
                            grid = grid_temp
            draw_carot(column)
            screen.blit(board, (0,0))
            pygame.display.flip()
            if event.type == pygame.QUIT:
                x = True


def game_online(chosenplayer, appkey):
    game_id = 'CONNECT4'
    kv_store = KVScore(app_key=appkey)
    x = False
    placed = False
    column = 0
    while x == False:
        grid, playersign = kv_store.get_game(game_id)
        if playersign == chosenplayer:
            placed = False
            while placed == False:
                win = check_winner(grid, playersign)
                if win == True:
                    screen.blit(board, (0,0))
                    pygame.display.flip()
                    winner_message(playersign, chosenplayer)
                    x = True
                    break
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        x = True
                    draw_board(grid)    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if column == 0:
                                pass
                            else:
                                column -= 1
                        elif event.key == pygame.K_RIGHT:
                            if column == 6:
                                pass
                            else:
                                column += 1
                        elif event.key == pygame.K_RETURN:
                            placed = True
                            grid_temp = grid
                            grid = place_counter(playersign, grid, column)
                            if grid == False:
                                placed = False
                                grid = grid_temp
                    draw_carot(column)
                    screen.blit(board, (0,0))
                    pygame.display.flip()
                    if placed == True:
                        playersign = current_player(playersign)
                        kv_store.store_game(game_id, grid, playersign)
                        win = check_winner(grid, playersign)
                        if win == True:
                            screen.blit(board, (0,0))
                            pygame.display.flip()
                            winner_message(playersign, chosenplayer)
                            x = True
                            break
                        break
        draw_board(grid)
        screen.blit(board, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.wait(1000)


### Begin ###
grid = reset_grid() # creates a new grid
playersign = 'S' # Resets player order
start = main_menu()

if start == 'LOCAL':
    game_local(grid, playersign)
elif start == 'CREATE':
    appkey = game_create(grid, playersign)
    chosenplayer = 'X'
    game_online(chosenplayer, appkey)
elif start == 'JOIN':
    appkey = game_join()
    chosenplayer = 'Y'
    game_online(chosenplayer, appkey)