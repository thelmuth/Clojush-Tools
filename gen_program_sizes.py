#!/usr/bin/python
#import math
import os
from sys import maxint

# Set these before running:
#fileName = "Results/newGO/lex/log19.txt"
#fileName = "Results/weighted/2f/log5.txt"
#fileName = "Results/two-frame-kata/bowling-lexicase/log1.txt"
#fileName = "Results/ULTRA/lexicase/log8.txt"
#fileName = "Results/ULTRA/larger-lexicase/log3.txt"

#fileName = "Results/GECCO13/pagie-no-erc-ultra/log0.txt"
fileName = "Results/GECCO13/pagie-no-erc-normal/log0.txt"

# Main area
f = open(fileName)

gen = 0

sizes = []
avgSizes = []

for line in f:

    if line.startswith(";; -*- Report"):
        gen = int(line.split()[-1])

    if line.startswith("Size:"):
        size = int(line.split()[-1])
        sizes.append(size)

    if line.startswith("Average program size in population"):
        mean_size = float(line.split()[-1])
        avgSizes.append(mean_size)


#print
#print "Best fitnesses of runs:"
for gen, (size, avg)  in enumerate(zip(sizes, avgSizes)):
    print "Gen: %3i  | Best Prog Size = %4i  | Mean Prog Size = %.1f" % (gen, size, avg)
