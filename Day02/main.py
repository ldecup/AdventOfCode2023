import os

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

class game:
    def __init__(self, id, sets, feasible, localMax):
        self.id = id
        self.sets = sets
        self.feasible = feasible
        self.localMax = localMax

data = []
for line in inData:
    data.append(line.rstrip('\n'))

def parseGame(data):
    gameData = game(None,[],True,[0,0,0])
    gameData.id = data.split(":")[0].split(" ")[1]
    sets = data.split(":")[1].split(";")
    for set in sets:
        currentSetAsStrings = set.split(",")
        currentSet = []
        for info in currentSetAsStrings:
            currentSet.append(info.lstrip(" ").split(" "))
        gameData.sets.append(currentSet)
    return gameData

def computeFeasibility(game, numRed, numGreen, numBlue):
    for set in game.sets:
        setTotals = [0,0,0] #RGB
        for hand in set:
            if hand[1] == "red":
                setTotals[0] = setTotals[0] + int(hand[0])
                if game.localMax[0] < int(hand[0]):
                    game.localMax[0] = int(hand[0])
            elif hand[1] == "green":
                setTotals[1] = setTotals[1] + int(hand[0])
                if game.localMax[1] < int(hand[0]):
                    game.localMax[1] = int(hand[0])
            elif hand[1] == "blue":
                setTotals[2] = setTotals[2] + int(hand[0])
                if game.localMax[2] < int(hand[0]):
                    game.localMax[2] = int(hand[0])
        game.feasible = ((setTotals[0] <= numRed) and (setTotals[1] <= numGreen) and (setTotals[2] <= numBlue)) and game.feasible

gameList = []
for datum in data:
    gameList.append(parseGame(datum))

idTotal = 0
powerTotal = 0
for game in gameList:
    computeFeasibility(game, 12, 13, 14)
    if game.feasible:
        idTotal = idTotal + int(game.id)
    powerTotal = powerTotal + game.localMax[0]*game.localMax[1]*game.localMax[2]

print(idTotal)
print(powerTotal)

