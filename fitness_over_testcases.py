#import math
import os
#import sys

# Set these before running:
outputDirectory = "Results/kata2/bowling_lexicase/"
outputFilePrefix = "log"
outputFileSuffix = ".txt"
i = 7

filename = outputDirectory + outputFilePrefix + str(i) + outputFileSuffix

##########

f = open(filename)

all_errors = []

for line in f:

    if line.startswith("Errors:"):
        errors = [int(x.strip("N")) for x in line[9:-2].split()]
        all_errors.append(errors)



for testcase in range(0, len(all_errors[0])):
    print "testcase(%i):\t" % (testcase),
    for gen in range(0, len(all_errors)):
        print "%i\t" % (all_errors[gen][testcase]),
    print
