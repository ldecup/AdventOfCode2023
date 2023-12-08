import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

def distTraveled(timeHeld,raceTime):
    return (raceTime-timeHeld) * timeHeld

data = []
for line in inData:
    data.append(line.rstrip('\n'))

timeData = [int(i) for i in re.findall(r'\d+', data[0].split(":")[1])]
totalTime = int(data[0].split(":")[1].replace(" ",""))
distData = [int(i) for i in re.findall(r'\d+', data[1].split(":")[1])]
totalDist = int(data[1].split(":")[1].replace(" ",""))

#Part1
totalScore = 1
for index,raceTime in enumerate(timeData):
    raceScore = 0
    for timeHeld in range(1,raceTime):
        if distTraveled(timeHeld,raceTime) > distData[index]:
            raceScore += 1
    totalScore = totalScore * raceScore

print("Total score for part 1: " + str(totalScore))

#Part 2
for roughTimeStep in range(1,totalTime,10000):
    if distTraveled(roughTimeStep,totalTime) > totalDist:
        print("Rough time step: " + str(roughTimeStep))
        break

for fineTimeStep in range(roughTimeStep-10000,totalTime):
    if distTraveled(fineTimeStep,totalTime) > totalDist:
        lowerBound = fineTimeStep
        print("Found lower bound: " + str(lowerBound))
        break

upperBound = totalTime - fineTimeStep
totalWinMethods = upperBound - lowerBound + 1

print("Total number of ways to win for part 2: " + str(totalWinMethods))