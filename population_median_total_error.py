#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

#outputDirectory = "Results/kata-ULTRA/one-frame-lexicase/"

#outputDirectory = "Results/gecco13/bio-normal/"
#outputDirectory = "Results/gecco13/bio-ultra/"
#outputDirectory = "Results/gecco13/bio-normal-env/"
#outputDirectory = "Results/gecco13/bio-45/"

#outputDirectory = "Results/gecco13/pagie-normal/"
#outputDirectory = "Results/gecco13/pagie-ultra/"

#outputDirectory = "Results/gecco13/pagie-no-erc-normal/"
#outputDirectory = "Results/gecco13/pagie-hogeweg-no-erc-45/"
#outputDirectory = "Results/gecco13/pagie-no-erc-ultra/" #uses non-equal ultra

#outputDirectory = "Results/gecco13/mom2/"
#outputDirectory = "Results/gecco13/mom2-lexicase/"
#outputDirectory = "Results/gecco13/mom2-ultra/"
#outputDirectory = "Results/gecco13/mom2-tags/"
#outputDirectory = "Results/gecco13/mom2-env/"
#outputDirectory = "Results/gecco13/mom2-lex-ultra/"

#outputDirectory = "Results/gecco13/mom3/"
#outputDirectory = "Results/gecco13/mom3-lexicase/"
#outputDirectory = "Results/gecco13/mom3-ultra/"
#outputDirectory = "Results/gecco13/mom3-lex-ultra/"
#outputDirectory = "Results/gecco13/mom3-lex-ultra-tags/"

#outputDirectory = "Results/gecco13/big-mom3/mom3-lex-ultra/"

#outputDirectory = "Results/gecco13/mux6-normal/"
#outputDirectory = "Results/gecco13/mux6-ultra/"

#outputDirectory = "Results/gecco13/factorial-normal/"
#outputDirectory = "Results/gecco13/factorial-ultra/"
#outputDirectory = "Results/gecco13/factorial-ultra-large/"
#outputDirectory = "Results/gecco13/factorial-normal-500gens/"
#outputDirectory = "Results/gecco13/factorial-ultra-500gens/"
#outputDirectory = "Results/gecco13/factorial-no-lex-500gens/"
#outputDirectory = "Results/gecco13/factorial-ultra-no-lex-500gens/"

#outputDirectory = "Results/lexicase-paper/subtree-GOs/factorial-tourn/"
#outputDirectory = "Results/lexicase-paper/subtree-GOs/factorial-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/NON-EQUAL-SIZE/factorial-tourn/"
#outputDirectory = "Results/lexicase-paper/ultra/NON-EQUAL-SIZE/factorial-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/factorial-EGL/"

#outputDirectory = "Results/lexicase-paper/bio-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/bio-lex/"

#outputDirectory = "Results/gecco13/equal-size-ULTRA/bio/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/pagie-no-erc/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/factorial/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/factorial-tourney/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/mux6/"

#outputDirectory = "Results/lexicase-paper/ultra/dm3-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/dm3-tourney/"
#outputDirectory = "Results/lexicase-paper/subtree-GOs/dm3-lexicase/"
#outputDirectory = "Results/lexicase-paper/subtree-GOs/dm3-tourney/"
#outputDirectory = "Results/lexicase-paper/ultra/dm3-small-pop-lex/" 
#outputDirectory = "Results/lexicase-paper/ultra/dm4-lex/" 

#outputDirectory = "Results/timing/ultra/dm3-lexicase/"
#outputDirectory = "Results/timing/ultra/dm3-tourney/"

#outputDirectory = "Results/lexicase-paper/ael/factorial-ael/"
#outputDirectory = "Results/lexicase-paper/ael/factorial-new-rand/"
#outputDirectory = "Results/lexicase-paper/ael/dm3-ael/"

#outputDirectory = "Results/exploratory-trad-programming/change-exploratory/"
#outputDirectory = "Results/exploratory-trad-programming/change-exploratory-2/"
#outputDirectory = "Results/exploratory-trad-programming/change-exploratory-intextra/"
#outputDirectory = "Results/exploratory-trad-programming/change-exploratory-minimal/"
#outputDirectory = "Results/exploratory-trad-programming/change-no-mut-ultra/"
#outputDirectory = "Results/exploratory-trad-programming/change-no-paren-mutation-ultra/"

#outputDirectory = "Results/ultra/DOT-normal/"
#outputDirectory = "Results/ultra/DOT-no-paren-ULTRA/"

#outputDirectory = "Results/thesis/fizz-buzz-exploratory/"
#outputDirectory = "Results/thesis/fizz-buzz-exploratory-ITS/"
#outputDirectory = "Results/thesis/fizz-buzz-exploratory-ITS2/"

#outputDirectory = "Results/thesis/multiplicative-fitness/factorial/"
#outputDirectory = "Results/thesis/multiplicative-fitness/fizz-buzz-mult/"
#outputDirectory = "Results/thesis/multiplicative-fitness/fizz-buzz-tourney/"
#outputDirectory = "Results/thesis/multiplicative-fitness/fizz-buzz-lex/"

#outputDirectory = "Results/GECCO14/order-lexicase/factorial/"
#outputDirectory = "Results/GECCO14/order-lexicase/factorial-10/"

#outputDirectory = "Results/GECCO14/order-lexicase/pagie-946/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-895/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-80/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-64/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-464/"

#outputDirectory = "Results/thesis/wc-exploratory/"
#outputDirectory = "Results/GECCO14/wc/domains-all-cases-empties/" #bad ULTRA params
#outputDirectory = "Results/GECCO14/wc/domains-all-cases-padding/" #bad ULTRA params
#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-empties/"
#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-padding/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-BAD-LOGS/"
# outputDirectory = "Results/GECCO14/wc/padding-max-points-1000/"
# outputDirectory = "Results/GECCO14/wc/bushy-max-points-1000/"
# outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/"
# outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000/"
# outputDirectory = "Results/GECCO14/wc/ultra-params-05-05-10/"
# outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-100/"
# outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-0/"
# outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-two/"
# outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000-two/"

#outputDirectory = "Results/ULTRA-redo/pagie/subtree-80-10-10/"
#outputDirectory = "Results/ULTRA-redo/pagie/subtree-45-45-10/"
#outputDirectory = "Results/ULTRA-redo/pagie/ultra/"

#############  For simplification paper
#outputDirectory = "Results/padding-ultra/pagie/padding/"
#outputDirectory = "Results/GECCO14/simplification/odd/"
#outputDirectory = "Results/padding-ultra/pagie/padding150/"
#outputDirectory = "Results/padding-ultra/pagie/fixed-padding/"

#outputDirectory = "Results/padding-ultra/factorial/ultra-padding/"
#outputDirectory = "Results/padding-ultra/mux6/ultra-padding/"

#outputDirectory = "Results/ULTRA-mut/wc/print-instr-percents/"
#outputDirectory = "Results/ULTRA-mut/wc/ultra-005-005-10/"
#outputDirectory = "Results/ULTRA-mut/wc/split-ULTRA-50-50/"
#outputDirectory = "Results/ULTRA-mut/wc/split-ULTRA-75-25/"
#outputDirectory = "Results/ULTRA-mut/wc/split-ULTRA-90-10/"

#outputDirectory = "Results/ULTRA-redo/wc/subtree-80-10-10/"

############ For lexicase paper resub
#outputDirectory = "Results/lexicase-paper/resub/dm3/lex-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney8-ultra/"

outputDirectory = "Results/lexicase-paper/resub/factorial/lex-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney2-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/tourney4-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney8-ultra/"

# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney2-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney4-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney6-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney8-ultra/"

# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney2-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney4-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney6-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney8-ultra/"

# outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney2-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney4-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney6-ultra/"
# outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/wc/tourney3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/tourney5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-7/"


#outputDirectory = "Results/exploratory-int-sqrt/lex/"

#outputDirectory = "Results/lexicase-paper/resub/wc/tourney40/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney40-ultra/"



outputFilePrefix = "log"
outputFileSuffix = ".txt"


#outputFilePrefix = "bio-ultralog"
#outputFilePrefix = "bio-normallog"

errorType = "int"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)


bestFitnessesOfRuns = []
testFitnessOfBest = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    best_median_error = maxint
    done = False

    bestTest = maxint

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Median total errors"):
            gen_best_error = -1
            if line[-2] == "N" or line[-2] == "n":
                line = line[:-2]
            try:
                gen_best_error = float(line.split()[-1])
            except ValueError:
                try:
                    gen_best_error = int(line.split()[-1])
                except ValueError:
                    raise Exception("errorType of %s is not recognized" % errorType)

            if gen_best_error < best_median_error:
                best_median_error = gen_best_error

        if line.startswith("Test total error for best:"):
            try:
                bestTest = int(line.split()[-1].strip("Nn"))
            except ValueError, e:
                bestTest = float(line.split()[-1].strip("Nn"))

    bestFitnessesOfRuns.append((gen, best_median_error, done))

    if bestTest < maxint:
        testFitnessOfBest.append(bestTest)
            
    i += 1


#print
#print "Best fitnesses of runs:"
for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    doneSym = ""
    if fitness == 0:
        doneSym = " <- suc"
        if len(testFitnessOfBest) > i:
            doneSym += " | test = %i" % testFitnessOfBest[i]
    elif not done:
        doneSym = " --"
    if fitness >= 0.001:
        print "Run: %3i  | Gen: %5i  | Best Fitness (median) = %8.3f%s" % (i, gen, fitness, doneSym)
    else:
        print "Run: %3i  | Gen: %5i  | Best Fitness (median) = %.3e%s" % (i, gen, fitness, doneSym)

totalFitness = 0
inds = 0
perfectSolutions = 0
for (gen, fitness, done) in bestFitnessesOfRuns:
    if done:
        totalFitness += fitness
        inds += 1
        if fitness == 0.0:
            perfectSolutions += 1


print "-----"
print "Number of finished runs: %i" % inds
print "perfect solutions: %i" % (perfectSolutions)
if inds > 0:
    print "Mean Median Population Fitnesses: %.5f" % (totalFitness / float(inds))
