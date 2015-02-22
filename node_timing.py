#!/usr/bin/python
import os
import re
import sys
from math import sqrt
from sys import maxint

# Set these before running:

#outputDirectory = "Results/lexicase-paper/subtree-GOs/dm3-lexicase/"
#outputDirectory = "Results/lexicase-paper/subtree-GOs/dm3-tourney/"

#outputDirectory = "Results/timing/ultra/dm3-lexicase/"
#outputDirectory = "Results/timing/ultra/dm3-tourney/"

#outputDirectory = "Results/lexicase-paper/ael/factorial-ael/"
#outputDirectory = "Results/lexicase-paper/ael/factorial-new-rand/"

#outputDirectory = "Results/thesis/change-exploratory/"
#outputDirectory = "Results/thesis/change-exploratory-2/"
#outputDirectory = "Results/thesis/change-exploratory-intextra/"
#outputDirectory = "Results/thesis/change-exploratory-minimal/"

outputDirectory = "Results/lexicase-paper/ultra/dm4-lex/" 

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

nodeList = []
if len(sys.argv) >= 2:
    nodeFile = open(sys.argv[1])
    nodeList = [line.strip() for line in nodeFile.readlines()]
    nodeFile.close()


nodeGroupDict = {}
nodeGroupDict["z"] = "ignore"

# rack 1
for x in range(1,19):
    s = "1-" + str(x)
    nodeGroupDict[s] = "rack" + s
for x in [2,3,4,5,8,10,11,13,14,15,16]:
    nodeGroupDict["1-" + str(x)] = "rack1-large" #"rack1-2,3,4,5,8,10,11,13,14,15,16"
nodeGroupDict["1-1"] = "rack1-1,12"
nodeGroupDict["1-12"] = "rack1-1,12"

# rack 2
for x in range(1,22):
    nodeGroupDict["2-" + str(x)] = "rack2"
nodeGroupDict["2-13"] = "rack2-13,14,15"
nodeGroupDict["2-14"] = "rack2-13,14,15"
nodeGroupDict["2-15"] = "rack2-13,14,15"

# rack 4
nodeGroupDict["4-1"] = "rack4-1"
nodeGroupDict["4-2"] = "rack4-2,3,4"
nodeGroupDict["4-3"] = "rack4-2,3,4"
nodeGroupDict["4-4"] = "rack4-2,3,4"

timeAndGenList = [] #Has tuples of (gen, totalTime, done)

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    totalTime = 0
    done = False
    totalTimeNotPrinted = True

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Total Time:"):
            totalTimeNotPrinted = False
            regexp = re.compile(r'Total Time:\s*(\d+\.\d) seconds')
            match = re.search(regexp, line)
            totalTime = float(match.group(1))

        if line.startswith("Reproduction:") and totalTimeNotPrinted:
            regexp = re.compile(r'Reproduction:\s*(\d+\.\d) seconds,\s*(\d+\.\d)%')
            match = re.search(regexp, line)
            (reproTime, reproPercent) = match.groups()

            totalTime = (float(reproTime) * 100.0) / float(reproPercent)


    timeAndGenList.append((gen, totalTime, done))
            
    i += 1


nodeGroupTimes = {}
for group in nodeGroupDict.values():
    nodeGroupTimes[group] = []

nodeTimesDict = {}

#print
#print "Best fitnesses of runs:"
for i, (gen, time, done) in enumerate(timeAndGenList):
    if gen > 0:
        print "Run: %3i  | Gen: %5i  | Time (sec) = %8.i | Time/Gen = %8.1f" % (i, gen, int(time), (time/gen))
    
        if len(nodeList) > i:
            node = nodeList[i]
            times = nodeTimesDict.get(node, [])
            times.append(time/gen)
            nodeTimesDict[node] = times
            
            nodeGroupTimes[nodeGroupDict[node]].append(time/gen)

def sample_std_dev(nums):
    if len(nums) <= 1:
        return -1
    mean = float(sum(nums)) / len(nums)
    return sqrt(sum([(x - mean)**2 for x in nums]) / (len(nums) - 1))

print
print "---------------------------------------------------------------------"
print "------ Nodes ------"
print

for node in sorted(nodeTimesDict.keys()):
    times = nodeTimesDict[node]
    if len(times) > 0 and node != "z":
        meanTimes = float(sum(times)) / len(times)
        print "compute-%-4s  | Runs: %3i  | Mean Time/Gen = %8.1f  | StdDev = %8.1f" % (node, len(times), meanTimes, sample_std_dev(times))


print
print "---------------------------------------------------------------------"
print "------ Node groups ------"
print

for nodeGroup in sorted(nodeGroupTimes.keys()):
    times = nodeGroupTimes[nodeGroup]
    if len(times) > 0 and nodeGroup != "ignore":
        meanTimes = float(sum(times)) / len(times)
        print "%-14s  | Runs: %3i  | Mean Time/Gen = %8.1f  | StdDev = %8.1f" % (nodeGroup, len(times), meanTimes, sample_std_dev(times))



