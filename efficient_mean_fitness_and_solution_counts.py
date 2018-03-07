#!/usr/bin/python
import os, sys
from sys import maxint

# Set these before running:

### Parent selection v2: tournament

#outputDirectory = "Results/parent-selection-v2/tournament/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/tournament/syllables/"
outputDirectory = "Results/parent-selection-v2/tournament/vector-average/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"



errorType = "float"

# Some functions
def median(lst):
    if len(lst) <= 0:
        return False
    sorts = sorted(lst)
    length = len(lst)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def mean(nums):
    if len(nums) <= 0:
        return False
    return sum(nums) / float(len(nums))

def reverse_readline(filename, buf_size=8192):
    """a generator that returns the lines of a file in reverse order
       From: https://stackoverflow.com/questions/2301789/read-a-file-in-reverse-order-using-python"""
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        total_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(total_size, offset + buf_size)
            fh.seek(-offset, os.SEEK_END)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # the first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # if the previous chunk starts right from the beginning of line
                # do not concact the segment to the last line of new chunk
                # instead, yield the segment first 
                if buffer[-1] is not '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if len(lines[index]):
                    yield lines[index]
        yield segment


# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

print
print "           Directory of results:"
print outputDirectory

bestFitnessesOfRuns = []
testFitnessOfBest = []
testFitnessOfSimplifiedBest = []
errorThreshold = maxint
errorThresholdPerCase = maxint
numCases = maxint

fileName0 = (outputFilePrefix + str(i) + outputFileSuffix)
f0 = open(outputDirectory + fileName0)

for line in f0:
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

    if errorThresholdPerCase != maxint and numCases != maxint:
        break

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    sys.stdout.write("%4i" % i)
    sys.stdout.flush()
    if i % 25 == 24:
        print

    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
#    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    best_mean_error = maxint
    done = False

    bestTest = maxint
    simpBestTest = maxint

    if os.path.getsize(outputDirectory + fileName) == 0:
        bestFitnessesOfRuns.append((gen, best_mean_error, done))
        testFitnessOfBest.append(bestTest)
        testFitnessOfSimplifiedBest.append(simpBestTest)
        i += 1
        continue

    for line in reverse_readline(outputDirectory + fileName):

        if line.startswith(";; -*- Report") and gen == 0:
            gen = int(line.split()[-1])

        if gen != 0 and best_mean_error < maxint:
            break

        if line.startswith("SUCCESS"):
            done = "SUCCESS"

        if line.startswith("FAILURE"):
            done = "FAILURE"

        if line.startswith("Mean:"):
            gen_best_error = -1
            if errorType == "float":
                gen_best_error = float(line.split()[-1])
            elif errorType == "int" or errorType == "integer":
                gen_best_error = int(line.split()[-1])
            else:
                raise Exception("errorType of %s is not recognized" % errorType)

            if gen_best_error < best_mean_error:
                best_mean_error = gen_best_error

        if line.startswith("Test total error for best:") and done:
            try:
                bestTest = int(line.split()[-1].strip("Nn"))
            except ValueError, e:
                bestTest = float(line.split()[-1].strip("Nn"))

        if line.startswith("Test total error for best:") and not done:
            try:
                simpBestTest = int(line.split()[-1].strip("Nn"))
            except ValueError, e:
                simpBestTest = float(line.split()[-1].strip("Nn"))


    bestFitnessesOfRuns.append((gen, best_mean_error, done))
    testFitnessOfBest.append(bestTest)
    testFitnessOfSimplifiedBest.append(simpBestTest)
            
    i += 1

print
print "Error threshold per case:", errorThresholdPerCase
print "-------------------------------------------------"

for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    doneSym = ""
    if fitness <= errorThresholdPerCase:
        doneSym = " <- suc"
        if not done:
            doneSym += "$$$$$$ ERROR $$$$$$" #Should never get here
        if len(testFitnessOfBest) > i and testFitnessOfBest[i] < maxint:
            if isinstance(testFitnessOfBest[i], int):
                doneSym += " | test = %i" % testFitnessOfBest[i]
            else:
                doneSym += " | test = %.3f" % testFitnessOfBest[i]
        if len(testFitnessOfSimplifiedBest) > i and testFitnessOfSimplifiedBest[i] < maxint:
            if isinstance(testFitnessOfSimplifiedBest[i], int):
                doneSym += " | test on simplified = %i" % testFitnessOfSimplifiedBest[i]
            else:
                doneSym += " | test on simplified = %.4f" % testFitnessOfSimplifiedBest[i] #TMH this line changed
    elif not done:
        doneSym = " -- not done"
    if fitness >= 0.001 or fitness == 0.0:
        print "Run: %3i  | Gen: %5i  | Best Fitness (mean) = %8.4f%s" % (i, gen, fitness, doneSym)
    else:
        print "Run: %3i  | Gen: %5i  | Best Fitness (mean) = %.4e%s" % (i, gen, fitness, doneSym)

totalFitness = 0
inds = 0
perfectSolutions = 0
perfectOnTestSet = 0
simpPerfectOnTestSet = 0
trainSolutionGens = []
testSolutionGens = []

for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    if done:
        totalFitness += fitness
        inds += 1
        if fitness <= errorThresholdPerCase:
            perfectSolutions += 1
            trainSolutionGens.append(gen)
            if len(testFitnessOfBest) > i:
                if testFitnessOfBest[i] <= errorThresholdPerCase:
                    perfectOnTestSet += 1
                    testSolutionGens.append(gen)
            if len(testFitnessOfSimplifiedBest) > i:
                if testFitnessOfSimplifiedBest[i] <= errorThresholdPerCase:
                    simpPerfectOnTestSet += 1

if len(trainSolutionGens) > 0:
    print "------------------------------------------------------------"
    print "Training Solution Generations:"
    print "Mean:      ", mean(trainSolutionGens)
    print "Minimum:   ", min(trainSolutionGens)
    print "Median:    ", median(trainSolutionGens)
    print "Maximum:   ", max(trainSolutionGens)

    if len(testSolutionGens) > 0:
        print "--------------------------"
        print "Test Solution Generations:"
        print "Mean:      ", mean(testSolutionGens)
        print "Minimum:   ", min(testSolutionGens)
        print "Median:    ", median(testSolutionGens)
        print "Maximum:   ", max(testSolutionGens)

print "------------------------------------------------------------"

print "Number of finished runs:            %4i" % inds
print "Solutions found:                    %4i" % (perfectSolutions)
print "Zero error on test set:             %4i" % perfectOnTestSet
print "Simplified zero error on test set:  %4i" % simpPerfectOnTestSet

print "------------------------------------------------------------"

if inds > 0:
    print "MBF: %.5f" % (totalFitness / float(inds))
