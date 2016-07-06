#import math
import os
#import sys

# Set these before running:

csv_format = "wide" # Can be wide or long

######## For GPTP Plush Paper

dirs = [("Replace Space With Newline", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
        ("Syllables", "Results/bench-prog-synth/syllables/parent-selection/lexicase/"),
        ("Negative To Zero", "Results/bench-prog-synth/negative-to-zero/parent-selection/lexicase/"),
        ("X-Word Lines", "Results/bench-prog-synth/x-word-lines/parent-selection/lexicase/"),
        ("Count Odds", "Results/bench-prog-synth/count-odds/parent-selection/lexicase/")]




######## For dissertation

#dirs = [("lexicase", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/")]


# dirs = [("lexicase", "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"),
#         ("tourney7", "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"),
#         ("ifs7", "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/")]

######### Old

#dir1 = "Results/GECCO13/bio-normal/"
#dir2 = "Results/GECCO13/bio-45/"
#dir3 = "Results/GECCO13/bio-ultra/"
#dir4 = "Results/equal-size-ULTRA/bio/"

#dir1 = "Results/GECCO13/pagie-no-erc-normal/"
#dir2 = "Results/GECCO13/pagie-hogeweg-no-erc-45/"
#dir3 = "Results/GECCO13/pagie-no-erc-ultra/"
#dir4 = "Results/equal-size-ULTRA/pagie-no-erc/"

#dir1 = "Results/GECCO13/mux6-normal/"
#dir2 = "Results/GECCO13/mux6-ultra/"
#dir4 = "Results/equal-size-ULTRA/mux6/"

#dir1 = "Results/GECCO13/factorial-normal/"
#dir2 = "Results/GECCO13/factorial-ultra/"
#dir3 = "Results/GECCO13/factorial-ultra-large/"

#dir1 = "Results/GECCO13/factorial-normal-500gens/"
#dir2 = "Results/GECCO13/factorial-ultra-500gens/"
#dir4 = "Results/equal-size-ULTRA/factorial/"

# dir1 = "Results/gecco13/DM/mom2-lex-ultra"
# dir2 = "Results/plush-testing/dm2-ultra-lex/"
# dir3 = "Results/plush-testing/dm2-zero-align-dev/" 
# dir4 = "Results/plush-testing/dm2-noops/"

# prefix1 = "log"
# prefix2 = "bio-normallog"

#dirs = [("Normal", dir1, prefix1),
#        ("Normal_45", dir2, prefix1),
#        ("ULTRA", dir3, prefix1),
#        ("ULTRA-Equal-Sizes", dir4, prefix1)]

# dirs = [("Push", dir1, prefix1),
#         ("Plush", dir2, prefix1),
#         ("PlushNoops", dir4, prefix1),
#         ("PlushNoAlignDev", dir3, prefix1)]

outputFileSuffix = ".txt"

def my_mean(list_of_nums):
    if len(list_of_nums) == 0:
        return 0.0
    return float(sum(list_of_nums)) / float(len(list_of_nums))

def getProgramSizes(outputDirectory, outputFilePrefix):
    global max_gen

    i = 0

    if outputDirectory[-1] != '/':
        outputDirectory += '/'
    dirList = os.listdir(outputDirectory)


    max_generations = 0
    sizes_per_gen = []

    while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:

        fileName = (outputFilePrefix + str(i) + outputFileSuffix)
        f = open(outputDirectory + fileName)

        gen = 0
        mean_size = 0

        for line in f:
            if i == 0:
                if line.startswith("max-generations"):
                    max_generations = int(line.split()[-1])
                    max_gen = max_generations
                    sizes_per_gen = [[] for x in range(max_generations + 1)]

            if line.startswith(";; -*- Report"):
                gen = int(line.split()[-1])

            if line.startswith("Average genome size in population (length)"):
                mean_size = float(line.split()[-1])
                sizes_per_gen[gen].append(mean_size)

        i += 1

    return sizes_per_gen


if csv_format == "long":
    print "Condition,Generation,MeanGenomeSize"
    # for (condition, directory, prefix) in dirs:
    #     sizes = getProgramSizes(directory, prefix)
    for (condition, directory) in dirs:
        sizes = getProgramSizes(directory, "log")

        for gen, gen_sizes in enumerate(sizes):
            print "%s,%i,%f" % (condition, gen, my_mean(gen_sizes))

elif csv_format == "wide":
    print "generation," + str([n for (n,d) in dirs]).replace(" ","").replace("]","").replace("[","").replace("'","")

    dir_size_lists = [getProgramSizes(d, "log") for (n,d) in dirs]
#    print "dir_size_lists = ", dir_size_lists
    for g in range(max_gen+1):
        out_str = str(g) + ","
        for size_list in dir_size_lists:
            try:
                size = "%0.3f," % my_mean(size_list[g])
            except:
                size = ","
            out_str += size
        print out_str[:-1]

else:
    print "Invalid csv_format:", csv_format
