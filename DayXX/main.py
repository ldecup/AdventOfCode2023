import os

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'testinput.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

data = []
for line in inData:
    data.append(line.rstrip('\n'))