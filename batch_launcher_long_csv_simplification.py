#!/usr/bin/python
import os, glob, re
from sys import maxint

# Set these before running:

######## For simplification and generalization paper

problems = [#"checksum",
#            "collatz-numbers",
#            "compare-string-lengths",
#            "count-odds",
#            "digits",
#            "double-letters",
#            "even-squares",
#            "for-loop-index",
#            "grade",
#            "last-index-of-zero",
#            "median",
#            "mirror-image",
            "negative-to-zero",
#            "number-io",
#            "pig-latin",
#            "replace-space-with-newline",
#            "scrabble-score",
#            "smallest",
#            "small-or-large",
#            "string-differences",
#            "string-lengths-backwards",
#            "sum-of-squares",
#            "super-anagrams",
#            "syllables",
#            "vector-average",
#            "vectors-summed",
#            "wallis-pi",
#            "word-stats",
#            "x-word-lines"
            ]

for namespace in problems:
    print "Processing", namespace

    os.system("python Tools/long_csv_simplification_generalization.py %s > simplification-data/long-simp-%s.csv" % (namespace, namespace))

print "\nDone!"
