#Importing the libraries
import os
import random

#Global variables
print("Welcome to tic tac toe")

#Dictionary to store the moves
theBoard = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

#User-defined functions
def printBoard():
    print(theBoard['7'] + "|" + theBoard['8'] + "|" + theBoard['9'])
    print("-+-+-")
    print(theBoard['4'] + "|" + theBoard['5'] + "|" + theBoard['6'])
    print("-+-+-")
    print(theBoard['1'] + "|" + theBoard['2'] + "|" + theBoard['3'])

def playGame():
    #Initialising the turns and counter
    turn = 'X'
    count = 0

    while True:
        print("")
        printBoard()

        if count == 9:
            print("All the squares are filled")
            break
        
        if turn=='X':
            #Take input from the user
            move = input("\nMove to which place {}: ".format(turn))
            print("User's choice: ", move)
            
        else:
            computerChoice = list(filter(lambda x : theBoard[x]==" ", theBoard.keys()))
            move = random.choice(computerChoice)
            print("Computer's choice: ", move)

        #Checking if the square is empty
        if theBoard[move] == ' ':
            theBoard[move] = turn
            #Checking in case there is a winner
            winner = checkWin(turn)

            if winner!="":
                print("")
                printBoard()
                print("Congratulations! The winner is {}!".format(winner))
                break

            else:
                count += 1
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

        else:
            print("That place is already filled")
            continue

    print("\nGame Over")

def checkWin(turn):
    winner = ""

    #Checking rows
    if (theBoard['7']==theBoard['8']==theBoard['9']==turn) or (theBoard['4']==theBoard['5']==theBoard['6']==turn) or (theBoard['1']==theBoard['2']==theBoard['3']==turn):
        winner = turn

    #Checking columns
    if (theBoard['7']==theBoard['4']==theBoard['1']==turn) or (theBoard['8']==theBoard['5']==theBoard['2']==turn) or (theBoard['9']==theBoard['6']==theBoard['3']==turn):
        winner = turn

    #Checking diagonals
    if (theBoard['7']==theBoard['5']==theBoard['3']==turn) or (theBoard['9']==theBoard['5']==theBoard['1']==turn):
        winner = turn

    return winner

def restartGame():
    choice = input("Would you like to restart? (Y/N): ").lower()
    if choice == 'y':
        os.system("clear")
        for values in theBoard:
            theBoard[values] = ' '
        main()
    else:
        print("Thank you for playing")

#Main function
def main():
    playGame()
    restartGame()

main()