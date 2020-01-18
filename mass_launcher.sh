
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/"
#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/"

#expdir="/home/thelmuth/Collab/thelmuth/Results/epigenetic-tags/"

#expdir="/home/thelmuth/Collab/thelmuth/Results/domain-knowledge/kitchen-sink-instructions/"

#expdir="/home/thelmuth/Collab/aabdelha/results2/batch-tournament/"

#expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-drive-gp/add-case-after-50-gens/"
#expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-25-generations/"
expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-100-generations/"

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
    echo "$namespace"
    if [ "$1" != "" ]; then
	python $pythonscript "$expdir$namespace" $1
    else
	python $pythonscript "$expdir$namespace" brief
    fi
done
