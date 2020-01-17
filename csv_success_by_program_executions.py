#!/usr/bin/python

"""
For each success, records the program executions along with the number of train, test, and simp_test solutions at that point.
"""

import os, sys
from sys import maxint

# Set these before running:
problem = "double-letters"
error_threshold = 0

max_executions = 30000000

normal_training_cases_size = int(max_executions / (1000 * 300))
print "Normal training cases size =", normal_training_cases_size

# Dirs for downsampled lexicase
# dirs = [("lexicase", normal_training_cases_size, "/home/thelmuth/Results/parent-selection-v3-UMAD/lexicase/%s" % problem),
#         ("downsample-25", int(normal_training_cases_size * 0.25), "/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.25/%s" % problem),
#         ("downsample-10", int(normal_training_cases_size * 0.1), "/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.1/%s" % problem)
# ]

dirs = [#("lexicase", normal_training_cases_size, "/home/thelmuth/Results/parent-selection-v3-UMAD/lexicase/%s" % problem),
        ("CDGP", False, "/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/no-generational-case-additions/%s" % problem),
        ("CDGP50", False, "/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-50-gens/%s" % problem)
]


for (prob, rate, direct) in dirs:
    print prob, " - ", direct


outputFilePrefix = "log"
outputFileSuffix = ".txt"


def getSuccessProgExecs(outputDirectory, cases_size):
    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    train_success_progexecs = []
    test_success_progexecs = []
    simplified_test_success_progexecs = []
    
    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        prog_execs = -1
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

            if line.startswith("Number of program evaluations used so far:") and prog_execs == -1:
                prog_execs = int(line.split()[-1]) * cases_size

            if line.startswith("Number of program executions (running on a single case counts as 1 execution):") and prog_execs == -1:
                prog_execs = int(line.split()[-1])

            if prog_execs >= 0 and trainSuccess != -1 and testSuccess != -1 and simpTestSuccess != -1:
                break

        if trainSuccess == True: # Might be -1, which would need to be False here
            train_success_progexecs.append(prog_execs)
        if testSuccess == True: # Might be -1, which would need to be False here
            test_success_progexecs.append(prog_execs)
        if simpTestSuccess == True: # Might be -1, which would need to be False here
            simplified_test_success_progexecs.append(prog_execs)

        i += 1


    return (train_success_progexecs, test_success_progexecs, simplified_test_success_progexecs)

def numbers_leq_x(nums, x):
    """Returns the count of the number of numbers <= x in list nums"""
    return len(filter(lambda a: a <= x, nums))

#### Printing

print "method,program_executions,train,test,simp"

for (prob, cases_size, directory) in dirs:
    (train_success_progexecs, test_success_progexecs, simplified_test_success_progexecs) = getSuccessProgExecs(directory, cases_size)

    train_success_progexecs.sort()
    test_success_progexecs.sort()
    simplified_test_success_progexecs.sort()

    print "%s,0,0,0,0" % prob
    
    for prog_execs in train_success_progexecs:
        train = numbers_leq_x(train_success_progexecs, prog_execs)
        test =  numbers_leq_x(test_success_progexecs, prog_execs)
        simp =  numbers_leq_x(simplified_test_success_progexecs, prog_execs)

        print "%s,%i,%i,%i,%i" % (prob, prog_execs, train, test, simp)

    print "%s,%i,%i,%i,%i" % (prob, max_executions, train, test, simp)


"""
    print
    print prob
    print "Train:", train_success_progexecs
    print "Test:", test_success_progexecs
    print "TestSimp:", simplified_test_success_progexecs
"""
"""
    for prog_execs in range(0, max_gens + 1):
        train_this_prog_execs = numbers_leq_x(train_success_progexecs, prog_execs)
        test_this_prog_execs =  numbers_leq_x(test_success_progexecs, prog_execs)
        simp_this_prog_execs =  numbers_leq_x(simplified_test_success_progexecs, prog_execs)
        
        print "%s,%i,%i,%i,%i" % (prob, prog_execs, train_this_prog_execs, test_this_prog_execs, simp_this_prog_execs)
"""
