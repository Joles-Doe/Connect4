import time
from Connect4_Logic import * # Imports all the functions from a separate file
from Connect4_GUI import * # Imports GUI **[subject to change]**
import pygame
pygame.init()
import os
# Imports ^

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###

### Begin / Reset game ###
grid = reset_grid() # creates a new grid
playersign = 'S' # Resets player order





### Winner segment here, where the condition is check_winner == True ###