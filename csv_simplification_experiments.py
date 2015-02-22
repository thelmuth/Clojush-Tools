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

start_and_simp = [(starting_sizes[i], simplified_sizes[i]) for i in range(len(starting_sizes))]

start_and_simp.sort(key=lambda tup: float(sum(tup[1]))/len(tup[1]))
start_and_simp.sort(key=lambda tup: tup[0])

print "Program,Type,Size"
for i, (start, simp) in enumerate(start_and_simp):
    print "%d,Start,%d" % (i, start)
    for s in simp:
        print "%d,Simplified,%d" % (i, s)

#    print "%d,Max,%d" % (i, max(simp))
#    print "%d,Min,%d" % (i, min(simp))
