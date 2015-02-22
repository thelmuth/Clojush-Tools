#!/usr/bin/python
#import math
import os
from sys import maxint

# Set these before running:
#fileName = "Results/newGO/lex/log19.txt"
#fileName = "Results/weighted/2f/log5.txt"
#fileName = "Results/two-frame-kata/bowling-lexicase/log1.txt"
#fileName = "Results/ULTRA/lexicase/log8.txt"
fileName = "Results/ULTRA/larger-lexicase/log3.txt"

errorType = "float"

# Main area
f = open(fileName)

gen = 0
best_mean_error = maxint

mean_errors = []

for line in f:

    if line.startswith(";; -*- Report"):
        gen = int(line.split()[-1])

    if line.startswith("Mean:"):
        gen_best_error = -1
        if errorType == "float":
            gen_best_error = float(line.split()[-1])
        elif errorType == "int" or errorType == "integer":
            gen_best_error = int(line.split()[-1])
        else:
            raise Exception("errorType of %s is not recognized" % errorType)

        mean_errors.append(gen_best_error)


#print
#print "Best fitnesses of runs:"
for gen, mean_error  in enumerate(mean_errors):
    print "Gen: %3i  | Best Fitness (mean) = %8.2f" % (gen, mean_error)
