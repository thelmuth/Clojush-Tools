
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/"
#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/"

#expdir="/home/thelmuth/Results/plushi/"
#expdir="/home/thelmuth/Results/elitist-survival-2018/rate-90/lexicase/"
#expdir="/home/thelmuth/Results/elitist-survival-2018-not-UMAD/rate-100/lexicase/"
#expdir="/home/thelmuth/Results/elitist-survival-2018-not-UMAD/rate-30/tournament/"

#expdir="/home/thelmuth/Results/UMAD/tournament/size-neutral-add-delete/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/epsilon-lexicase/"
#expdir="/home/thelmuth/Results/elitist-survival-2018/rate-80/lexicase/"
#expdir="/home/thelmuth/Results/elitist-survival-2018-not-UMAD/rate-50/lexicase/"

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
    if [ "$1" != "" ]; then
	python $pythonscript "$expdir$namespace" $1
    else
	python $pythonscript "$expdir$namespace" brief
    fi
done
