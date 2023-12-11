import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

pipeMap = []
for line,lineData in enumerate(inData):
    pipeMap.append('+'+lineData.rstrip('\n')+'+')
    sList = re.search('S',lineData)
    if sList != None:
        startPos = [line+1,sList.start()+1] #+1 because of the padding

#Pad the pipeMap with + to avoid bound issues
dummyLine = ""
for i in range(len(pipeMap[0])):
    dummyLine += "+"
pipeMap.insert(0,dummyLine)
pipeMap.append(dummyLine)

def readLegalMoves(currentPos,pipeMap):
    legalMoves = []
    currentLine = currentPos[0]
    currentCol = currentPos[1]
    if pipeMap[currentLine][currentCol] == 'S':
        #Check left
        if pipeMap[currentLine][currentCol-1] in ['-','L','F']:
            legalMoves.append([currentLine,currentCol-1])
        #Check right
        if pipeMap[currentLine][currentCol+1] in ['-','J','7']:
            legalMoves.append([currentLine,currentCol+1])
        #Check above
        if pipeMap[currentLine-1][currentCol] in ['|','F','7']:
            legalMoves.append([currentLine-1,currentCol])
        #Check below
        if pipeMap[currentLine+1][currentCol] in ['|','J','L']:
            legalMoves.append([currentLine+1,currentCol])
    elif pipeMap[currentLine][currentCol] == '-':
        #Check left
        if pipeMap[currentLine][currentCol-1] in ['-','L','F']:
            legalMoves.append([currentLine,currentCol-1])
        #Check right
        if pipeMap[currentLine][currentCol+1] in ['-','J','7']:
            legalMoves.append([currentLine,currentCol+1])
    elif pipeMap[currentLine][currentCol] == '|':
        #Check above
        if pipeMap[currentLine-1][currentCol] in ['|','F','7']:
            legalMoves.append([currentLine-1,currentCol])
        #Check below
        if pipeMap[currentLine+1][currentCol] in ['|','J','L']:
            legalMoves.append([currentLine+1,currentCol])
    elif pipeMap[currentLine][currentCol] == 'L':
        #Check right
        if pipeMap[currentLine][currentCol+1] in ['-','J','7']:
            legalMoves.append([currentLine,currentCol+1])
        #Check above
        if pipeMap[currentLine-1][currentCol] in ['|','F','7']:
            legalMoves.append([currentLine-1,currentCol])
    elif pipeMap[currentLine][currentCol] == 'J':
        #Check left
        if pipeMap[currentLine][currentCol-1] in ['-','L','F']:
            legalMoves.append([currentLine,currentCol-1])
        #Check above
        if pipeMap[currentLine-1][currentCol] in ['|','F','7']:
            legalMoves.append([currentLine-1,currentCol])
    elif pipeMap[currentLine][currentCol] == '7':
        #Check left
        if pipeMap[currentLine][currentCol-1] in ['-','L','F']:
            legalMoves.append([currentLine,currentCol-1])
        #Check below
        if pipeMap[currentLine+1][currentCol] in ['|','J','L']:
            legalMoves.append([currentLine+1,currentCol])
    elif pipeMap[currentLine][currentCol] == 'F':
        #Check right
        if pipeMap[currentLine][currentCol+1] in ['-','J','7']:
            legalMoves.append([currentLine,currentCol+1])
        #Check below
        if pipeMap[currentLine+1][currentCol] in ['|','J','L']:
            legalMoves.append([currentLine+1,currentCol])
    return legalMoves

def updateBounds(minPos,maxPos,currPos):
    tempMinPos = minPos
    tempMaxPos = maxPos
    if currPos[0] > tempMaxPos[0]: tempMaxPos[0] = currPos[0]
    if currPos[0] < tempMinPos[0]: tempMinPos[0] = currPos[0]
    if currPos[1] > tempMaxPos[1]: tempMaxPos[1] = currPos[1]
    if currPos[1] < tempMinPos[1]: tempMinPos[1] = currPos[1]

#Choose one of the 2 starting legal moves as the start position, the other one as the end position
currentPos = readLegalMoves(startPos,pipeMap)[0]
endPos = readLegalMoves(startPos,pipeMap)[1]
moveList = [startPos,currentPos]
minBoundPos = startPos.copy()
maxBoundPos = startPos.copy()
while currentPos != endPos:
    legalMoves = readLegalMoves(currentPos,pipeMap)
    for move in legalMoves:
        if move != moveList[-2]:
            currentPos = move
            moveList.append(move)
            updateBounds(minBoundPos,maxBoundPos,currentPos)
            break

print("Number of steps to the middle of the loop (part 1): " + str(int(len(moveList)/2)))

def isPointInPolygon(point,moveList):
    numberOfCrossings = 0
    #Those 3 lines were spit out verbatim by a LLM by the way. Outstanding.
    for i in range(len(moveList)):
        j = (i+1) % len(moveList)
        if ((moveList[i][1] > point[1]) != (moveList[j][1] > point[1])) and (point[0] < (moveList[j][0] - moveList[i][0]) * (point[1] - moveList[i][1]) / (moveList[j][1] - moveList[i][1]) + moveList[i][0]):
            numberOfCrossings += 1
    return numberOfCrossings % 2 == 1

#Strip the map to only the rectangle enclosing the main loop (to discard obviously irrelevant data points)
strippedPipeMap = []
for indexL,line in enumerate(pipeMap):
    if indexL >= minBoundPos[0] and indexL <= maxBoundPos[0]:
        tempLine = ''
        for indexC,char in enumerate(line):
            if indexC >= minBoundPos[1] and indexC <= maxBoundPos[1]:
                tempLine += char
        strippedPipeMap.append(tempLine)

#Real slow (like 15-20s)
pointsInLoop = []
for line in range(len(pipeMap)):
    for col in range(len(pipeMap[0])):
        if isPointInPolygon([line,col],moveList) and [line,col] not in moveList:
            pointsInLoop.append([line,col])

print("Number of points within the loop: " + str(len(pointsInLoop)))