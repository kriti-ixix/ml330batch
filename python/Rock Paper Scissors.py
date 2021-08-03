import os
import random as r

def clearScreen():
    if os.name == 'posix':
        # For UNIX Systems
        os.system('clear')
    else:
        # For Windows
        os.system('cls')


x = input("First player's move: ")
clearScreen()
#y = input("Second player's move: ")
#clearScreen()
y = r.choice(['rock', 'paper', 'scissor'])

x = x.lower()
y = y.lower()

print("X chose {x1} and Y chose {y1}".format(x1=x, y1=y))

if (x=='rock' and y=='scissor') or (x=='paper' and y=='rock') or (x=='scissor' and y=='paper'):
    print("X is the winner!")
elif (y=='rock' and x=='scissor') or (y=='paper' and x=='rock') or (y=='scissor' and x=='paper'):
    print("Y is the winner!")
else:
    print("No winner")

