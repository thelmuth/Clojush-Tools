#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_bd = True
print_errordiv = False
print_ham = False

#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/two-tests-lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/two-tests-better-lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/exploratory/while-lexicase/"

#outputDirectory = "Results/parent-selection-v2/lexicase/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/lexicase/syllables/"
#outputDirectory = "Results/parent-selection-v2/lexicase/vector-average/"
#outputDirectory = "Results/parent-selection-v2/lexicase/double-letters/"
#outputDirectory = "Results/parent-selection-v2/lexicase/mirror-image/"
#outputDirectory = "Results/parent-selection-v2/lexicase/last-index-of-zero/"
outputDirectory = "Results/parent-selection-v2/lexicase/scrabble-score/"
#outputDirectory = "Results/parent-selection-v2/lexicase//"
#outputDirectory = "Results/parent-selection-v2/lexicase//"
#outputDirectory = "Results/parent-selection-v2/lexicase//"
#outputDirectory = "Results/parent-selection-v2/lexicase//"


#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/tournament/replace-space-with-newline/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/tournament/syllables/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/tournament/vector-average/"



######## Diversity Recovery trials
## Drop 25
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run8/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run8/"

## Div90
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run6/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run6/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run10/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run10/"

## Tourney < 15
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run1/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run1/"


##### Double Letters #####
#------------------------#

## Div Drop 25
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/lexicase/run21/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/tournament/run21/"

## Div 90
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/lexicase/run3/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/tournament/run3/"

## Tourney < 15
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/lexicase/run1/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/tournament/run1/"



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

