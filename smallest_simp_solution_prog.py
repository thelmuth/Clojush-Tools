#!/usr/bin/python
import os
from sys import maxint

# Set these before running:


outputDirectory = "/home/thelmuth/Results/counterexample-driven-gp/add-case-after-50-gens/scrabble-score"

#######################################################################################
########################### Parent Selection Experiments ##############################
#######################################################################################

#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/even-squares/extra-errors/lexicase/"

#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/extra-errors/lexicase/"

#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/scrabble-score/fixed-ommitted-instructions/lexicase/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/fixed-ommitted-instructions/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/fixed-ommitted-instructions/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/added-training-cases/lexicase/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/added-training-cases/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/added-training-cases/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed-backup/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed-backup/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed-backup/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines-extra-errors/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines-extra-errors/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines-extra-errors/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/extra-errors/lexicase/"

#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/ifs-7/"

## Yuriy's problems

#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/median/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/median/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/median/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/ifs-7/"




##########################################################################################
### EHC
##########################################################################################

# 2) Normal EHC - max evals 3e10, silence mut on, hill climbing on
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/ifs-7/"

# 3) max evals 3e10, silence mut on, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/ifs-7/"

# 4) max gens 300, silence mut on, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/ifs-7/"

# 5) max evals 3e10, silence mut off, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/ifs-7/"

# 6) max gens 300, silence mut off, hill climbing off, init max prog size 200
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/ifs-7/"

# W) max evals 3e10, silence mut off, hill climbing off, init max prog size 400, half genes silenced
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney/standard-half-silenced/"

# X) these are to see how many point evaluations are used in a typical GP run of this problem
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/ifs-7/"


########## EHC GECCO Paper

#outputDirectory = "Results/bench-prog-synth/count-odds/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/count-odds/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/double-letters/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/double-letters/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/grade/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/grade/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/lexicase/standard/"

#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/lexicase/standard/"

#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/lexicase/standard/"

# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard-half-silenced/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/epigenetic-silence-mutation/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/EHC/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/lexicase/standard/"


##########################################################################################
### Multi-Chance Lexicase
##########################################################################################

#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-2/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-3/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-4/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-5/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-90/"


outputFilePrefix = "log"
outputFileSuffix = ".txt"


#outputFilePrefix = "bio-ultralog"
#outputFilePrefix = "bio-normallog"

errorType = "float"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

print "Directory of results:", outputDirectory

bestFitnessesOfRuns = []
testFitnessOfBest = []
testFitnessOfSimplifiedBest = []
errorThreshold = maxint
errorThresholdPerCase = maxint
sizeOfFinalProg = []
simpSizeOfFinalProg = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
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



print "-------------------------------------------------"

smallestSimpGeneralizingSolutionProgSize = maxint

print "RunNumber,MeanErrorOnTraining,TotalErrorOnTest,SimplifiedTotalErrorOnTest,OriginalSize,SimplifiedSize"
for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    errorTest = "-1"
    simpErrorTest = "-1"
    error = "-1"

    if fitness == 0.0:
        error = "0.0"
    else:
        error = "%f" % fitness

#    if fitness <= errorThresholdPerCase:
#        doneSym = " <- suc"
#        if not done:
#            doneSym += "$$$$$$ ERROR $$$$$$" #Should never get here
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

        if testFitnessOfSimplifiedBest[i] == 0.0 and simpSizeOfFinalProg[i] < smallestSimpGeneralizingSolutionProgSize:
            smallestSimpGeneralizingSolutionProgSize = simpSizeOfFinalProg[i]

    print "%i,%s,%s,%s,%i,%i" % (i, error, errorTest, simpErrorTest, sizeOfFinalProg[i], simpSizeOfFinalProg[i])
    # else:
    #     print "Run: %3i  | Gen: %5i  | Best Fitness (mean) = %.4e%s" % (i, gen, fitness, doneSym)

print "-------------------------------------------------"
print "Smallest simplified program size of generalizing solution:", smallestSimpGeneralizingSolutionProgSize
