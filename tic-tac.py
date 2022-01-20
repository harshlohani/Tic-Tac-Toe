#Implementation of Two Player Tic-Tac-Toe game in Python.
from re import X
# FIXME: better names for packages
import file1

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,    # added key:value pairs      # dictionary data type
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []       # creating an empty list whi will be used to restart game 
for i in theBoard:
    board_keys.append(i)        # inserting boardkeys with values which will be used to reset theBoard

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):                  # creating the physical board
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

x_name1=file1.x_name     #holds the name of player1
o_name2=file1.o_name     #holds the name of player2


print("the first player is",x_name1,"\nThe second player is",o_name2)   #print statement showing the names of player 1 & player 2

# Now we'll write the main function which has all the gameplay functionality.

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        
        if (turn=='X'):
            print("It's your turn," + x_name1 + ".Your next move.")
        elif(turn=='O'):
            print("It's your turn," + o_name2 + ".Your next move.")
    
        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:

            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****")            
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                if (turn=='X') : 
                    print(" **** " +x_name1 + " won. ****")    
                else :
                    print(" **** " +o_name2 + " won. ****") 
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        # FIXME: remove unused vars
        counter=0
        # FIXME: use constants instead of using literals everywhere
        if (turn =='X'):
            turn = 'O'
        else:
            turn = 'X'  
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for i in board_keys:
            theBoard[i] = " "

        game()

if __name__ == "__main__":
    game()