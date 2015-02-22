#!/usr/bin/python
#import math
import os
from sys import maxint

# Set these before running:
#outputDirectory = "Results/gecco13/pagie-normal/"
#outputDirectory = "Results/gecco13/pagie-ultra/"

#outputDirectory = "Results/gecco13/pagie-no-erc-normal/"
#outputDirectory = "Results/gecco13/pagie-hogeweg-no-erc-45/"
#outputDirectory = "Results/gecco13/pagie-no-erc-ultra/" #Uses non-equal size ULTRA
#outputDirectory = "Results/gecco13/equal-size-ULTRA/pagie-no-erc/"

#outputDirectory = "Results/GECCO14/order-lexicase/pagie-946/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-895/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-80/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-64/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-464/"

#outputDirectory = "Results/ULTRA-redo/pagie/subtree-80-10-10/"
#outputDirectory = "Results/ULTRA-redo/pagie/subtree-45-45-10/"
#outputDirectory = "Results/ULTRA-redo/pagie/ultra/"

#outputDirectory = "Results/padding-ultra/pagie/padding/"
#outputDirectory = "Results/padding-ultra/pagie/padding200/"
#outputDirectory = "Results/padding-ultra/pagie/padding150/"
#outputDirectory = "Results/padding-ultra/pagie/padding-bug-finding/"
outputDirectory = "Results/padding-ultra/pagie/fixed-padding/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

#outputFilePrefix = "bio-ultralog"
#outputFilePrefix = "bio-normallog"

errorType = "float"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)


bestFitnessesOfRuns = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    best_hits = maxint
    best_mean_error = maxint
    done = False

    for line in f:

        try:
            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])

            if line.startswith("SUCCESS") or line.startswith("FAILURE"):
                done = True

            if line.startswith("Best's total error (hits)"):
                gen_hits = int(line.split()[-1])
                
                if gen_hits < best_hits:
                    best_hits = gen_hits

        except ValueError:
            print "ERROR: " + line


    bestFitnessesOfRuns.append((gen, best_hits, done))
            
    i += 1


#print
#print "Best fitnesses of runs:"
for i, (gen, hits, done) in enumerate(bestFitnessesOfRuns):
    print "Run: %3i  | Gen: %4i  | Best Hits = %i" % (i, gen, hits)

success_hits = 0
for (gen, hits, done) in bestFitnessesOfRuns:
    if hits == 0:
        success_hits += 1

print "-----"
print "Number of successful runs based on hits: %i" % success_hits
