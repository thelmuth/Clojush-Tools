
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Results/plushi/"
#expdir="/home/thelmuth/Results/elitist-survival-2018/rate-80/lexicase/"
expdir="/home/thelmuth/Results/elitist-survival-2018-not-UMAD/rate-50/lexicase/"

declare -a namespaces=(
    "replace-space-with-newline"
    "syllables"
    "vector-average"
    "string-lengths-backwards"
    "mirror-image"
    "x-word-lines"
    "negative-to-zero"
    "double-letters"
    "last-index-of-zero"
    "compare-string-lengths"
    "sum-of-squares"

    # "number-io"
    # "small-or-large"
    # "for-loop-index"
    # "string-differences"
    # "even-squares"
    # "count-odds"
    # "super-anagrams"
    # "vectors-summed"
    # "scrabble-score"
    # "checksum"
    # "digits"
    # "grade"
    # "median"
    # "smallest"

    # "collatz-numbers"
    # "wallis-pi"
    # "pig-latin"
    # "word-stats"
)

for namespace in "${namespaces[@]}"
do
    #echo "$namespace"
    python $pythonscript "$expdir$namespace" brief

done
