import time
from Connect4_Logic import * # Imports all the functions from a separate file
from Connect4_GUI import * # Imports GUI **[subject to change]**
# Imports ^

### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###

### Begin / Reset game ###
grid = reset_grid() # creates a new grid
# print(grid["row3"][3]) # Debug

playersign = 'S' # Resets player order

intro_message()

Game = False
while (Game == False): # While loop to play until someone wins
    print_grid(grid)
    playersign = current_player(playersign)
    grid = place_counter(playersign, grid)
    time.sleep(2)
    if check_winner(grid, playersign) == True:
        break

winner_message(playersign)

### Winner segment here, where the condition is check_winner == True ###