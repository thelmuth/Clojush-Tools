#!/usr/bin/python
import os, ast
from sys import maxint, argv

# Set these before running:

percents = [10, 5, 1]

#######################################################################################
############################### Lexicase Tournament Experiments #######################
#######################################################################################

#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/replace-space-with-newline/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/replace-space-with-newline/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/syllables/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/syllables/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/string-lengths-backwards/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/string-lengths-backwards/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/negative-to-zero/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/negative-to-zero/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/x-word-lines/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/x-word-lines/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/count-odds/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/count-odds/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/mirror-image/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/mirror-image/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/double-letters/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/double-letters/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/vector-average/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/vector-average/logs/"

#######################################################################################
############################### Hyper Selection #######################
#######################################################################################

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/double-letters/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/double-letters/tourney-7/logs/"

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/mirror-image/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/mirror-image/tourney-7/logs/"

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/count-odds/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/count-odds/tourney-7/logs/"

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/x-word-lines/lexicase/logs/"
#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/x-word-lines/tourney-7/logs/"

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/vector-average/lexicase/logs/"
#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/vector-average/tourney-7/logs/"

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/string-lengths-backwards/tourney-7/logs/"






if len(argv) > 1:
    outputDirectory = argv[1]


outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

print
print outputDirectory
print

success_total_gens = 0
failure_total_gens = 0
successes = 0
failures = 0
success_percent_selections_dict = {}
failure_percent_selections_dict = {}
for p in percents:
    success_percent_selections_dict[p] = 0
    failure_percent_selections_dict[p] = 0

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:    
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    print "run =", i, ", total gens =", (success_total_gens + failure_total_gens)

    gen = 0
    done = False

    file_total_gens = 0
    file_percent_selections_dict = {}
    for p in percents:
        file_percent_selections_dict[p] = 0

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            successes += 1
            # Since succeeded, add this run's percent selections to the succeed version
            success_total_gens += file_total_gens
            for p in percents:
                success_percent_selections_dict[p] += file_percent_selections_dict[p]

            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            failures += 1
            # Since failed, add this run's percent selections to the fail version
            failure_total_gens += file_total_gens
            for p in percents:
                failure_percent_selections_dict[p] += file_percent_selections_dict[p]

            break

        if line.startswith("Selection counts: "):
            selection_counts_str = line[len("Selection counts: "):].strip().replace("(", "[").replace(")", "]").replace(" ", ", ")
            selection_counts = ast.literal_eval(selection_counts_str)

            total_selections = sum(selection_counts)
            if total_selections > 0:
                file_total_gens += 1
                for p in percents:
                    big_selection_counts = filter(lambda x: (x / float(total_selections)) > (p / 100.0), selection_counts)

                    file_percent_selections_dict[p] += len(big_selection_counts)
            
    i += 1


print
print "Success dict:", success_percent_selections_dict
print "Failure dict:", failure_percent_selections_dict
print

print "For %i successful runs:" % successes
for p in percents:
    print "Number of individuals per generation with more than %2d%% of selections: %2.4f" % (p, (success_percent_selections_dict[p]/float(success_total_gens)))

print
print "For %i failed runs:" % failures
for p in percents:
    print "Number of individuals per generation with more than %2d%% of selections: %2.4f" % (p, (failure_percent_selections_dict[p]/float(failure_total_gens)))

print
print "For all %i runs:" % (failures + successes)
for p in percents:
    print "Number of individuals per generation with more than %2d%% of selections: %2.4f" % (p, ((failure_percent_selections_dict[p] + success_percent_selections_dict[p])/float(failure_total_gens + success_total_gens)))

