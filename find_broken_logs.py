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

outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000-two/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    sys.stdout.write(outputFilePrefix + str(i) + outputFileSuffix + ': ')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    gen_list = []
    gen = 0

    for line in f:
        if ";; -*- Report" in line:
            gen = int(line.split()[-1])
            if gen in gen_list:
                sys.stdout.write("BAD LOG | gen = " + str(gen))
                break
            gen_list.append(gen)
            
    print
    i += 1
