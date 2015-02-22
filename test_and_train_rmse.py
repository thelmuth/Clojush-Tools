#import math
import os
#import sys

# Set these before running:

#outputDirectory = "Results/GECCO13/bio-normal/"
#outputDirectory = "Results/GECCO13/bio-ultra/"
#outputDirectory = "Results/GECCO13/bio-normal-env/"
#outputDirectory = "Results/GECCO13/bio-45/"

#outputDirectory = "Results/lexicase-paper/ultra/bio-lex/"

#outputDirectory = "Results/gecco13/equal-size-ULTRA/bio/"

#outputDirectory = "Results/GECCO14/order-lexicase/bio-88/"

#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-subtree-81-9/"
#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-subtree-45-45/"
#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-tourney/"

#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-lexicase/"
#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-88/"
#outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-78/"
outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-ol-72/"
outputDirectory = "Results/GECCO14/order-lexicase/rmse-bio-ol-61/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

errorType = "float"


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

for i, (gen, train, test, done)  in enumerate(bestFitnessesOfRuns):
    print "Run %s: At generation %s" % (i, gen)
    print "These are best of run - not necessarily from last generation:"
    print "  Train RMSE = %s" % train
    print "  Test RMSE  = %s\n" % test

totalTrainRMSE = 0
totalTestRMSE = 0
inds = 0
testRMSEs = []
trainRMSEs = []
for (gen, train, test, done) in bestFitnessesOfRuns:
    if done:
        totalTrainRMSE += train
        trainRMSEs.append(train)
        totalTestRMSE += test
        testRMSEs.append(test)
        inds += 1

if inds > 0:
    print "-----"
    print "Mean of best train RMSE across %i runs: %.5f" % (inds, totalTrainRMSE / float(inds))
    print "Mean of best test RMSE across %i runs: %.5f" % (inds, totalTestRMSE / float(inds))


#testRMSEs.sort()
#for test in testRMSEs:
#    print "-- %.2f" % test

#trainRMSEs.sort()
#for train in trainRMSEs:
#    print "-- %.2f" % train

def median(lst):
    sorts = sorted(lst)
    length = len(lst)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

print
print "---------"
print
print "Median of train = %.2f" % (median(trainRMSEs))
print "Median of test = %.2f" % (median(testRMSEs))
