import math
import os
import sys

# Set these before running:
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

#outputDirectory = "Results/gecco13/big-mom3/mom3-lex-ultra/"

#outputDirectory = "Results/gecco13/mux6-normal/"
#outputDirectory = "Results/gecco13/mux6-ultra/"

#outputDirectory = "Results/gecco13/factorial-normal/"
#outputDirectory = "Results/gecco13/factorial-ultra/"
#outputDirectory = "Results/gecco13/factorial-ultra-large/"
#outputDirectory = "Results/gecco13/factorial-normal-500gens/"
#outputDirectory = "Results/gecco13/factorial-ultra-500gens/"

#outputDirectory = "Results/gecco13/pagie-no-erc-normal/"
#outputDirectory = "Results/gecco13/pagie-hogeweg-no-erc-45/"

#outputDirectory = "Results/gecco13/equal-size-ULTRA/bio/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/pagie-no-erc/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/factorial/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/factorial-tourney/"
#outputDirectory = "Results/gecco13/equal-size-ULTRA/mux6/"
#outputDirectory = "Results/lexicase-paper/ultra/factorial-EGL/"

#Note: Following group did not use equal size ULTRA; they may not work if moved
#outputDirectory = "Results/lexicase-paper/ultra/NON-EQUAL-SIZE/factorial-lex/"
#outputDirectory = "Results/lexicase-paper/subtree-GOs/factorial-lex/"

#outputDirectory = "Results/lexicase-paper/ultra/dm3-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/dm3-tourney/"

#outputDirectory = "Results/lexicase-paper/ael/factorial-ael/"
#outputDirectory = "Results/lexicase-paper/ael/factorial-new-rand/"

#outputDirectory = "Results/ultra/DOT-normal/"
#outputDirectory = "Results/ultra/DOT-no-paren-ULTRA/"

#outputDirectory = "Results/GECCO14/order-lexicase/pagie-946/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-895/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-80/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-64/"
#outputDirectory = "Results/GECCO14/order-lexicase/pagie-464/"

#outputDirectory = "Results/gecco13/DM/mom2-lex-ultra"
#outputDirectory = "Results/plush-testing/dm2-ultra-lex/"

#outputDirectory = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/tourney-subtree/"
#outputDirectory = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/lexicase-subtree/"
#outputDirectory = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/tourney-ultra/"
outputDirectory = "Results/gecco13/redo-with-fixed-evalpush-limit/dm2/lexicase-ultra/"



outputFilePrefix = "log"
outputFileSuffix = ".txt"

z = 0.99

# Don't have to change anything below!
really_huge_number = sys.maxint

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

# M = population size
# G = maximum generations in a run
# z = desired probability of finding a solution
def computational_effort(success_generations, runs, M, G, z):
    min_effort = really_huge_number
    prev_i_effort = really_huge_number
    for i in range(G):
        effort = number_individuals_evaluated(success_generations,
                                              runs, M, i, z)
        min_effort = min(min_effort, effort)

        # Print all efforts
        #print "effort(", i, ") = " + str(effort)

        # Print only improvement efforts
        #if(effort < prev_i_effort):
        if i in success_generations:
            print "effort(%4i) = %12i" % (i, effort)

        # Set prev_i_effort
        prev_i_effort = effort

    return min_effort

def number_individuals_evaluated(success_generations, runs, M, i, z):
    return (M * (i + 1) *
            number_of_required_independent_runs(success_generations,
                                                runs, i, z))
        
def number_of_required_independent_runs(success_generations, runs, i, z):
    cumulative_probability = cumulative_probability_of_success(success_generations, runs, i)
    if cumulative_probability == 0.0:
        return really_huge_number
    if cumulative_probability >= 1.0:
        return int(math.ceil(math.log(1.0 - z) / math.log(1.0 / really_huge_number)))
    return int(math.ceil(math.log(1.0 - z) / math.log(1.0 - cumulative_probability)))

def cumulative_probability_of_success(success_generations, runs, i):
    total_prob = 0.0
    for j in range(i + 1):
        total_prob += probability_of_success(success_generations, runs, j)
    return total_prob

def probability_of_success(success_generations, runs, i):
    return float(success_generations.count(i)) / float(runs)


#print "TEST ", computational_effort([10, 11, 12, 13, 14, 20, 30], 10, 1000, 51, 0.99)

# Main area

print
print "Directory of runs =", outputDirectory
print

print "Computing Computational Effort..."

population_size = sys.maxint
max_generations = sys.maxint

i = 0
runs = 0
success_generations = []
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    sys.stdout.write('.')
    if i % 50 == 49:
        print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    lastGeneration = -1

    for line in f:
        if i == 0:
            if line.startswith("population-size"):
                population_size = int(line.split()[-1])

            if line.startswith("max-generations"):
                max_generations = int(line.split()[-1])

        if line.startswith(";; -*- Report"):
            lastGeneration = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            success_generations.append(lastGeneration)
            # Prints out when a success is found
            #print "Success in run", i, "in generation", lastGeneration
            break

    i += 1

print
print "Success generation counts:"
if len(success_generations) == 0:
    print "    No Successful Generations"
else:
    for i in range(0, max_generations):
        # For generation with labels:
        #print "    Runs succeeding in gen", i, "=", success_generations.count(i)

        # For only successful generations
        if success_generations.count(i) > 0:
            print "    Runs succeeding in gen %4i = %2i" % (i, success_generations.count(i))

        # For csv file output
        #print success_generations.count(i)


print
computational_effort = computational_effort(success_generations, runs, population_size, max_generations, z)

print
print "Population size = %i" % population_size
print "Max generations = %i" % max_generations

print
print "Computational Effort =", computational_effort


print "Number of successful runs =", len(success_generations)
print

