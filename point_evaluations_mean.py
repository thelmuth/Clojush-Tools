
#!/usr/bin/python
import os
from sys import maxint

# Set these before running:

print_csv = True
print_csv_failures = False

### EHC
# 2) Normal EHC - max evals 3e10, silence mut on, hill climbing on
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-EHC/EHC-testing/ifs-7/"

# 3) max evals 3e10, silence mut on, hill climbing off
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/lexicase/"
outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/EHC-testing/ifs-7/"

# 4) max gens 300, silence mut on, hill climbing off
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline-epiline-without-hill-climbing/max-gens-300-silence-mut-on/ifs-7/"

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



outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

if not print_csv:
    print
    print "           Directory of results:"

print outputDirectory

if not print_csv:
    print

pointEvaluationsOfRuns = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    point_evals = 0
    done = False

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            #break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Number of point (instruction) evaluations so far:") and not done:
            point_evals = int(line.split()[-1])

    pointEvaluationsOfRuns.append((gen, point_evals, done))
            
    i += 1


#### Printing

if print_csv:
    print "run\tresult\tgeneration\tsuccesses_using_at_most_this_many_generations\tpoint_evaluations\tsuccesses_using_at_most_this_many_point_evaluations"

for i, (gen, point_evals, done) in enumerate(pointEvaluationsOfRuns):
    if print_csv:

        suc_gens = 0
        suc_pe = 0

        if done == "SUCCESS":
            for (other_gen, other_pe, other_done) in pointEvaluationsOfRuns:
                if other_done == "SUCCESS" and other_gen <= gen:
                    suc_gens += 1

                if other_done == "SUCCESS" and other_pe <= point_evals:
                    suc_pe += 1

        if print_csv_failures or done == "SUCCESS":
            print "%i\t%s\t%i\t%i\t%i\t%i" % (i, done, gen, suc_gens, point_evals, suc_pe)

    else:
        doneSym = ""
        if not done:
            doneSym = " -- not done"
        print "Run: %3i  | Gen: %5i  | Point Evals = %12d%s" % (i, gen, point_evals, doneSym)


if not print_csv:

    totalPoint_Evals = 0
    total_point_evals_of_failed_runs = 0
    finished = 0
    failed = 0

    for i, (gen, point_evals, done) in enumerate(pointEvaluationsOfRuns):
        if done:
            finished += 1
            totalPoint_Evals += point_evals

            if done == "FAILURE":
                total_point_evals_of_failed_runs += point_evals
                failed += 1

    print "--------------------"
    print "Number of finished runs:                   %13i" % finished
    print "Total Point Evals of Finished Runs:        %13i" % totalPoint_Evals
    if finished > 0:
        print "Mean Point Evals Per Run of Finished Runs: %13.3e" % (totalPoint_Evals / float(finished))

    print "-----"
    print "Number of failed runs:                     %13i" % failed
    print "Total Point Evals of Failed Runs:          %13i" % total_point_evals_of_failed_runs
    if failed > 0:
        print "Mean Point Evals Per Run of Failed Runs:   %13.3e" % (total_point_evals_of_failed_runs / float(failed))

    print "-----"
