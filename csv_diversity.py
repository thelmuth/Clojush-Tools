#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

############ For lexicase paper resub
# dirs = [("lexicase", "Results/lexicase-paper/resub/wc/diversity-figures/lex/"),
#         ("tourney3", "Results/lexicase-paper/resub/wc/diversity-figures/tourney3/"),
#         ("tourney5", "Results/lexicase-paper/resub/wc/diversity-figures/tourney5/"),
#         ("tourney7", "Results/lexicase-paper/resub/wc/diversity-figures/tourney7/"),
#         ("ifs3", "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-3/"),
#         ("ifs5", "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-5/"),
#         ("ifs7", "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-7/")]


######## For dissertation

# dirs = [("lexicase", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/")]

# dirs = [("lexicase", "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/")]

############ For GECCO16 Diversity Workshop - Diversity Recovery paper

# dirs = [("Drop25-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run0/"),
#         ("Drop25-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run0/")
#         ]

dirs = [("Drop25-Run8-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run8/"),
        ("Drop25-Run8-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run8/")
        ]


# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run6/"
# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run6/"

# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run0/"
# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run0/"



outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area

def mean(nums):
    if len(nums) <= 0:
        return -1
    return sum(nums) / float(len(nums))

max_gen = 0
def getBehavioralDiversities(outputDirectory):
    global max_gen

    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    bd_list_per_gen = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    
        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        done = False

        for line in f:

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])
                if gen > max_gen:
                    max_gen = gen
                while len(bd_list_per_gen) <= gen:
                    bd_list_per_gen.append([])

            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break
        
            if line.startswith("Behavioral diversity:"):
                bd = float(line.split()[-1])
                bd_list_per_gen[gen].append(bd)
            
        i += 1

    return [mean(x) for x in bd_list_per_gen]


print "generation," + str([n for (n,d) in dirs]).replace(" ","").replace("]","").replace("[","").replace("'","")

dir_bd_lists = [getBehavioralDiversities(d) for (n,d) in dirs]
for g in range(max_gen+1):
    out_str = str(g) + ","
    for bd_list in dir_bd_lists:
        try:
            bd = "%0.3f," % bd_list[g]
        except:
            bd = ","
        out_str += bd
    print out_str[:-1]
