import math
import os
import sys
import re
from scipy import stats

# Set these before running:
#dir0 = "Results/GECCO13/mom2/" 
#dir1 = "Results/GECCO13/mom2-lexicase/" 
#dir2 = "Results/GECCO13/mom2-ultra/" 
#dir3 = "Results/GECCO13/mom2-lex-ultra/" 

#dir0 = "Results/GECCO13/mom3/"
#dir1 = "Results/GECCO13/mom3-lexicase/"
#dir2 = "Results/GECCO13/mom3-ultra/"
#dir3 = "Results/GECCO13/mom3-lex-ultra/"

dir0 = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/tourney-subtree/"
dir1 = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/lexicase-subtree/"
dir2 = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/tourney-ultra/"
dir3 = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/lexicase-ultra/"

#dir0 = "Results/GECCO13/pagie-no-erc-normal/"
#dir1 = "Results/GECCO13/BAD-ULTRA/pagie-no-erc-ultra/"
#dir2 = "Results/GECCO13/pagie-no-erc-ultra/"
#dir3 = "Results/GECCO13/pagie-hogeweg-no-erc-45/"

#dir0 = "Results/GECCO13/mux6-normal/"
#dir1 = "Results/GECCO13/mux6-ultra/"

#dir0 = "Results/GECCO13/factorial-normal/"
#dir1 = "Results/GECCO13/factorial-ultra/"
#dir2 = "Results/GECCO13/factorial-ultra-large/"

#dir0 = "Results/GECCO13/factorial-normal-500gens/"
#dir1 = "Results/GECCO13/factorial-ultra-500gens/"

# These are for non-equal-oportunity ULTRA
#dir0 = "Results/lexicase-paper/ultra/factorial-tourn/"
#dir1 = "Results/lexicase-paper/ultra/factorial-lex/"

# These use equal-oportunity ULTRA
#dir0 = "Results/equal-size-ULTRA/factorial/"
#dir1 = "Results/equal-size-ULTRA/factorial-tourney/"

#dir0 = "Results/lexicase-paper/ultra/dm3-lex/"
#dir1 = "Results/lexicase-paper/ultra/dm3-tourney/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

errorType = "float"

# Functions
def my_mean(list_of_nums):
    return float(sum(list_of_nums)) / float(len(list_of_nums))

def standard_deviation(list_of_nums, mean):
    return math.sqrt(sum([(x - mean) * (x - mean) for x in list_of_nums]) / (float(len(list_of_nums) - 1)))


# Main area

def get_best_fitnesses(outputDirectory):
    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    print
    print "Directory of runs =", outputDirectory
    print

    print "Computing Mean Best Fitness..."

    i = 0
    runs = 0
    best_fitnesses = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
        sys.stdout.write('.')
        if i % 50 == 49:
            print
    
        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        best_mean_error = sys.maxint

        for line in f:            
            if line.startswith("Mean:"):
                gen_best_error = -1
                if errorType == "float":
                    gen_best_error = float(line.split()[-1])
                elif errorType == "int" or errorType == "integer":
                    gen_best_error = int(line.split()[-1])
                else:
                    raise Exception("errorType of %s is not recognized" % errorType)

                if gen_best_error < best_mean_error:
                    best_mean_error = gen_best_error

                    
        best_fitnesses.append(best_mean_error)

        i += 1

    return best_fitnesses

def t_tests(outputDirectory1, outputDirectory2):
    best_fitnesses_1 = get_best_fitnesses(outputDirectory1)
    print
    print "------------------------------------------------------------------"
    best_fitnesses_2 = get_best_fitnesses(outputDirectory2)
    
    # Compute MBF and std dev
    mbf1 = my_mean(best_fitnesses_1)
    stdev1 = standard_deviation(best_fitnesses_1, mbf1)
    
    mbf2 = my_mean(best_fitnesses_2)
    stdev2 = standard_deviation(best_fitnesses_2, mbf2)
    
    print
    print "------------------------------------------------------------------"
    print
    print "For directory:", outputDirectory1
    print "Mean best fitness =", mbf1
    print "Std. Dev. =", stdev1
    print
    
    print
    print "For directory:", outputDirectory2
    print "Mean best fitness =", mbf2
    print "Std. Dev. =", stdev2
    print
    
    # Compute t test
    (t_statistic, p_value) = stats.ttest_ind(best_fitnesses_1, best_fitnesses_2)
    
    print "------------------------------------------------------------------"
    print
    print "t-test that above means are different, with two-tailed p-value"
    print "t-statistic =", t_statistic
    print "two-tailed p-value =", p_value
    print "one-tailed p-value =", (p_value / 2.0)
    print
    

# Function calls
#t_tests(dir0, dir1)
#t_tests(dir1, dir2)
#t_tests(dir0, dir2)
#t_tests(dir0, dir4)

t_tests(dir2, dir3)
