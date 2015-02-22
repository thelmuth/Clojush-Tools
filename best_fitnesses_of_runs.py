#import math
import os
from sys import maxint

# Set these before running:
#outputDirectory = "results/kata2/bowling_lexicase/"
outputDirectory = "Results/kata-gsxover/lexicase/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

errorType = "int"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)


#print "Computing best hits per generation..."

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
    best_total_error = maxint

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("Total:"):
            gen_best_error = -1
            if errorType == "float":
                gen_best_error = float(line.split()[-1])
            elif errorType == "int" or errorType == "integer":
                gen_best_error = int(line.split()[-1])
            else:
                raise Exception("errorType of %s is not recognized" % errorType)

            if gen_best_error < best_total_error:
                best_total_error = gen_best_error

    bestFitnessesOfRuns.append((gen, best_total_error))
            
    i += 1


#print
#print "Best fitnesses of runs:"
for i, (gen, fitness)  in enumerate(bestFitnessesOfRuns):
    if errorType == "float":
        print "Run: %3i  | Gen: %3i  | Best Fitness = %8.3f" % (i, gen, fitness)
    else:
        print "Run: %3i  | Gen: %3i  | Best Fitness = %5i" % (i, gen, fitness)
