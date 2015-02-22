#import math
import os
#import sys
from scipy.stats import mstats

# Set these before running:

dir1 = "Results/gecco13/bio-normal/"
dir2 = "Results/gecco13/bio-ultra/"
dir3 = "Results/gecco13/bio-45/"
dir4 = "Results/gecco13/equal-size-ULTRA/bio/"
dir5 = "Results/GECCO14/order-lexicase/bio-88/"
dir6 = "Results/lexicase-paper/ultra/bio-lex/"

rmse_bio_tourney = "Results/GECCO14/order-lexicase/rmse-bio-tourney"
order_lex_72 = "Results/GECCO14/order-lexicase/rmse-bio-ol-72/"

prefix1 = "bio-normallog"
prefix2 = "log"

dirs = [#("Normal", dir1, prefix1),
        #("ULTRA-non-equal-size", dir2, prefix2),
        #("Normal-45", dir3, prefix2),
        #("ULTRA", dir4, prefix2),
        #("ULTRA-plus-order-lexicase", dir5, prefix2),
        #("ULTRA-lexicase", dir6, prefix2)
         ("ULTRA-Tourney", rmse_bio_tourney, prefix2),
         ("Order-Lexicase-72", order_lex_72, prefix2)
         ]

outputFileSuffix = ".txt"

errorType = "float"

def getTrainTest(outputDirectory, outputFilePrefix):
    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    trainFits = []
    testFits = []

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

        trainFits.append(train)
        testFits.append(test)
        i += 1

    return (trainFits, testFits)


def kruskal(fits1, fits2):
    (h_statistic, p_value) = mstats.kruskalwallis(fits1, fits2)
    print "Kruskal-Wallis non-parametric ANOVA that two samples come from same distribution"
    print "h-statistic =", h_statistic
    print "two-tailed p-value =", p_value


while len(dirs) > 0:
    (condition1, directory1, prefix1) = dirs[0]
    dirs = dirs[1:]

    (trainFits1, testFits1) = getTrainTest(directory1, prefix1)

    for (condition2, directory2, prefix2) in dirs:
        (trainFits2, testFits2) = getTrainTest(directory2, prefix2)

        print "================================================="
        print "Comparing conditions %s and %s" % (condition1, condition2)
        print
        print "For training fitness cases:"
        
        kruskal(trainFits1, trainFits2)
        
        print
        print "----------"
        print
        print "For test fitness cases:"
        
        kruskal(testFits1, testFits2)

        print
        print "================================================="
