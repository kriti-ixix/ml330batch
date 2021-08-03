#Importing the libraries
import random

#User-defined functions

#Function to build a deck 
#Return: deck -> list
def buildDeck():
    deck = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
    wilds = ["Wild", "Wild Draw Four"]

    for colour in colours:
        for value in values:
            cardVal = colour + " " + value
            deck.append(cardVal)
            if value!="0":
                deck.append(cardVal)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck

#Function to draw a card 
#Return: cardsDrawn -> list
def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))

    return cardsDrawn

#Display the cards a user has currently 
#Returns: none
def showHand(player, playerHand):
    print("\nIt's " +  player + "'s turn ")
    print("Your Hand:")
    print("-------------------------------")
    y=1 

    for card in playerHand:
        print("{}) {}".format(y, card))
        y+=1 

#Checking whether user can play a card or not
#Return: boolean
def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True 
        elif colour in card or value in card:
            return True 
    return False


unoDeck = buildDeck()
random.shuffle(unoDeck)
print(unoDeck)
discards = [] 

players = [] #List to store the cards of all players
playerNames = [] #List to store the names of the players
numPlayers = int(input("\nHow many players? "))

#Adding players to the list and each draws five cards
for x in range(numPlayers):
    name = input("Enter player's name: ")
    playerNames.append(name)
    players.append(drawCards(5))

print("\nThe cards are: ")
for (x, y) in zip(players, playerNames):
    print("The player {} has: {}".format(y, x))

#Initialising the game
playerTurn = 0
playDirection = 1
playing = True

#Making a discards pile
discards.append(unoDeck.pop(0))
#Getting the colour and value of the card on top of the discards pile
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]

if currentColour!= "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

#Starting the game
while playing:
    showHand(playerNames[playerTurn], players[playerTurn])
    print("\nCard on top of the discard pile: ", discards[-1])
    
    #If the user has a card that they can play
    if canPlay(currentColour, cardVal, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play? "))

        #If the user gave a card number that doesn't exist in their deck
        while cardChosen>len(players[playerTurn]):
            cardChosen = int(input("Invalid option. Which card do you want to play? "))

        cardPlayed = players[playerTurn][cardChosen-1]
        
        #If the user chose a card from his deck that he cannot play
        while not canPlay(currentColour, cardVal, [cardPlayed]):
            cardChosen = int(input("Invalid card. Which card do you want to play? "))
            while cardChosen>len(players[playerTurn]):
                cardChosen = int(input("Invalid option. Which card do you want to play? "))
            cardPlayed = players[playerTurn][cardChosen-1]

        print("You played", cardPlayed)
        players[playerTurn].pop(cardChosen-1) #Removing it from the players deck
        discards.append(cardPlayed) #Adding the card played to the discards pile

        #Checking for wins
        if len(players[playerTurn])==0:
            winner = playerNames[playerTurn]
            playing = False
        else:
            #Checking for special cards
            splitCard = discards[-1].split(" ", 1)
            currentColour = splitCard[0]

            #Checking for wild card
            if len(splitCard)==1:
                cardVal = "Any"
            else:
                #Not a wild card
                cardVal = splitCard[1]

            if (currentColour=="Wild"):
                print("1. Red\t2. Green\t3. Yellow\t4. Blue")
                newColour = input("Which colour do you choose? ")
                currentColour = newColour

            #Checking for other special cards
            if cardVal == 'Reverse':
                playDirection = playDirection * -1
            elif cardVal == 'Skip':
                pass
            elif cardVal == 'Draw Two':
                pass
            elif cardVal == 'Draw Four':
                pass

    #The user has no card they can play
    else:
        input("Press enter to draw a card")
        players[playerTurn].extend(drawCards(1))

    #Next player's turn
    playerTurn += playDirection
    if playerTurn >= numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers - 1

print("Game Over!") 
print(winner, " is the winner!")            