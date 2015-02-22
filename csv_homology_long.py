#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

######## For dissertation

# dirs = [("lexicase", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/")]

# dirs = [("lexicase", "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/")]

######## For EHC paper

dirs = [("standard", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard/"),
        ("standardHalfSilenced", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard-half-silenced/" ),
        ("ESM", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/epigenetic-silence-mutation/"),
        ("EHC", "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/EHC/")]


outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area

def mean(nums):
    if len(nums) <= 0:
        return -1
    return sum(nums) / float(len(nums))

max_gen = 0
def getHomologies(outputDirectory):
    global max_gen

    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    homology_list_per_gen = []
    homology_stddev_per_gen = []
    point_evals_per_gen = []

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
                while len(homology_list_per_gen) <= gen:
                    homology_list_per_gen.append([])
                    homology_stddev_per_gen.append([])
                    point_evals_per_gen.append([])

            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break
        
            if line.startswith("Average:             "):
                homology = float(line.split()[-1])
                homology_list_per_gen[gen].append(homology)
            
            if line.startswith("Standard deviation:  "):
                stddev_homology = float(line.split()[-1])
                homology_stddev_per_gen[gen].append(stddev_homology)

            if line.startswith("Number of point (instruction) evaluations so far:"):
                point_evals = int(line.split()[-1])
                point_evals_per_gen[gen].append(point_evals)

        i += 1

    return ([mean(avg_hom) for avg_hom in homology_list_per_gen],
            [mean(stddev_hom) for stddev_hom in homology_stddev_per_gen],
            [mean(point_evals) for point_evals in point_evals_per_gen],
            [len(avg_hom) for avg_hom in homology_list_per_gen])

#print "generation," + str([n for (n,d) in dirs]).replace(" ","").replace("]","").replace("[","").replace("'","")
print "setting,generation,runsAtThisGen,averagePointEvals,averageHomology,standardDeviationHomology"

for (n,d) in dirs:
    (mean_avg_hom, mean_stddev_hom, mean_point_evals, num_runs) = getHomologies(d)
    for g in range(len(mean_avg_hom)):
        out_str = "%s,%i,%i,%f,%f,%f" % (n, g, num_runs[g], mean_point_evals[g], mean_avg_hom[g], mean_stddev_hom[g])
        print out_str


# dir_homology_lists = [getHomologies(d) for (n,d) in dirs]
# for g in range(max_gen+1):
#     out_str = str(g) + ","
#     for homology_list in dir_homology_lists:
#         try:
#             homology = "%0.3f," % homology_list[g]
#         except:
#             homology = ","
#         out_str += homology
#     print out_str[:-1]
