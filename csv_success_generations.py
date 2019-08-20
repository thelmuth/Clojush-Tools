
#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

error_threshold = 0
max_gens = 1000

# Novelty Lexicase

#main_dir = "/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/"
main_dir = "/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/"

probs = ["compare-string-lengths",
         "double-letters",
         "replace-space-with-newline",
         "last-index-of-zero",
         "vector-average",
         "mirror-image",
         "x-word-lines",
         "negative-to-zero",
         "scrabble-score",
         #pig-latin",
         "syllables"]

dirs = [(prob, main_dir + prob) for prob in probs]


outputFilePrefix = "log"
outputFileSuffix = ".txt"


def getSuccessGens(outputDirectory):
    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    train_success_generations = []
    test_success_generations = []
    simplified_test_success_generations = []
    
    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = -1
        trainSuccess = -1
        testSuccess = -1
        simpTestSuccess = -1

        for line in reversed(f.readlines()):

            if line.startswith("Test total error for best:") and simpTestSuccess == -1:
                try:
                    simpBestTest = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    simpBestTest = float(line.split()[-1].strip("Nn"))
                if simpBestTest <= error_threshold:
                    simpTestSuccess = True
                else:
                    simpTestSuccess = False

            if line.startswith("Test total error for best:") and simpTestSuccess != -1:
                try:
                    bestTest = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    bestTest = float(line.split()[-1].strip("Nn"))
                if bestTest <= error_threshold:
                    testSuccess = True
                else:
                    testSuccess = False

            if line.startswith("SUCCESS"):
                trainSuccess = True
            if line.startswith("FAILURE"):
                trainSuccess = False
                testSuccess = False
                simpTestSuccess = False

            if line.startswith(";; -*- Report") and gen == -1:
                gen = int(line.split()[-1])


            if gen >= 0 and trainSuccess != -1 and testSuccess != -1 and simpTestSuccess != -1:
                break

        if trainSuccess == True: # Might be -1, which would need to be False here
            train_success_generations.append(gen)
        if testSuccess == True: # Might be -1, which would need to be False here
            test_success_generations.append(gen)
        if simpTestSuccess == True: # Might be -1, which would need to be False here
            simplified_test_success_generations.append(gen)

        i += 1


    return (train_success_generations, test_success_generations, simplified_test_success_generations)

def numbers_leq_x(nums, x):
    """Returns the count of the number of numbers <= x in list nums"""
    return len(filter(lambda a: a <= x, nums))

#### Printing

#tab_sep_titles = str([n for (n,d) in dirs]).replace(" ","").replace("]","").replace("[","").replace("'","").replace(",","\t")
#print "run\tresult\tgeneration\t" + tab_sep_titles + "\tpoint-evaluations\t" + tab_sep_titles

print "problem,generation,number_of_train_successes,number_of_test_successes,number_of_simplified_test_successes"

#raise Exception("asdasd")

for (prob, directory) in dirs:
    (train_success_generations, test_success_generations, simplified_test_success_generations) = getSuccessGens(directory)

    for gen in range(0, max_gens + 1):
        train_this_gen = numbers_leq_x(train_success_generations, gen)
        test_this_gen =  numbers_leq_x(test_success_generations, gen)
        simp_this_gen =  numbers_leq_x(simplified_test_success_generations, gen)
        
        print "%s,%i,%i,%i,%i" % (prob, gen, train_this_gen, test_this_gen, simp_this_gen)

