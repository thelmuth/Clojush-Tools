
#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_csv_failures = False
error_threshold = 0

### EHC
# 2) Normal EHC - max evals 3e10, silence mut on, hill climbing on
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/ifs-7/"

# 3) max evals 3e10, silence mut on, hill climbing off
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/ifs-7/"

# 4) max gens 300, silence mut on, hill climbing off
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/ifs-7/"

# dirs = [("4-max-gens-300-silence-mut-on-lexicase", "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/lexicase/"),
#         ("4-max-gens-300-silence-mut-on-tourney", "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/tourney-7/"),
#         ("4-max-gens-300-silence-mut-on-ifs", "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/ifs-7/")
#         ]

# 5) max evals 3e10, silence mut off, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/\
# "
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/ifs-7/"

# 6) max gens 300, silence mut off, hill climbing off, init max prog size 200
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/init-size-200/ifs-7/"

# X) these are to see how many point evaluations are used in a typical GP run of this problem
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/ifs-7/"

# *) Comparison of tournament selection runs limited by 3e10 point evaluations
#dirs = [("5-max-evals-3e10-silence-mut-off-tourney-7", "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/"),
#        ("3-max-evals-3e10-silence-mut-on-tourney-7", "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/tourney-7/"),
#        ("2-max-evals-3e10-silence-hill-climbing-tourney-7", "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/")
#        ]

# Autoconstruction

dirs = [("standard", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
        ("autoconstruction", "zzResults/autoconstruction/replace-space-with-newline/trial1/")]



outputFilePrefix = "log"
outputFileSuffix = ".txt"


def getGenAndPointEvals(outputDirectory):
    # Main area
    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)
    
    pointEvaluationsOfRuns = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

        runs = i + 1 # After this loop ends, runs should be correct
        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = -1
        point_evals = -1
        bestTest = -1
        done = False

        for line in reversed(f.readlines()):

            if done and gen >= 0 and point_evals >= 0 and bestTest >= 0:
                break

            if line.startswith(";; -*- Report") and gen == -1:
                gen = int(line.split()[-1])

            if line.startswith("SUCCESS") and not done:
                done = "SUCCESS"

            if line.startswith("FAILURE") and not done:
                done = "FAILURE"

            if line.startswith("Number of point (instruction) evaluations so far:") and done and point_evals == -1:
                point_evals = int(line.split()[-1])

            if line.startswith("Test total error for best:") and done and bestTest == -1:
                try:
                    bestTest = int(line.split()[-1].strip("Nn"))
                except ValueError, e:
                    bestTest = float(line.split()[-1].strip("Nn"))

        if bestTest <= error_threshold and done == "SUCCESS":
            done = "GENERALIZED_SUCCESS"

        pointEvaluationsOfRuns.append((gen, point_evals, done))

        i += 1

    return pointEvaluationsOfRuns


#### Printing

tab_sep_titles = str([n for (n,d) in dirs]).replace(" ","").replace("]","").replace("[","").replace("'","").replace(",","\t")
print "run\tresult\tgeneration\t" + tab_sep_titles + "\tpoint-evaluations\t" + tab_sep_titles

#print "1\tSUCCESS\t45\t\t\t3\t4314314\t\t\t3"

#raise Exception("asdasd")

for dir_num in range(len(dirs)):
    this_directory = dirs[dir_num][1]

    pointEvaluationsOfRuns = getGenAndPointEvals(this_directory)

    pre_tabs = "\t" * (dir_num + 1)
    post_tabs = "\t" * (len(dirs) - dir_num)

    for i, (gen, point_evals, done) in enumerate(pointEvaluationsOfRuns):

        suc_gens = 0
        suc_pe = 0

        if done == "GENERALIZED_SUCCESS":
            for (other_gen, other_pe, other_done) in pointEvaluationsOfRuns:
                if other_done == "GENERALIZED_SUCCESS" and other_gen <= gen:
                    suc_gens += 1

                if other_done == "GENERALIZED_SUCCESS" and other_pe <= point_evals:
                    suc_pe += 1

        if print_csv_failures or done == "GENERALIZED_SUCCESS":
            print "%i\t%s\t%i%s%i%s%i%s%i%s" % (i, done, gen, pre_tabs, suc_gens, post_tabs, point_evals, pre_tabs, suc_pe, post_tabs)
