#import math
import os
#import sys

# Set these before running:

#dir1 = "Results/gecco13/DM/mom2-lex-ultra"
dir2 = "Results/plush-testing/dm2-selected-sizes/"

prefix1 = "log"

dirs = [("Plush", dir2, prefix1)]

outputFileSuffix = ".txt"

def my_mean(list_of_nums):
    if len(list_of_nums) == 0:
        return 0.0
    return float(sum(list_of_nums)) / float(len(list_of_nums))

def getProgramSizes(outputDirectory, outputFilePrefix):
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    max_generations = 0
    sizes_per_gen = []
    parent_sizes_per_gen = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        mean_size = 0

        for line in f:
            if i == 0:
                if line.startswith("max-generations"):
                    max_generations = int(line.split()[-1])
                    sizes_per_gen = [[] for x in range(max_generations + 1)]
                    parent_sizes_per_gen = [[] for x in range(max_generations + 1)]

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])

            if line.startswith("Average program size in population"):
                mean_size = float(line.split()[-1])
                sizes_per_gen[gen].append(mean_size)

            if line.startswith("Average selected parent genome size for generation"):
                parent_size = float(line.split()[-1])
                parent_sizes_per_gen[gen].append(parent_size)

        i += 1

    return (sizes_per_gen, parent_sizes_per_gen)


print "Condition,Generation,MeanProgramSize,ParentMeanProgramSize,DifBetweenParentSizeAndMeanSize"
for (condition, directory, prefix) in dirs:
    sizes, parent_sizes = getProgramSizes(directory, prefix)

    for gen, gen_sizes, gen_par in zip(range(len(sizes)), sizes, parent_sizes):
        print "%s,%i,%f,%f,%f" % (condition, gen, my_mean(gen_sizes), my_mean(gen_par), my_mean(gen_par) - my_mean(gen_sizes))
