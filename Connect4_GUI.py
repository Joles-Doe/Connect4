### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###
import time
import pygame
pygame.init()
# Imports ^



def print_grid(grid):
    for x in reversed(list(grid.values())):
        print(x)

def intro_message():
    print('Welcome to connect 4')
    time.sleep(1)
    print('The aim of the game is to get 4 counters in a row - diagonally, horizontally, or vertically.')
    time.sleep(1)
    print('The first player to achieve this wins!')
    time.sleep(1)
    print('Player 1 will start first, with their counter defined as "X"')
    time.sleep(1)
    print('Player 2 will follow, their counter defined as "Y"')
    time.sleep(1)
    print('Good luck, may the best player win!')

def winner_message(playersign):
    if playersign == 'X':
        player = '1'
    else:
        player = '2'
    print('Congratulations, player {}, you won!'.format(player))
