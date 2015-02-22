import math
import os
import sys

# Set these before running:
#outputDirectory = "Results/GECCO13/mom2/"
#outputDirectory = "Results/GECCO13/mom2-lexicase/"
#outputDirectory = "Results/GECCO13/mom2-ultra/"
#outputDirectory = "Results/GECCO13/mom2-tags/"
#outputDirectory = "Results/GECCO13/mom2-env/"
#outputDirectory = "Results/GECCO13/mom2-lex-ultra/"

#outputDirectory = "Results/GECCO13/mom3/"
#outputDirectory = "Results/GECCO13/mom3-lexicase/"
#outputDirectory = "Results/GECCO13/mom3-ultra/"
#outputDirectory = "Results/GECCO13/mom3-lex-ultra/"

#outputDirectory = "Results/GECCO13/big-mom3/mom3-lex-ultra/"

#outputDirectory = "Results/GECCO13/mux6-normal/"
#outputDirectory = "Results/GECCO13/mux6-ultra/"

#outputDirectory = "Results/GECCO13/factorial-normal/"
#outputDirectory = "Results/GECCO13/factorial-ultra/"
#outputDirectory = "Results/GECCO13/factorial-ultra-large/"
#outputDirectory = "Results/GECCO13/factorial-normal-500gens/"
#outputDirectory = "Results/GECCO13/factorial-ultra-500gens/"

#outputDirectory = "Results/lexicase-paper/ultra/dm3-lex/"
#outputDirectory = "Results/thesis/change-exploratory/"
#outputDirectory = "Results/thesis/change-exploratory-2/"

#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-empties/"
#outputDirectory = "Results/GECCO14/wc/domains-lower-ultra-padding/"
#outputDirectory = "Results/GECCO14/wc/padding-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/bushy-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/"
outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-two/"
#outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-100/"
#outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-0/"


#outputDirectory = "Results/ULTRA-redo/pagie/ultra/"
#outputDirectory = "Results/padding-ultra/pagie/padding/"
#outputDirectory = "Results/padding-ultra/pagie/padding200/"
#outputDirectory = "Results/padding-ultra/pagie/padding150/"
#outputDirectory = "Results/padding-ultra/pagie/padding-bug-finding/"
#outputDirectory = "Results/padding-ultra/pagie/fixed-padding/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

verbose = True
if(len(sys.argv) > 1):
    verbose = False

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    success = False
    simpl = False

    if verbose:
        print
        print "-------------------------------------------------"
        print "------------------ Run %i ------------------------" % i
        print

    testForBest = 5

    for line in f:
        if line.startswith("Successful program: "):
            if verbose:
                print line
                print
            else:
                if sys.argv[1] != "test" or testForBest == 0:
                    print line[len("Successful program: "):-1]
            success = True

        if simpl == True and verbose:
            print "Simplification after 1000 steps:"
            print line
            break

        if success and line.startswith("step: 1000"):
            simpl = True

        if line.startswith("Test total error for best:"):
            testForBest = int(line.split()[-1].strip("Nn"))

    i += 1
