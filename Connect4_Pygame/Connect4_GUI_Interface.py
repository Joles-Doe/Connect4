### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###
import time
import pygame
from Connect4_Logic_GUI import * # Imports all the functions from a separate file
pygame.init()
# Imports ^

def print_grid(grid):
    for x in reversed(list(grid.values())):
        print(x)

class gamecolours():
    global red, blue, lightblue, yellow, white, slate
    red = (255, 0, 0)
    blue = 	(0, 0, 255)
    lightblue = (111, 187, 211)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
    slate = (112, 128, 144)

class gamescreen():
    global screen
    screen = pygame.display.set_mode((740, 740)) #width, height
    pygame.display.set_caption('Test')

def draw_board(grid, playersign, row, column):
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
            if row == 'PASS':
                colour = white
            else:
                if x == column and y == row:
                    if playersign == 'X':
                        colour = red
                    else:
                        colour = yellow
            pygame.draw.circle(board, colour, (xoffset + (x * circlewidth), yoffset + (y * circleheight)), radius)

def draw_carot(column):
    pygame.draw.line(board, red, [44 + (column * 100), 680], [69 + (column * 100), 630], 10) # make a carot
    pygame.draw.line(board, red, [94 + (column * 100), 680], [69 + (column * 100), 630], 10)

