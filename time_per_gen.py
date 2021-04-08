#!/usr/bin/python
import os
import time
from sys import maxint

# Set these before running:

verbose = True

#outputDirectory = "Results/GECCO14/wc/padding-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/bushy-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/"
#outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000/"
#outputDirectory = "Results/GECCO14/wc/ultra-params-05-05-10/"
#outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-100/"
#outputDirectory = "Results/GECCO14/wc/ultra-params-01-01-0/"
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-two/"
#outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000-two/"


############ For lexicase paper resub
#outputDirectory = "Results/lexicase-paper/resub/dm3/lex-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/dm3/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/ultra/dm3-lex/"
#outputDirectory = "Results/lexicase-paper/ultra/dm3-tourney/" 

#outputDirectory = "Results/lexicase-paper/resub/factorial/lex-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-1/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-e-plus-2-target/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/normalized-e-over-target-plus-output/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-1/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-e-plus-2-target/tourney8-ultra/"

#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney2-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney4-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney6-ultra/"
#outputDirectory = "Results/lexicase-paper/resub/factorial/ifs-e-over-target-plus-output/tourney8-ultra/"

#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-RETRY/" #lex 1st half
#outputDirectory = "Results/GECCO14/wc/empties-max-points-1000-two/" #lex 2nd half
#outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000/" #tourney7 1st half
#outputDirectory = "Results/GECCO14/wc/tourney-max-points-1000-two/" #tourney7 2nd half
#outputDirectory = "Results/lexicase-paper/resub/wc/tourney3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/tourney5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/ifs-size-7/"

#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/lex/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/tourney3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/tourney5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/tourney7/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-3/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-5/"
#outputDirectory = "Results/lexicase-paper/resub/wc/diversity-figures/ifs-size-7/"


outputDirectory = "Results/2021-benchmark-problem-development/final-run/dice-game/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"

# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

start_end_numGens = []

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    #sys.stdout.write('.')
    #if i % 50 == 49:
    #    print
    
    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
    f = open(outputDirectory + fileName)

    gen = 0
    prev_gen_time = 0
    current_time = 0
    start_time = 0
    done = False

    for line in f:

        if line.startswith(";; -*- Report"):
            gen = int(line.split()[-1])

        if line.startswith("SUCCESS"):
            done = "SUCCESS"
            break

        if line.startswith("FAILURE"):
            done = "FAILURE"
            break

        if line.startswith("Current time:"):
            prev_gen_time = current_time
            try:
                current_time = int(line.split()[-1])
            except:
                current_time = int(line.split()[-2])
            if gen == 0:
                start_time = current_time

    start_end_numGens.append((start_time, current_time, gen, prev_gen_time, done))
            
    i += 1


#print
#print "Best fitnesses of runs:"
for i, (start_time, end_time, gen, prev_gen_time, done) in enumerate(start_end_numGens):
    time_ms = end_time - start_time
    time_min = time_ms / (60.0 * 1000)
    time_per_gen_sec = time_ms / (1000.0 * gen)
    if verbose:
        time_for_last_gen = (end_time - prev_gen_time) / 1000.0
        time_since_last_gen = time.time() - (end_time / 1000.0)
        if done:
            print "Run: %3i  | Gen: %5i  | Total = %7.1f min | Per gen = %6.1f sec | Last gen = %6.1f sec | %s" % (i, gen, time_min, time_per_gen_sec, time_for_last_gen, done)
        else:
            print "Run: %3i  | Gen: %5i  | Total = %7.1f min | Per gen = %6.1f sec | Last gen = %6.1f sec | Since last gen = %.1f sec" % (i, gen, time_min, time_per_gen_sec, time_for_last_gen, time_since_last_gen)
    else:
        print "Run: %3i  | Gen: %5i  | Total = %5.1f min | Per gen = %.1f sec" % (i, gen, time_min, time_per_gen_sec)

times_ms = [end - start for [start,end,gen,prev,done] in start_end_numGens]
gens = [gen for [start,end,gen,prev,done] in start_end_numGens]

print "-----"
print "Total time = %.3f sec" % (sum(times_ms) / 1000.0)
print "Total gens = %i" % (sum(gens))
print "Overall time per generation = %.2f sec" % (sum(times_ms) / (1000.0 * sum(gens)))
