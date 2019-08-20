import math
import os
import sys

# Set these before running:

outputDirectory = "Collab/aabdelha/results/last-index-of-zero10p/lexicase/last-index-of-zero/"
outputDirectory = "Collab/aabdelha/results/scrabble-score10p/lexicase/scrabble-score/"


outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

verbose = True
if(len(sys.argv) > 1):
    verbose = False

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    success = False
    simpl = False

    if verbose:
        print
        print "-------------------------------------------------"
        print "------------------ Run %i ------------------------" % i
        print

    testForBest = 5

    for line in f:
        if line.startswith("Successful program: "):
            if verbose:
                print line
                print
            else:
                if sys.argv[1] != "test" or testForBest == 0:
                    print line[len("Successful program: "):-1]
            success = True

        if simpl == True and verbose:
            print "Simplification after 1000 steps:"
            print line
            break

        if success and line.startswith("step: 1000"):
            simpl = True

        if line.startswith("Test total error for best:"):
            testForBest = int(line.split()[-1].strip("Nn"))

    i += 1
