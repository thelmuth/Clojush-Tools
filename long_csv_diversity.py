#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

## For EHC paper

# dirs = [("Baseline", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard/"),
#         ("Ep0", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard-half-silenced/"),
#         ("EHC1", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/EHC/"),
#         ("Ep1M", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/epigenetic-silence-mutation/")
#         ]

# dirs = [("Baseline", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/"),
#         ("Ep0", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney-7/standard-half-silenced/"),
#         ("EHC1", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney-7/EHC/"),
#         ("Ep1M", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/EHC-testing/tourney-7/")
#         ]

# dirs = [("Baseline", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard/"),
#         ("Ep0", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard-half-silenced/"),
#         ("EHC1", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/EHC/"),
#         ("Ep1M", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/epigenetic-silence-mutation/")
#         ]


############ For GECCO16 Diversity Workshop - Diversity Recovery paper
######## Replace Space With Newline
### Div drop 25
# dirs = [("Drop25-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run0/"),
#         ("Drop25-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run0/")
#         ]
# dirs = [("Drop25-Run8-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run8/"),
#         ("Drop25-Run8-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run8/")
#         ]

### Div > 90
# dirs = [("Div90-Run6-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run6/"),
#         ("Div90-Run6-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run6/")
#         ]
# dirs = [("Div90-Run10-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run10/"),
#         ("Div90-Run10-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run10/")
#         ]

### tourney Div < 15
# dirs = [("Div15-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run0/"),
#         ("Div15-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run0/")
#         ]
# dirs = [("Div15-Run1-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run1/"),
#         ("Div15-Run1-tournament", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run1/")
#         ]

####### Double Letters
### Div drop 25
# dirs = [("Drop25-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/lexicase/run0/"),
#         ("Drop25-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/tournament/run0/")
#         ]
# dirs = [("Drop25-Run21-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/lexicase/run21/"),
#         ("Drop25-Run21-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/tournament/run21/")
#         ]

### Div > 90
# dirs = [("Div90-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/lexicase/run0/"),
#         ("Div90-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/tournament/run0/")
#         ]
# dirs = [("Div90-Run3-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/lexicase/run3/"),
#         ("Div90-Run3-tournament", "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/tournament/run3/")
#         ]

### tourney Div < 15
# dirs = [("Div15-Run0-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/lexicase/run0/"),
#         ("Div15-Run0-tournament", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/tournament/run0/")
#         ]
# dirs = [("Div15-Run1-lexicase", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/lexicase/run1/"),
#         ("Div15-Run1-tournament", "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/tournament/run1/")
#         ]


############ For GPTP 17 - Sarah Troise's weighted lexicase paper

# dirs = [("Number-of-Zeros", "/home/stroise/results/weighted-lexicase/number-of-zeros/replace-space-with-newline/"),
#         ("Number-of-Nonzeros-Inverse", "/home/stroise/results/weighted-lexicase/number-of-nonzero-inverse/replace-space-with-newline/"),
#         ("Median-Inverse", "/home/thelmuth/Results/weighted-lexicase/weighted-lexicase/median-inverse/replace-space-with-newline/"),
#         ("Number-of-Zeros-Inverse", "/home/stroise/results/weighted-lexicase/number-of-zeros-inverse/replace-space-with-newline/"),
#         ("Number-of-Nonzeros", "/home/stroise/results/weighted-lexicase/number-of-nonzero/replace-space-with-newline/"),
#         ("Median", "/home/stroise/results/weighted-lexicase/median/replace-space-with-newline/"),
#         ("Average", "/home/thelmuth/Results/weighted-lexicase/weighted-lexicase/average/replace-space-with-newline/"),
#         ("Variance", "/home/stroise/results/weighted-lexicase/variance/replace-space-with-newline/"),
#         ("Variance-Inverse", "/home/thelmuth/Results/weighted-lexicase/weighted-lexicase/variance-inverse/replace-space-with-newline/")
#        ]

# dirs = [("Number-of-Zeros", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/number-of-zeros/replace-space-with-newline/"),
#         ("Number-of-Nonzeros-Inverse", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/number-of-nonzero-inverse/replace-space-with-newline/"),
#         ("Median-Inverse", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/median-inverse/replace-space-with-newline/"),
#         ("Number-of-Zeros-Inverse", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/number-of-zeros-inverse/replace-space-with-newline/"),
#         ("Number-of-Nonzeros", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/number-of-nonzero/replace-space-with-newline/"),
#         ("Median", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/median/replace-space-with-newline/"),
#         ("Average", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/average/replace-space-with-newline/"),
#         ("Variance", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/variance/replace-space-with-newline/"),
#         ("Variance-Inverse", "/home/thelmuth/Results/weighted-lexicase/ranked-lexicase/variance-inverse/replace-space-with-newline/")
#         ]

# dirs = [("Regular-Lexicase", "/home/thelmuth/Results/parent-selection-v2/lexicase/replace-space-with-newline"),
#         ("Number-of-Zeros", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/number-of-zeros/replace-space-with-newline/"),
#         ("Number-of-Nonzeros-Inverse", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/number-of-nonzero-inverse/replace-space-with-newline/"),
#         ("Median-Inverse", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/median-inverse/replace-space-with-newline/"),
#         ("Number-of-Zeros-Inverse", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/number-of-zeros-inverse/replace-space-with-newline/"),
#         ("Number-of-Nonzeros", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/number-of-nonzero/replace-space-with-newline/"),
#         ("Median", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/median/replace-space-with-newline/"),
#         ("Average", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/average/replace-space-with-newline/"),
#         ("Variance", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/variance/replace-space-with-newline/"),
#         ("Variance-Inverse", "/home/thelmuth/Results/weighted-lexicase/bias-lexicase/variance-inverse/replace-space-with-newline/")
#         ]

dirs = [("Regular-Lexicase", "/home/thelmuth/Results/parent-selection-v2/lexicase/replace-space-with-newline")]





outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area

# def mean(nums):
#     if len(nums) <= 0:
#         return -1
#     return sum(nums) / float(len(nums))

#max_gen = 0
def printBehavioralDiversitiesLong(method, outputDirectory):
    #global max_gen

    run_num = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    #bd_list_per_gen = []

    while (outputFilePrefix + str(run_num) + outputFileSuffix) in dirList:
    
        fileName = (outputFilePrefix + str(run_num) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        done = False
        behavioral_diversity = -1
        point_evals = -1

        for line in f:

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])
                # if gen > max_gen:
                #     max_gen = gen
                # while len(bd_list_per_gen) <= gen:
                #     bd_list_per_gen.append([])

            if line.startswith("Behavioral diversity:"):
                behavioral_diversity = float(line.split()[-1])
#                bd_list_per_gen[gen].append(bd)

            if line.startswith("Error (vector) diversity:"):
                error_vector_diversity = float(line.split()[-1])                
 
            if line.startswith("Number of point (instruction) evaluations so far:"):
                point_evals = int(line.split()[-1])
                print "%s,%i,%i,%i,%0.3f,%0.3f" % (method, run_num, gen, point_evals, behavioral_diversity, error_vector_diversity)


            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break        

           
        run_num += 1

    return


#print "method,run,generation,ptevals,behavioral_diversity"
print "method,trial,generation,ptevals,behavioral_diversity,error_vector_diversity"

for (method, directory) in dirs:
    printBehavioralDiversitiesLong(method, directory)

# dir_bd_lists = [getBehavioralDiversities(d) for (n,d) in dirs]
# for g in range(max_gen+1):
#     out_str = str(g) + ","
#     for bd_list in dir_bd_lists:
#         try:
#             bd = "%0.3f," % bd_list[g]
#         except:
#             bd = ","
#         out_str += bd
#     print out_str[:-1]
