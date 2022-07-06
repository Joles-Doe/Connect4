### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###
import time
import pygame
pygame.init()
# Imports ^

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
    pygame.display.set_caption('Test')

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

def reset_grid():
    grid_dictionary = {} # Dictionary
    for x in range(0, 6): # Dynamic variable which automatically rewrites the grid
        grid_dictionary["row{0}".format(x)] = ['-', '-', '-', '-', '-', '-', '-']
    return(grid_dictionary) # Returns dictionary
    # print(grid_dictionary["row2"][2]) # Debug



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

def counter_array(column, row):
    global counterlist
    counterlist = []
    counterlist.append(int(f"{column}{row}"))

def winner_message(playersign):
    if playersign == 'X':
        player = 'red'
    else:
        player = 'yellow'
    font_style = pygame.font.SysFont(None, 50)
    message = font_style.render('Congratulations, {} player, you won!'.format(player), True, black)
    message_rect = message.get_rect(center = (740 / 2, 640 / 2))
    screen.blit(message, message_rect)
    pygame.display.flip()
    time.sleep(3)

### Begin game ###
grid = reset_grid() # creates a new grid
playersign = 'S' # Resets player order


x = False
column = 0
while x == False:
    for event in pygame.event.get():
        draw_board(grid)
        win = check_winner(grid, playersign)
        if win == True:
            screen.blit(board, (0,0))
            pygame.display.flip()
            print('win')
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

winner_message(playersign)