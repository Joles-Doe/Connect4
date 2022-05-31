### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###
import time

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
    if playersign == 'S' or 'Y':
        return 'X'
    elif playersign == 'X':
        return 'Y'

class UserRetry(Exception): # Custom exception to reset the place_counter loop
    pass

def place_counter(playersign, grid):
    while True:
        try: # Try except loop to prevent letters from being entered
            column = (int(input('Please enter the column you wish to place your counter in '))) - 1 # Column input
            if (grid["row{row}".format(row = 5)][column] != '-'): # Checks for if the column is already full
                print('That column is full, please choose another column')
                raise(UserRetry) # Resets the loop
            else:
                break
        except UserRetry: # Custom exception to reset the loop
            pass
        except:
            print('Please enter a column between 1-7')
    
    row = 0
    while True:
        if (grid["row{row}".format(row = row)][column] != '-'): # Automatically finds the lowest point in the grid
            row += 1
        else:
            grid["row{row}".format(row = row)][column] = playersign # Replaces the current value with the current player's sign
            return grid
        
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