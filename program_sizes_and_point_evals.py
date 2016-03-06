#import math
import os
from sys import maxint

# Set these before running:

#outputDirectory = "Results/bench-prog-synth/median/lexicase/"
#outputDirectory = "Results/bench-prog-synth/median/init-max-size-20/lexicase/"

#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/"

### EHC
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/lexicase/standard/"

### Baseline for benchmarks
#outputDirectory = "Results/clustering-bench/number-io/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/mirror-image/baseline-uniform/logs/"


outputDirectory = "Results/clustering-bench/vector-average/lexicase/logs/"




outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)


#print "Computing best hits per generation..."

sizes = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    size = 0
    mean_size = 0
    point_evals = 0

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("Size:"):
            size = int(line.split()[-1])

        if line.startswith("Number of point (instruction) evaluations so far"):
            point_evals = int(line.split()[-1])

        if line.startswith("Average program size in population"):
            mean_size = float(line.split()[-1])

    sizes.append((gen, size, mean_size, point_evals))
            
    i += 1


bestSumSize = 0
popSumSize = 0

for i, (gen, size, mean_size, point_evals)  in enumerate(sizes):
    extra = ""
    if gen > 5000 and mean_size < 2.0:
        extra = " -- DEGEN"
    print "Run: %3i  | Gen: %5i  | Best Prog Size = %4i  | Mean Prog Size = %5.1f | Point Evals = %11i %s" % (i, gen, size, mean_size, point_evals, extra)
    bestSumSize += size
    popSumSize += mean_size

print "-----"
print "Mean of Best Sizes:\t\t%.1f" % (float(bestSumSize) / len(sizes))
print "Mean of Population Mean Sizes:\t%.1f" % (float(popSumSize) / len(sizes))

