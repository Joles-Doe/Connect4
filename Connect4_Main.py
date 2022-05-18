import time
from Connect4_Logic import * # Imports all the functions from a separate file
from Connect4_GUI import * # Imports GUI **[subject to change]**
# Imports ^

### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###

grid = reset_grid() # creates a new grid
# print(grid["row3"][3]) # Debug



### main segment here ###

### Winner segment here, where the condition is check_winner == True ###

current_player = 0

if current_player == 0:
    playersign = 'X'
else:
    playersign = 'Y'