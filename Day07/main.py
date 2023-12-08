import os
import time

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

handList = []
for line in inData:
    handList.append(line.rstrip('\n').split())

cardStrengthsPart1 = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
cardStrengthsPart2 = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

def readHand(hand,optimize):
    detectedCards = []
    optimalHand = None
    for card in hand:
        detectedIndex = next((index for index,x in enumerate(detectedCards) if card == x[0]), None)
        if not any(card == x[0] for x in detectedCards):
            detectedCards.append([card,1])
        else:
            detectedCards[detectedIndex][1] += 1
    detectedCards = sorted(detectedCards, key=lambda x: x[1])
    if optimize:
        jIndex = next((index for index,x in enumerate(detectedCards) if 'J' == x[0]), None)
        if jIndex is not None:
            if len(detectedCards) is 1:
                optimalHand = 'AAAAA'
            else:
                if jIndex is not len(detectedCards) - 1:
                    targetIndex = len(detectedCards) - 1
                else:
                    targetIndex = len(detectedCards) - 2
                optimizedDetectedCards = detectedCards
                optimizedDetectedCards[targetIndex][1] += detectedCards[jIndex][1]
                optimizedDetectedCards.pop(jIndex)
                optimalHand = ''
                for opCard in optimizedDetectedCards:
                    optimalHand += opCard[0]*opCard[1]
    if len(detectedCards) is 1:                 return 7,optimalHand
    if any(4 == x[1] for x in detectedCards):   return 6,optimalHand
    if len(detectedCards) is 2:                 return 5,optimalHand
    if any(3 == x[1] for x in detectedCards):   return 4,optimalHand
    if len(detectedCards) is 3:                 return 3,optimalHand
    if len(detectedCards) is 4:                 return 2,optimalHand
    return 1,optimalHand

def isHand1Stronger(hand1,hand2,cardStrengthArray,optimize):
    hand1Strength = readHand(hand1,optimize)[0]
    hand2Strength = readHand(hand2,optimize)[0]
    if hand1Strength > hand2Strength:
        return True
    elif hand1Strength < hand2Strength:
        return False
    else:
        for a in range(5):
            if cardStrengthArray.index(hand1[a]) > cardStrengthArray.index(hand2[a]):
                return True
            elif cardStrengthArray.index(hand1[a]) < cardStrengthArray.index(hand2[a]):
                return False
        return None

def optimizeHand(hand):
    return None

#Quick sort
startTime = time.perf_counter()
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = []
        right = []
        for i in range(len(arr)-1):
            if isHand1Stronger(pivot[0],arr[i][0],cardStrengthsPart2,True): #Part1: cardStrengthsPart1,False #Part2: cardStrengthsPart2,True
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quickSort(left) + [pivot] + quickSort(right)
handList = quickSort(handList)
elapsedTime = time.perf_counter() - startTime

#Compute score
totalScore = 0
for index,hand in enumerate(handList):
    totalScore += int(hand[1])*(index+1)

print("Total score : " + str(totalScore) + " (sorting took " + str(elapsedTime) + "s)")