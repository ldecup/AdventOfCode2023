import os
import re

#Status: does not work. It gives an answer with a granularity of 1 after 10 minutes, but that answer is too high

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

#destination, source, range

def findLower(sourceId,mapId,almaMap):
    #Find the source in the map
    for subMap in almaMap[mapId]:
        if sourceId >= subMap[1] and sourceId <= subMap[1]+subMap[2]:
            delta = sourceId - subMap[1]
            #print(str(sourceId) + " matched " + str(subMap[0]+delta))
            return subMap[0]+delta
    #print("No match found for " + str(sourceId))
    return sourceId

def findUpper(destId,mapId,almaMap):
    for subMap in almaMap[mapId]:
        if destId >= subMap[0] and destId <= subMap[0]+subMap[2]:
            delta = destId - subMap[0]
            return subMap[1]+delta
    return destId

def isValidSeed(seedId,seedArray):
    for a in range(0,len(seedArray)-1,2):
        if seedId >= seedArray[a] and seedId <= seedArray[a]+seedArray[a+1]:
            return True
    return False

#Parser - input has to end with 2 empty lines, and seed data needs to be sent to a new line !
#TODO Parser has to sort submaps by destination ID
subArrays = []
sub = []
for line in inData:
    data = line.rstrip('\n')
    if data is not '':
        if ":" in data:
            data = data.split(" ")[0]
        else:
            data = re.findall(r'\d+',data)
        sub.append(data)
    else:
        sub[1:] = sorted(sub[1:], key=lambda x: x[0])
        subArrays.append(sub)
        sub = []

seedArray = [int(i) for i in subArrays[0][1]]

almaMap = []
for map in subArrays[1:]:
    almaLine = []
    for data in map[1:]:
        almaLine.append([int(i) for i in data])
    almaMap.append(almaLine)

#Part 1
lowestSeedLoc = float('inf')
for seedId in seedArray:
    soil = findLower(seedId,0,almaMap)
    fertilizer = findLower(soil,1,almaMap)
    water = findLower(fertilizer,2,almaMap)
    light = findLower(water,3,almaMap)
    temperature = findLower(light,4,almaMap)
    humidity = findLower(temperature,5,almaMap)
    location = findLower(humidity,6,almaMap)
    if location < lowestSeedLoc:
        lowestSeedLoc = location

print("Lowest seed location for part 1: " + str(lowestSeedLoc))

#Part 2
""" lowestSeedLoc = float('inf')
for a in range(0,len(seedIds)-1,2):
    print("At position " + str(a))
    for b in range(seedIds[a],seedIds[a]+seedIds[a+1]):
        soil = findLower(b,0,almaMap)
        fertilizer = findLower(soil,1,almaMap)
        water = findLower(fertilizer,2,almaMap)
        light = findLower(water,3,almaMap)
        temperature = findLower(light,4,almaMap)
        humidity = findLower(temperature,5,almaMap)
        location = findLower(humidity,6,almaMap)
        if location < lowestSeedLoc:
            lowestSeedLoc = location

print("Lowest seed location for part 2: " + str(lowestSeedLoc)) """

roughCurrentLocation = 0
while True:
    humidity = findUpper(roughCurrentLocation,6,almaMap)
    temperature = findUpper(humidity,5,almaMap)
    light = findUpper(temperature,4,almaMap)
    water = findUpper(light,3,almaMap)
    fertilizer = findUpper(water,2,almaMap)
    soil = findUpper(fertilizer,1,almaMap)
    seed = findUpper(soil,0,almaMap)
    if isValidSeed(seed,seedArray):
        print("Rough lowest seed location for part 2: " + str(roughCurrentLocation))
        break
    else:
        roughCurrentLocation += 100

currentLocation = roughCurrentLocation - 100
while True:
    humidity = findUpper(currentLocation,6,almaMap)
    temperature = findUpper(humidity,5,almaMap)
    light = findUpper(temperature,4,almaMap)
    water = findUpper(light,3,almaMap)
    fertilizer = findUpper(water,2,almaMap)
    soil = findUpper(fertilizer,1,almaMap)
    seed = findUpper(soil,0,almaMap)
    if isValidSeed(seed,seedArray):
        print("Best lowest seed location for part 2: " + str(currentLocation))
        break
    else:
        currentLocation += 1