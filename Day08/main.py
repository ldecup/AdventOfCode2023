import os
from collections import Counter
from math import gcd

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

instructions = inData[0].rstrip('\n')

mapData = []
for line in inData[2:]:
    mapLine = line.rstrip('\n').split(" = ")
    mapLine[1] = mapLine[1].lstrip("(").rstrip(")").split(", ")
    mapData.append(mapLine)

def findNodeIndex(node,mapData):
    return next((index for index,x in enumerate(mapData) if node == x[0]), None)

def lcm(stepCountArray):
    factors = Counter()
    for stepCount in stepCountArray:
        for factor, count in Counter(prime_factors(stepCount)).items():
            factors[factor] = max(factors[factor], count)
    lcm = 1
    for factor, count in factors.items():
        lcm *= factor ** count
    return lcm

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#Part1
""" currentNode = mapData[findNodeIndex('AAA',mapData)]
currentInstructionId = 0
stepCounter = 0
while currentNode[0] != 'ZZZ':
    currentInstruction = instructions[currentInstructionId]
    if currentInstruction == 'L':
        currentNode = mapData[findNodeIndex(currentNode[1][0],mapData)]
    elif currentInstruction == 'R':
        currentNode = mapData[findNodeIndex(currentNode[1][1],mapData)]
    currentInstructionId += 1
    stepCounter += 1
    if currentInstructionId > len(instructions) - 1:
        currentInstructionId = 0
 """

#Part2
currentNodeArray = []
stepCountArray = []
for node in mapData:
    if node[0][-1] == 'A':
        currentNodeArray.append(node)
        stepCountArray.append(0)

for index,node in enumerate(currentNodeArray):
    currentInstructionId = 0
    stepCounter = 0
    while node[0][-1] != 'Z':
        currentInstruction = instructions[currentInstructionId]
        if currentInstruction == 'L':
            node = mapData[findNodeIndex(node[1][0],mapData)]
        elif currentInstruction == 'R':
            node = mapData[findNodeIndex(node[1][1],mapData)]
        currentInstructionId += 1
        stepCounter += 1
        if currentInstructionId > len(instructions) - 1:
            currentInstructionId = 0
    stepCountArray[index] = stepCounter


print(stepCountArray)
print(lcm(stepCountArray))