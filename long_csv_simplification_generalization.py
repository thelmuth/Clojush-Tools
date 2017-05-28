#!/usr/bin/python
import os, glob, re, sys
from sys import maxint

# Set these before running:

######## For simplification and generalization paper

#namespace = "smallest"

namespace = sys.argv[1]

dirs = [("Program", "Results/simplification-generalization/" + namespace + "/program/"),
        ("Genome", "Results/simplification-generalization/" + namespace + "/genome/"),
        ("GenomeBacktracking", "Results/simplification-generalization/" + namespace + "/genome-backtracking/"),
        ("GenomeNoop", "Results/simplification-generalization/" + namespace + "/genome-noop/"),
        ("GenomeBacktrackingNoop", "Results/simplification-generalization/" + namespace + "/genome-backtracking-noop/")]


outputFileGlob = "simp-log*.txt"

# Main area

def printSimpGenLong(method, outputDirectory):

    if outputDirectory[-1] != '/':
        outputDirectory += '/'

    input_files = glob.glob(outputDirectory + outputFileGlob)
    input_files.sort()

    for input_file in input_files:
        f = open(input_file)

        match = re.search(r"simp-log(\d*).txt", input_file)
        log = int(match.group(1))

        trial = -1
        prog_size = -1
#        done = False            
#        behavioral_diversity = -1
#        point_evals = -1

        for line in f:

            if line.startswith("Trial"):
                trial = int(line.split()[-1])

            if line.startswith("Simplified Program Size (points):") or line.startswith("Program Size (points):"):
                prog_size = int(line.split()[-1])
 
            if line.startswith("Total Test Error:"):
                if not line[-2].isdigit(): # Removes N from numbers like 3431N
                    line = line[:-2]

                # try: #make sure works with int and float errors
                try:
                    test_error = int(line.split()[-1])
                    print "%s,%i,%i,%s,%i,%i" % (method, log, trial, "unsimplified", prog_size, test_error)
                except ValueError:
                    test_error = float(line.split()[-1])
                    print "%s,%i,%i,%s,%i,%0.3f" % (method, log, trial, "unsimplified", prog_size, test_error)

            if line.startswith("Simplified Total Test Error:"):
                if not line[-2].isdigit(): # Removes N from numbers like 3431N
                    line = line[:-2]

                # try: #make sure works with int and float errors
                try:
                    test_error = int(line.split()[-1])
                    print "%s,%i,%i,%s,%i,%i" % (method, log, trial, "simplified", prog_size, test_error)
                except ValueError:
                    test_error = float(line.split()[-1])
                    print "%s,%i,%i,%s,%i,%0.3f" % (method, log, trial, "simplified", prog_size, test_error)


print "method,log,trial,type,programSize,testError"


for (method, directory) in dirs:
    printSimpGenLong(method, directory)
