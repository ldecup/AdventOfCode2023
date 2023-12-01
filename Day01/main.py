import os
import re

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'input.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

digits = ["one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
digitPattern = '|'.join(digits)

data = []
for line in inData:
    data.append(line.rstrip('\n'))

#Turns word digits into digit digits
def digitize(value):
    if len(value) > 1:
        return str(digits.index(value)+1)
    else:
        return value

totalCalibration = 0
for line in data:
    firstDigit = re.findall(digitPattern, line)[0]
    #To find the last digit, reverse the string and use the reverse of the pattern (and reverse the match :))
    lastDigit = re.findall(digitPattern[::-1], line[::-1])[0][::-1]

    calibrationValue = int(digitize(firstDigit)+digitize(lastDigit))
    totalCalibration += calibrationValue

print(totalCalibration)