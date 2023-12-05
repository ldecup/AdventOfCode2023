import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

scratchData = []
for line in inData:
    card = []
    card.append(int(re.findall(r'\d+',line.rstrip('\n').split(":")[0])[0]))
    card.append(re.findall(r'\d+',line.rstrip('\n').split(":")[1].split("|")[0]))
    card.append(re.findall(r'\d+',line.rstrip('\n').split(":")[1].split("|")[1]))
    card.append("0") #Storing those as strings to avoid finding them with "if cardId in subCard"
    card.append("1") #There is probably cleaner, but that avoids a visible loop
    scratchData.append(card)

#[ID,winningNB,playerNB,nbOfWins,nbOfCards]
    
#Compute wins per card, and part 1
totalValue = 0
for card in scratchData:
    nbOfWins = 0
    cardValue = 0
    for winningNb in card[1]:
        if winningNb in card[2]:
            #Part 1 ---
            if cardValue == 0:
                cardValue = 1
            else:
                cardValue = cardValue*2
            #Part 1 ---
            nbOfWins += 1
    card[3] = str(nbOfWins)
    totalValue += cardValue

#Part 2
totalNbOfCards = 0
for index,card in enumerate(scratchData):
    nbOfWins = int(card[3])
    for a in range(nbOfWins):
        cardId = card[0]+1+a
        for subCard in scratchData:
            if cardId in subCard:
                subCard[4] = str(int(subCard[4])+int(card[4])) #The main casualty of storing data as strings :(
                break
    totalNbOfCards += int(card[4])    

print("Total value for part 1: " + str(totalValue))
print("Total number of scratchcards for part 2: " + str(totalNbOfCards))