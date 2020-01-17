
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-tournament/batch-size-8-tournament-size-64/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-tournament/batch-size-8-tournament-size-7/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/tournament/size-64/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/knobelty/hamming/knobelty-novelty-probability-0.2/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/knobelty/manhattan/knobelty-novelty-probability-0.2/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/madcap-epsilon-lexicase/semi-dynamic/rate-of-zero-epsilon-0.5/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pool-lexicase/pool-size-10/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/novelty-search/hamming-distance/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/novelty-search/manhattan-distance/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pareto-tournament/objectives-total-error-size/tournament-size-32/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pareto-tournament/objectives-total-error-age/tournament-size-32/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/co-solvability/divide-by-max-error/"

expdir=$1


declare -a namespaces=(
    "compare-string-lengths"
    "double-letters"
    "replace-space-with-newline"
    "string-lengths-backwards"
    "last-index-of-zero"
    "vector-average"
    "mirror-image"
    "x-word-lines"
    "negative-to-zero"
    "scrabble-score"
    "smallest"
    "syllables"

    "number-io"
    "small-or-large"
    "for-loop-index"
    "string-differences"
    "even-squares"
    "count-odds"
    "super-anagrams"
    "sum-of-squares"
    "vectors-summed"
    "pig-latin"
    "checksum"
    "digits"
    "grade"
    "median"


    # "collatz-numbers"
    # "wallis-pi"
    # "word-stats"
)

for namespace in "${namespaces[@]}"
do
    #echo "$namespace"
    if [ "$2" != "" ]; then
	python $pythonscript "$expdir$namespace" $2
    else
	python $pythonscript "$expdir$namespace" brief
    fi
done
