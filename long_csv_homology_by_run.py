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

dirs = [("Baseline", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/"),
        ("Ep0", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney-7/standard-half-silenced/"),
        ("EHC1", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney-7/EHC/"),
        ("Ep1M", "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/EHC-testing/tourney-7/")
        ]

# dirs = [("Baseline", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard/"),
#         ("Ep0", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard-half-silenced/"),
#         ("EHC1", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/EHC/"),
#         ("Ep1M", "Results/bench-prog-synth/syllables/ehc-experiments/tourney/epigenetic-silence-mutation/")
#         ]


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
        homology = -1
        point_evals = -1

        for line in f:

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])
                # if gen > max_gen:
                #     max_gen = gen
                # while len(bd_list_per_gen) <= gen:
                #     bd_list_per_gen.append([])

            if line.startswith("Average:") or line.startswith("Average            (sample 1):") or line.startswith("(ALL) Average:"):
                homology = float(line.split()[-1])
#                bd_list_per_gen[gen].append(bd)
 
            if line.startswith("Number of point (instruction) evaluations so far:"):
                point_evals = int(line.split()[-1])
                print "%s,%i,%i,%i,%0.3f" % (method, run_num, gen, point_evals, homology)


            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break        

           
        run_num += 1

    return


#print "method,run,generation,ptevals,behavioral_diversity"
print "method,trial,generation,ptevals,mean_homology"

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
