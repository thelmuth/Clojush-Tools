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

#outputDirectory = "Results/GECCO14/simplification/odd/"

outputDirectory = "Results/padding-ultra/pagie/padding-bug-finding/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    best_program = ""

    for line in f:
        if line.startswith("Best program: "):
            best_program = line[len("Best program: "):].strip()

    print best_program

    i += 1
