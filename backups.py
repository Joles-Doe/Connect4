def check_winner(grid, playersign):
    diagonal = False
    vertical = False # While loops
    horizontal = False
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
    # Vrow = 0
    # Vcolumn = 0
    # while (vertical == False): # Vertical check
    #     Vrow_1 = Vrow # Temporary row variable to prevent errors
    #     if Vrow == 6:
    #         vertical = True # Breaks the loop if all the rows have been iterated through
    #         break
    #     for x in range(7): # Checks the whole row
    #         if counter == 4:
    #             return True # Returns true if it finds a 4 in a row
    #         if (grid["row{row}".format(row = Vrow_1)][Vcolumn] == playersign): # Checks if current position is the same as the current player
    #             counter += 1
    #             Vrow_1 += 1
    #             for x in range(3): #Additional loop to check the next 3 rows
    #                 if (grid["row{row}".format(row = Vrow_1)][Vcolumn] == playersign):
    #                     counter += 1
    #                     Vrow_1 += 1 #Moves onto the next row
    #                 else:
    #                     Vrow_1 = Vrow
    #                     Vcolumn += 1 # Resets values, moves onto next column and breaks the inside loop
    #                     counter = 0
    #                     break
    #         else:
    #             Vcolumn += 1 # Moves onto the next column, reset counter
    #             counter = 0
    #     Vrow +=1 # Moves onto the next row and resets the column
    #     Vcolumn = 0
    
    for Hrow in range(6):
        row_1 = grid["row{row}".format(row = Hrow)]
        row_str = "".join(row_1)
        if playersign * 4 in row_str:
            return True
        # Hcolumn_1 = Hcolumn # Temporary row variable to prevent errors
        # if Hrow == 6:
        #     horizontal = True
        #     break
        # for x in range(4):
        #     if counter == 4:
        #         return True
        #     if (grid["row{row}".format(row = Hrow)][Hcolumn_1] == playersign):
        #         counter += 1
        #         Hcolumn_1 += 1
        #         for x in range(3):
        #             if (grid["row{row}".format(row = Hrow)][Hcolumn_1] == playersign):
        #                 counter += 1
        #                 Hcolumn_1 += 1
        #             else:
        #                 Hcolumn_1 = Hcolumn + 1
        #                 counter = 0
        #                 break










import time
# Imports ^

### Connect 4 = {7 columns, 6 rows} ###
### player 1 counters are defined by 'X', player 2 counters are defined by 'Y' ###
### Rows are inverted - for example: row5 is the bottom row ###

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

grid = reset_grid() # creates a new grid
# print(grid["row3"][3]) # Debug



### main segment here ###

### Winner segment here, where the condition is check_winner == True ###

current_player = 0

if current_player == 0:
    playersign = 'X'
else:
    playersign = 'Y'