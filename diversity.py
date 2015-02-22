#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_bd = True
print_ham = False

#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/two-tests-lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/two-tests-better-lexicase/"
outputDirectory = "Results/bench-prog-synth/checksum/exploratory/while-lexicase/"

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

bd_list_per_gen = []
ham_list_per_gen = []

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
            while len(bd_list_per_gen) <= gen:
                bd_list_per_gen.append([])
                ham_list_per_gen.append([])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Behavioral diversity:"):
            bd = float(line.split()[-1])
            bd_list_per_gen[gen].append(bd)

        if line.startswith("Mean Hamming distance between sampled"):
            ham = float(line.split()[-1])
            ham_list_per_gen[gen].append(ham)
            
    i += 1



print
print outputDirectory

if print_bd:
    print
    print "Mean Behavioral Diversity Each Generation Across Runs"
    for gen_bd in bd_list_per_gen:
        print "%0.3f" % (mean(gen_bd))

if print_ham:
    print
    print "Mean Mean Hamming Distance Between Pairs Each Generation Across Runs"
    for gen_ham in ham_list_per_gen:
        print "%0.3f" % (mean(gen_ham))

