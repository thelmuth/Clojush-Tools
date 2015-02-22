#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

outputDirPrefix = "Results/bench-prog-synth/"
outputDirPostfix = "/parent-selection/lexicase/"

problems = ["checksum",
            "collatz-numbers",
            "compare-string-lengths",
            "count-odds",
            "digits",
            "double-letters",
            "even-squares",
            "for-loop-index",
            "grade",
            "last-index-of-zero",
            "median",
            "mirror-image",
            "negative-to-zero",
            "number-io",
            "pig-latin",
            "replace-space-with-newline",
            "scrabble-score",
            "smallest",
            "small-or-large",
            "string-differences",
            "string-lengths-backwards",
            "sum-of-squares",
            "super-anagrams",
            "syllables",
            "vector-average",
            "vectors-summed",
            "wallis-pi",
            "word-stats",
            "x-word-lines"]


outputFilePrefix = "log"
outputFileSuffix = ".txt"

errorType = "float"


def print_for_problem(prob):

    outputDirectory = outputDirPrefix + prob + outputDirPostfix

    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    bestFitnessesOfRuns = []
    testFitnessOfBest = []
    testFitnessOfSimplifiedBest = []
    errorThreshold = maxint
    errorThresholdPerCase = maxint
    sizeOfFinalProg = []
    simpSizeOfFinalProg = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
            
        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        best_mean_error = maxint
        done = False

        bestTest = maxint
        simpBestTest = maxint
        size = 0
        simpSize = -1

        for line in f:

            if line.startswith("error-threshold"):
                try:
                    errorThreshold = int(line.split()[-1])
                except ValueError, e:
                    errorThreshold = float(line.split()[-1])
                if errorThreshold == 0:
                    errorThresholdPerCase = 0

            if errorThresholdPerCase == maxint and line.startswith("Errors:"):
                numCases = len(line.split()) - 1
                errorThresholdPerCase = float(errorThreshold) / numCases

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])

            if line.startswith("SUCCESS"):
                done = "SUCCESS"

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break

            if line.startswith("Mean:") and not done:
                gen_best_error = -1
                if errorType == "float":
                    gen_best_error = float(line.split()[-1])
                elif errorType == "int" or errorType == "integer":
                    gen_best_error = int(line.split()[-1])
                else:
                    raise Exception("errorType of %s is not recognized" % errorType)

                if gen_best_error < best_mean_error:
                    best_mean_error = gen_best_error

            if line.startswith("Test total error for best:") and not done:
                try:
                    bestTest = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    bestTest = float(line.split()[-1].strip("Nn"))

            if line.startswith("Test total error for best:") and done:
                try:
                    simpBestTest = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    simpBestTest = float(line.split()[-1].strip("Nn"))

            if line.startswith("Size:"):
                size = int(line.split()[-1])

            if line.startswith("size:"):
                simpSize = int(line.split()[-1])


        bestFitnessesOfRuns.append((gen, best_mean_error, done))
        testFitnessOfBest.append(bestTest)
        testFitnessOfSimplifiedBest.append(simpBestTest)
        sizeOfFinalProg.append(size)
        simpSizeOfFinalProg.append(simpSize)
            
        i += 1

    for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
        errorTest = "-1"
        simpErrorTest = "-1"
        error = "-1"

        if fitness == 0.0:
            error = "0.0"
        else:
            error = "%f" % fitness

        if len(testFitnessOfBest) > i and testFitnessOfBest[i] < maxint:
            if isinstance(testFitnessOfBest[i], int):
                errorTest = "%i" % testFitnessOfBest[i]
            else:
                errorTest = "%f" % testFitnessOfBest[i]
        if len(testFitnessOfSimplifiedBest) > i and testFitnessOfSimplifiedBest[i] < maxint:
            if isinstance(testFitnessOfSimplifiedBest[i], int):
                simpErrorTest = "%i" % testFitnessOfSimplifiedBest[i]
            else:
                simpErrorTest = "%f" % testFitnessOfSimplifiedBest[i]

        print "%s,%i,%s,%s,%s,%i,%i" % (prob, i, error, errorTest, simpErrorTest, sizeOfFinalProg[i], simpSizeOfFinalProg[i])


print "Problem,RunNumber,MeanErrorOnTraining,TotalErrorOnTest,SimplifiedTotalErrorOnTest,OriginalSize,SimplifiedSize"

for prob in problems:
    print_for_problem(prob)
