#!/usr/bin/python
import os
import re
from sys import maxint

# Set these before running:

#dir1 = "Results/lexicase-paper/selection-probs/lexicase/"
dir1 = "Results/lexicase-paper/selection-probs/tourney7/"



outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area

def getLogSelections(outputDirectory):
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    runs_selections = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    
        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        read = False
        selections = []

        for line in f:

            pattern = re.compile(r'(\d*),(\d*)')
            match = re.match(pattern, line)

            if line.startswith("rank,selections"):
                read = True
            elif match and read:
                rank = match.group(1)
                count = match.group(2)
                selections.append(count)
            elif read:
                read = False
                break

        runs_selections.append(selections)
            
        i += 1

    return runs_selections


all_selections = getLogSelections(dir1)

for i in range(0,len(all_selections[0])):
    s = "%d," % i
    for selections in all_selections:
        s += "%s," % selections[i]
    print s[:-1]
