import math
import os
import sys

# Set these before running:

#outputDirectory = "Results/GECCO14/simplification/dm3-simplified/"
#outputDirectory = "Results/GECCO14/simplification/odd-simplified/"
#outputDirectory = "Results/GECCO14/simplification/pagie-simplified/"
outputDirectory = "Results/GECCO14/simplification/wc-simplified/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Don't have to change anything below!

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

starting_sizes = []
simplified_sizes = []

i = 0
while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    program_num = 0

    for line in f:

        if i == 0:
            if line.startswith("initial size: "):
                start_size = int(line.split()[-1])
                starting_sizes.append(start_size)
            
                simplified_sizes.append([])

        if line.startswith("program number:"):
            program_num = int(line.split()[-1])

        if line.startswith("sizes after 10000 simplifications:"):
            simp_sizes = [int(x) for x in line[len("sizes after 10000 simplifications: ("):-2].split()]
            simplified_sizes[program_num].extend(simp_sizes)

    i += 1


for i, simp in enumerate(simplified_sizes):
    sys.stdout.write("%d," % starting_sizes[i])
    for j, s in enumerate(simp):
        sys.stdout.write(str(s))
        if j+1 != len(simp):
            sys.stdout.write(",")
    print
