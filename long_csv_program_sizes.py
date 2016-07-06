#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

######## For GPTP Plush Paper

dirs = [("Replace Space With Newline", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
        ("Syllables", "Results/bench-prog-synth/syllables/parent-selection/lexicase/"),
        ("Negative To Zero", "Results/bench-prog-synth/negative-to-zero/parent-selection/lexicase/"),
        ("X-Word Lines", "Results/bench-prog-synth/x-word-lines/parent-selection/lexicase/"),
        ("Count Odds", "Results/bench-prog-synth/count-odds/parent-selection/lexicase/")]


outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area

def printSizesLong(method, outputDirectory):

    run_num = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

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

            if line.startswith("Average genome size in population (length):"):
                mean_genome_size = float(line.split()[-1])
 
            if line.startswith("Average program size in population (points):"):
                mean_program_size = float(line.split()[-1])
                print "%s,%i,%i,%0.3f,%0.3f" % (method, run_num, gen, mean_genome_size, mean_program_size)


            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break        

           
        run_num += 1

    return


print "method,trial,generation,mean_genome_size,mean_program_size"

for (method, directory) in dirs:
    printSizesLong(method, directory)
