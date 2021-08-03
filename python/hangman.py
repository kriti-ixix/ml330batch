from icecream import ic
import random as r

def uniqueChars(movieChars):
    uniqueList = []
    
    for char in movieChars:
        if char==" ":
            continue
        if char not in uniqueList:
            uniqueList.append(char)
            
    return uniqueList

def printMovie():
    print('')
    for x in movieChosen:
        if x==" ":
            print(" ", end="")
        elif x in charsGuessed:
            print(x, end=" ")
        elif x not in charsGuessed:
            print("_", end=" ")

listOfMovies = ['SPIDERMAN', 'THOR RAGNAROK', 'JUSTICE LEAGUE', 'KNIGHT AND DAY', 'MEAN GIRLS']
movieChosen = r.choice(listOfMovies)
ic (movieChosen)

movieChars = list(movieChosen)
uniqueList = uniqueChars(movieChars)
charsChosen = r.sample(uniqueList, k=3)

charsGuessed = []
charsGuessed.extend(charsChosen)
#ic(charsGuessed)

guessesLeft = 10

while True:
    printMovie()
    ic (charsGuessed)
    if guessesLeft==0:
        print("\nYou ran out of guesses. Sorry!")
        break
        
    if len(charsGuessed)==len(uniqueList):
        print("\nCongratulations! You guessed it correctly with {} guesses left".format(guessesLeft))
        break
        
    charPicked = input("Guesses Left: {}\nEnter your guess: ".format(guessesLeft))
    charPicked = charPicked.upper()
    if charPicked in charsGuessed:
        print("\nYou guessed that already")
        continue
        
    if charPicked not in uniqueList:
        print("Oops! Wrong guess")
    elif charPicked in uniqueList:
        print("You guessed correctly!")
        charsGuessed.append(charPicked)
        
    guessesLeft -= 1 