#import math
import os
from sys import maxint

# Set these before running:
outputDirectory = "Results/plush-testing/factorial-ultra-delta-size/"


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

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("Average change in program size after a genetic operator"):
            size = float(line.split()[-1])

    sizes.append((gen, size))
            
    i += 1


changeSumSize = 0

for i, (gen, size)  in enumerate(sizes):
    print "Run: %3i  | Gen: %4i  | Mean Change Prog Size = %.3f" % (i, gen, size)
    changeSumSize += size

print "-----"
print "Mean of Mean Change in Prog  Sizes:\t%.3f" % (float(changeSumSize) / len(sizes))
