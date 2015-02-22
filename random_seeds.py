#!/usr/bin/python
import os
import sys
from sys import maxint

# Set these before running:

#outputDirectory = "Results/ULTRA-redo/pagie/subtree-80-10-10/"
#outputDirectory = "Results/ULTRA-redo/pagie/ultra/"

#outputDirectory = "Results/thesis/wc-exploratory/"
#outputDirectory = "Results/GECCO14/wc/domains-all-cases-empties/" #bad ULTRA params
#outputDirectory = "Results/GECCO14/wc/domains-all-cases-padding/" #bad ULTRA params
#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-empties/"
#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-padding/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/padding-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/bushy-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/"

#outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000-two/"

#outputDirectory = "Results/ULTRA-mut/wc/split-ULTRA-50-50"

#outputDirectory = "Results/lexicase-paper/resub/dm3/lex-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney6-ultra/"
outputDirectory = "Results/lexicase-paper/resub/dm3/tourney8-ultra/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

seeds = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write(outputFilePrefix + str(i) + outputFileSuffix + ': ')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    for line in f:
        if line.startswith("random-seed"):
            seed = line[len("random-seed = "):-1]
            seeds.append(seed)

            print "Run %3i seed: %s" % (i, seed)
            break

    i += 1

seed_dups = list(set([x for x in seeds if seeds.count(x) > 1]))
print "-----------------------"
print "Seed duplicates:", seed_dups
