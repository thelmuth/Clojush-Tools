
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/epsilon-lexicase-no-preselection/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/interleaved-sampling/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-epsilon-lexicase/batch-size-10/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-lexicase/batch-size-10/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-lexicase-eliteness/batch-size-10/"

#expdir="/home/thelmuth/Results/specialists-and-lexicase/subset-tournament-normal/tournament-size-7/"
#expdir="/home/thelmuth/Results/specialists-and-lexicase/subset-tournament-normal/tournament-size-1000/"
#expdir="/home/thelmuth/Results/specialists-and-lexicase/subset-tournament-normal-mu0.1/tournament-size-7/"
#expdir="/home/thelmuth/Results/specialists-and-lexicase/subset-tournament-normal-mu0.1/tournament-size-1000/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-novelty-lexicase-rate-0.25/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.25/"
expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-novelty-lexicase/rate-0.25/"


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
