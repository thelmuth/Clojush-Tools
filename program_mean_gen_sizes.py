#import math
import os, sys
from sys import maxint

# Set these before running:
#outputDirectory = "Results/kata-gsxover/lexicase/"
#outputDirectory = "Results/ULTRA/lexicase/"
#outputDirectory = "Results/ULTRA/larger-lexicase/

#outputDirectory = "Results/GECCO13/bio-normal/"
#outputDirectory = "Results/GECCO13/bio-ultra/" 

#outputDirectory = "Results/GECCO13/pagie-normal/"
#outputDirectory = "Results/GECCO13/pagie-ultra/"
#outputDirectory = "Results/GECCO13/pagie-no-erc-normal/"
#outputDirectory = "Results/GECCO13/pagie-no-erc-ultra/"
#outputDirectory = "Results/GECCO13/pagie-hogeweg-no-erc-45/"

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

#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/"
#outputDirectory = "Results/GECCO14/wc/padding-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/bushy-max-points-1000/"

outputDirectory = "Results/parent-selection-v3-UMAD/uniform/smallest/"


# This allows this script to take a command line argument for outputDirectory
if len(sys.argv) > 1 and sys.argv[1] != "brief" and sys.argv[1] != "csv":
    outputDirectory = sys.argv[1]


outputFilePrefix = "log"
outputFileSuffix = ".txt"

#outputFilePrefix = "bio-normallog"


# Helper function
def my_mean(list_of_nums):
    if len(list_of_nums) == 0:
        return 0
    return float(sum(list_of_nums)) / float(len(list_of_nums))

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)


#print "Computing best hits per generation..."
max_generations = 0
sizes_per_gen = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    gen = 0
    mean_size = 0

    for line in f:
        if i == 0:
            if line.startswith("max-generations"):
                max_generations = int(line.split()[-1])
                sizes_per_gen = [[] for x in range(max_generations + 1)]

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("Average program size in population"):
            mean_size = float(line.split()[-1])
            sizes_per_gen[gen].append(mean_size)
            
    i += 1



#for i, (gen, size, mean_size)  in enumerate(sizes_per_gen):
#    print "Run: %3i  | Gen: %4i  | Best Prog Size = %4i  | Mean Prog Size = %.1f" % (i, gen, size, mean_size)

for i, mean_sizes_at_gen in enumerate(sizes_per_gen):
    #print len(mean_sizes_at_gen)
    print "Gen: %4i | NumRunsRemaining: %4i | MeanOfMeanProgSize: %.1f" % (i, len(mean_sizes_at_gen), my_mean(mean_sizes_at_gen))
