import os

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

#Input data has to end with 2 \n
mapArray = []
localMap = []
for line in inData:
    if line == '\n':
        mapArray.append(localMap)
        localMap = []
    else:
        localMap.append(line.rstrip('\n'))

def isMirror(index,line):
    return line[index-min(index,len(line)-index):index] == line[index:index+min(index,len(line)-index)][::-1]

def findHorReflection(line):
    reflections = []
    for a in range(1,len(line)):
        if line[a] == line[a-1]:
            if isMirror(a,line):
                reflections.append(a)
    return reflections

def isHorReflection(index,map):
    for line in map[1:]:
        if line[index] == line[index-1]:
            if not isMirror(index,line):
                return False
        else:
            return False
    return True

def findVerReflection(map,col):
    colAsLine = ''
    for line in map:
        colAsLine += line[col]
    reflections = findHorReflection(colAsLine)
    return reflections

def flipMap(map):
    flippedMap = []
    for a in range(len(map[0])):
        colAsLine = ''
        for line in map:
            colAsLine += line[a]
        flippedMap.append(colAsLine)
    return flippedMap

def flipChar(line,col,map):
    tempMap = map
    if tempMap[line][col] == '.':
        tempMap[line] = tempMap[line][:col] + '#' + tempMap[line][col+1:]
    else:
        tempMap[line] = tempMap[line][:col] + '.' + tempMap[line][col+1:]
    return tempMap

#Part 1
score = 0
mirrorArray = []
for index,map in enumerate(mapArray):
    #Check for horizontal reflections
    horReflectionCandidates = findHorReflection(map[0])
    if horReflectionCandidates != []:
        for candidate in horReflectionCandidates:
            if isHorReflection(candidate,map):
                print("Horizontal reflection found for map " + str(index) + " at index " + str(candidate))
                mirrorArray.append(["hor",candidate])
                score += candidate
    #Check for vertical reflections
    verReflectionCandidates = findVerReflection(map,0)
    if verReflectionCandidates != []:
        for candidate in verReflectionCandidates:
            if isHorReflection(candidate,flipMap(map)):
                print("Vertical reflection found for map " + str(index) + " at index " + str(candidate))
                mirrorArray.append(["ver",candidate])
                score += candidate*100

print("Total score for part 1: " + str(score))

#Part 2
score = 0
for index,map in enumerate(mapArray):
    for lineIndex,line in enumerate(map):
        for colIndex,col in enumerate(line):
            flag = False
            tempMap = flipChar(lineIndex,colIndex,map.copy())
            #Check for horizontal reflections
            horReflectionCandidates = findHorReflection(tempMap[0])
            if horReflectionCandidates != []:
                for candidate in horReflectionCandidates:
                    if isHorReflection(candidate,tempMap) and mirrorArray[index] != ["hor",candidate]:
                        print("Horizontal reflection found for map " + str(index) + " flipped in (" + str(lineIndex) + "," + str(colIndex) + ") at index " + str(candidate))
                        score += candidate
                        flag = True
                        break
            if flag: break
            #Check for vertical reflections
            verReflectionCandidates = findVerReflection(tempMap,0)
            if verReflectionCandidates != []:
                for candidate in verReflectionCandidates:
                    if isHorReflection(candidate,flipMap(tempMap)) and mirrorArray[index] != ["ver",candidate]:
                        print("Vertical reflection found for map " + str(index) + " flipped in (" + str(lineIndex) + "," + str(colIndex) + ") at index " + str(candidate))
                        score += candidate*100
                        flag = True
                        break
            if flag: break
        else:
            continue
        break

print("Total score for part 2: " + str(score))