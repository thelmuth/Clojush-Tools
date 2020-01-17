#!/usr/bin/python
import os, sys
from sys import maxint

# Set these before running:

print_bd = True
print_errordiv = False
print_ham = False

#outputDirectory = "Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.25/syllables/"
#outputDirectory = "Results/parent-selection-v3-UMAD/lexicase/syllables"
outputDirectory = "Results/specialists-and-lexicase/elitist-survival-2018-not-UMAD/rate-100/lexicase/syllables"



if len(sys.argv) > 1:
    outputDirectory = sys.argv[1]

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
evd_list_per_gen = []
ham_list_per_gen = []

print
print outputDirectory

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
                evd_list_per_gen.append([])
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

        if line.startswith("Error (vector) diversity:"):
            evd = float(line.split()[-1])
            evd_list_per_gen[gen].append(evd)

        if line.startswith("Mean Hamming distance between sampled"):
            ham = float(line.split()[-1])
            ham_list_per_gen[gen].append(ham)
            
    i += 1


if print_bd:
    print
    print "Mean Behavioral Diversity Each Generation Across Runs"
    for gen_bd in bd_list_per_gen:
        print "%0.3f" % (mean(gen_bd))

if print_errordiv:
    print
    print "Mean Error Vector Diversity Each Generation Across Runs"
    for gen_evd in evd_list_per_gen:
        print "%0.3f" % (mean(gen_evd))

if print_ham:
    print
    print "Mean Mean Hamming Distance Between Pairs Each Generation Across Runs"
    for gen_ham in ham_list_per_gen:
        print "%0.3f" % (mean(gen_ham))

