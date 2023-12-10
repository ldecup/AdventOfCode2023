import os

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

mainData = []
for line in inData:
    mainData.append([int(i) for i in line.rstrip('\n').split(" ")])

def isSubValuesDone(array):
    if array == []: return False
    return not any(0 != x for x in array[-1])

def computeNext(array):
    subLine = []
    for a in range(1,len(array[-1])):
        subLine.append(array[-1][a]-array[-1][a-1])
    array.append(subLine)
    return array

totalSubValues = []
for line in mainData:
    subValuesForLine = [line]
    while not isSubValuesDone(subValuesForLine):
        computeNext(subValuesForLine)
    totalSubValues.append(subValuesForLine)

#Part 1
for subTable in totalSubValues:
    currTable = subTable[::-1]
    #Add a 0 to the line of 0
    currTable[0].append(0)
    #Going up
    for index,sub in enumerate(currTable[1:]):
        sub.append(sub[-1]+currTable[index][-1])

totalScore = 0
for line in totalSubValues:
    totalScore += line[0][-1]
print(totalScore)

#Part 2
for subTable in totalSubValues:
    currTable = subTable[::-1]
    #Add a 0 to the line of 0
    currTable[0].insert(0,0)
    #Going up
    for index,sub in enumerate(currTable[1:]):
        sub.insert(0,sub[0]-currTable[index][0])

totalScore = 0
for line in totalSubValues:
    totalScore += line[0][0]
print(totalScore)