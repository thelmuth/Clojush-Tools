#import math
import os
#import sys

# Set these before running:

## For the ULTRA paper
#dir1 = "Results/gecco13/bio-normal/"
#dir2 = "Results/gecco13/bio-ultra/"
#dir3 = "Results/gecco13/bio-45/"

## Redo of the ULTRA paper runs; prints best ind based on RMSE rather than total error
#dir001 = "Results/GECCO14/order-lexicase/rmse-bio-subtree-81-9/"
#dir003 = "Results/GECCO14/order-lexicase/rmse-bio-subtree-45-45/"
dir004 = "Results/GECCO14/order-lexicase/rmse-bio-tourney/" #uses ULTRA

#dir4 = "Results/gecco13/equal-size-ULTRA/bio/"

#dir5 = "Results/lexicase-paper/subtree-GOs/bio-lex/"
#dir5 = "Results/lexicase-paper/ultra/bio-lex/"

## Runs that might influence an Order Lexicase paper
lex = "Results/GECCO14/order-lexicase/rmse-bio-lexicase/"
order_lex_88 = "Results/GECCO14/order-lexicase/rmse-bio-88/"
order_lex_78 = "Results/GECCO14/order-lexicase/rmse-bio-78/"
order_lex_72 = "Results/GECCO14/order-lexicase/rmse-bio-ol-72/"
order_lex_61 = "Results/GECCO14/order-lexicase/rmse-bio-ol-61/"

prefix1 = "bio-normallog"
prefix2 = "log"

dirs = [#("Normal", dir001, prefix2),
        #("Non-Equal-ULTRA", dir2, prefix2),
        #("Normal45", dir003, prefix2),
        ("ULTRA-Tourney", dir004, prefix2),
        #("ULTRA-Lexicase", dir5, prefix2),
        #("ULTRA-Order-Lexicase", dir6, prefix2),
        #("U-Lexicase", lex, prefix2),
        ("U-OL-88", order_lex_88, prefix2),
        ("U-OL-78", order_lex_78, prefix2),
        ("U-OL-72", order_lex_72, prefix2),
        ("U-OL-61", order_lex_61, prefix2)
        ]

outputFileSuffix = ".txt"

errorType = "float"

def getTrainTest(outputDirectory, outputFilePrefix):
    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    bestFitnessesOfRuns = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
        #sys.stdout.write('.')
        #if i % 50 == 49:
        #    print
    
        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        #final = False
        gen = 0
        train = -1
        test = 0
        cur_gen_train = -1
        done = False

        for line in f:

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])

            if line.startswith("SUCCESS") or line.startswith("FAILURE"):
                done = True

            if line.startswith("RMS-error:"):
                if errorType == "float":
                    cur_gen_train = float(line.split()[-1])
                elif errorType == "int" or errorType == "integer":
                    cur_gen_train = int(line.split()[-1])
                else:
                    raise Exception("errorType of %s is not recognized" % errorType)

                if train == -1 or cur_gen_train < train:
                    train = cur_gen_train

            if train == cur_gen_train:
                if line.startswith("Test RMSE:"):
                    if errorType == "float":
                        test = float(line.split()[-1])
                    elif errorType == "int" or errorType == "integer":
                        test = int(line.split()[-1])
                    else:
                        raise Exception("errorType of %s is not recognized" % errorType)


        bestFitnessesOfRuns.append((gen, train, test, done))
        i += 1

    return bestFitnessesOfRuns


print "Condition,TrainRMSE,TestRMSE"
for (condition, direct, prefix) in dirs:
    trainAndTest = getTrainTest(direct, prefix)

    for (gen, train, test, done) in trainAndTest:
        print "%s,%f,%f" % (condition, train, test)
