import os
import re

#Status: not done at all

inPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'testinput.txt')
inFile = open(inPath, 'r')
inData = inFile.readlines()
inFile.close()

springData = []
for line in inData:
    tempSpring = []
    tempSpring.append([x for x in line.rstrip('\n').split(" ")[0].split(".") if x != ""])
    tempSpring.append(map(int,line.rstrip('\n').split(" ")[1]))
    springData.append(tempSpring)

#Simplify the problem: remove all good spring data (only #, on a line extremity)
for line in springData:
    for section in line[0]:
        if not any('?' == x for x in section):
            line[0].remove(section)
            line[1].pop(0)
        else: break
    for section in line[0][::-1]:
        if not any('?' == x for x in section):
            line[0].remove(section)
            line[1].pop(-1)
        else: break

def validConfs(inString,confMap):
    confs = []

    

confMap = []
for line in springData:
    dmgSpringNb = sum(line[1])
    opSpringNb = ''.join(line[0]).count('?') - dmgSpringNb



print("done")

