#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_homology = True

### EHC
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/ifs-7/"

# these are to see how many point evaluations are used in a typical GP run of this problem
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/tourney-7/"
outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/ifs-7/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

def mean(nums):
    if len(nums) <= 0:
        return -1
    return sum(nums) / float(len(nums))

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

point_evals_and_seconds = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    point_evals = -1
    total_time = -1

    for line in reversed(f.readlines()):

        if total_time > 0 and point_evals > 0:
            point_evals_and_seconds.append((point_evals, total_time))
            break

        if line.startswith("Number of point (instruction) evaluations so far"):
            point_evals = int(line.split()[-1])

        if line.startswith("Total Time:"):
            total_time = float(line.split()[-2])
            
    i += 1



print
print outputDirectory

for i, (point_evals, secs) in enumerate(point_evals_and_seconds):
    print "Run %3i | Point Evals: %13i | Seconds: %9.1f | Point Evals Per Second: %9.1f" % (i, point_evals, secs, (point_evals / secs))

total_point_evals = sum([pe for [pe, _] in point_evals_and_seconds])
total_secs = sum([secs for [_, secs] in point_evals_and_seconds])

print "-----"
print "Total point evals = %i" % total_point_evals
print "Total seconds = %.1f" % total_secs
print "Overall point evals per second = %.1f" % (total_point_evals / total_secs)
