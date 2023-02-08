
import os, sys


problems = ["compare-string-lengths",
            "double-letters",
            "replace-space-with-newline",
            "string-lengths-backwards",
            "last-index-of-zero",
            "vector-average",
            "mirror-image",
            "x-word-lines",
            "negative-to-zero",
            "scrabble-score",
            "smallest",
            "syllables"
]

basedir = "/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/no-generational-case-additions/%s/"
#basedir = "/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-50-gens/%s/"

dirs = []

for problem in problems:
    tup = (problem, basedir % problem)
    dirs.append(tup)




# Don't change below here.

outputFilePrefix = "log"
outputFileSuffix = ".txt"

def print_active_cases_long(method, outputDirectory):

    run_num = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)

    while (outputFilePrefix + str(run_num) + outputFileSuffix) in dirList:

        fileName = (outputFilePrefix + str(run_num) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0

        for line in f:


            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1]) 

            if line.startswith("Number of cases this gen"):
                active_cases = int(line.split()[-1])
                print("%s,%i,%i,%i" % (method, run_num, gen, active_cases))

            if line.startswith("SUCCESS"):
                done = "SUCCESS"
                break

            if line.startswith("FAILURE"):
                done = "FAILURE"
                break


        run_num += 1



print("method,trial,generation,active_cases")

for (method, directory) in dirs:
    print(method, file=sys.stderr)
    print_active_cases_long(method, directory)

