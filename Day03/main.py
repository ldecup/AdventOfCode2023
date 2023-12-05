import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

class part:
    def __init__(self, id, line, start, end, isGear, interlockCoords, matched):
        self.id = id
        self.line = line
        self.start = start
        self.end = end
        self.isGear = isGear
        self.interlockCoords = interlockCoords
        self.matched = matched


#Import the schematic and pad it with . to avoid handling out-of-range errors
schematic = []
for line in inData:
    schematic.append("."+line.rstrip('\n')+".")
dummyLine = ""
for i in range(len(schematic[0])):
    dummyLine = dummyLine + "."
schematic.insert(0,dummyLine)
schematic.append(dummyLine)

def isPart(line,start,end):
    flag = True
    flag = (schematic[line][start-1] == ".") and flag
    flag = (schematic[line][end] == ".") and flag
    for i in range(start-1,end+1):
        flag = (schematic[line-1][i] == ".") and flag
    for i in range(start-1,end+1):
        flag = (schematic[line+1][i] == ".") and flag
    return not flag

def isGear(part):
    part.isGear = False
    if schematic[part.line][part.start-1] == "*":
        part.isGear = True
        part.interlockCoords = [part.line,part.start-1]
    elif schematic[part.line][part.end] == "*":
        part.isGear = True
        part.interlockCoords = [part.line,part.end]
    for i in range(part.start-1,part.end+1):
        if schematic[part.line-1][i] == "*":
            part.isGear = True
            part.interlockCoords = [part.line-1,i]
    for i in range(part.start-1,part.end+1):
        if (schematic[part.line+1][i] == "*"):
            part.isGear = True
            part.interlockCoords = [part.line+1,i]
    return part.isGear

#Part1
partsList = []
listNotParts = []
totalPartID = 0
for lineID in range(1,len(schematic)):
    numbersInLine = re.finditer(r'\d+', schematic[lineID])
    for match in numbersInLine:
        matchValue = int(match.group())
        matchStart = match.span()[0]
        matchEnd = match.span()[1]
        if isPart(lineID,matchStart,matchEnd):
            currentPart = part(matchValue, lineID, matchStart,matchEnd, None, None, False)
            currentPart.isGear = isGear(currentPart)
            partsList.append(currentPart)
            totalPartID = totalPartID + matchValue
        else:
            listNotParts.append(part(matchValue, lineID, matchStart,matchEnd, None, None, False))

print(totalPartID)


#Part2
listMeshedGears = []
totalGearRatio = 0
for parts in partsList:
    if parts.isGear and parts.matched == False:
        for candidate in partsList:
            if (parts.interlockCoords == candidate.interlockCoords) and (candidate is not parts):
                listMeshedGears.append([parts,candidate])
                parts.matched = True
                candidate.matched = True
                totalGearRatio = totalGearRatio + (parts.id*candidate.id)
    
print(totalGearRatio)