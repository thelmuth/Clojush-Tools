#!/usr/bin/python
import os
from sys import maxint
import collections

# Set these before running:
genToStartLogging = 0

outputFilePrefix = "log"
outputFileSuffix = ".txt"

#outputDirectory = "Results/ULTRA-begin-parens/individual-runs/"
#outputFilePrefix = "no-selection-all-open-parens-first-last-removed"
#outputFilePrefix = "no-selection-all-open-parens-keep-first-last"
#outputFilePrefix = "no-selection-all-random-programs-size-200-to-300-"


#outputDirectory = "Results/ULTRA-begin-parens/no-alignment-deviation/"
#outputDirectory = "Results/ULTRA-begin-parens/bushy-rand-and-mut/"
#outputDirectory = "Results/ULTRA-begin-parens/ultra-paren-mutaiton-on/"
#outputDirectory = "Results/ULTRA-begin-parens/ultra-normal/"
outputDirectory = "Results/ULTRA-begin-parens/normal-random-code-frequent-ULTRA-paren-mut/"


# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

openParenDictList = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    gen = 0

    openParenDictList.append({})
    readData = False

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith(";;;;;;;;;;;;;;;"):
            readData = False

        if readData and (gen >= genToStartLogging):
            lineDataStr = line.strip().split(",")
            lineData = [int(x) for x in lineDataStr]
            parens = lineData[0]
            programCount = lineData[1]
            newCount = openParenDictList[-1].get(parens,0) + programCount
            openParenDictList[-1][parens] = newCount

        if line.startswith("StartParens,ProgramCount"):
            readData = True

    i += 1

def dictMergeSummingValues(a, b):
    allKeys = set(a.keys()).union(set(b.keys()))
    result = {}
    for k in allKeys:
        result[k] = a.get(k,0) + b.get(k,0)
    return result

allData = reduce(dictMergeSummingValues, openParenDictList)

for x in range(0,max(allData.keys())+1):
    print "%d,%d" % (x, allData.get(x,0))


#for d in openParenDictList:
#    for x in range(0,max(d.keys())+1):
#        print "%d,%d" % (x, d.get(x,0))
