import math
import os
import sys

# Set these before running:

outputDirectory = "Collab/aabdelha/results/scrabble-score10p/lexicase/scrabble-score/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    best_program = ""

    for line in f:
        if line.startswith("Best program: "):
            best_program = line[len("Best program: "):].strip()

    print best_program

    i += 1
