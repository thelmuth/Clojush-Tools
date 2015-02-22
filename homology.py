#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_homology = True

outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"
outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"
outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/"

outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"
outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"
outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/"


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

homology_list_per_gen = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    gen = 0
    done = False

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])
            while len(homology_list_per_gen) <= gen:
                homology_list_per_gen.append([])


        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Average            (sample 1)"):
            homology = float(line.split()[-1])
            homology_list_per_gen[gen].append(homology)
            
    i += 1



print
print outputDirectory

if print_homology:
    print
    print "Mean of Average Edit Distance Each Generation Across Runs"
    for gen_homology in homology_list_per_gen:
        print "%0.3f" % (mean(gen_homology))
