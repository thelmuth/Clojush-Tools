
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-tournament/batch-size-8-tournament-size-64/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/batch-tournament/batch-size-8-tournament-size-7/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/tournament/size-32/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/tournament/size-4/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pareto-tournament/objectives-total-error-size-age/tournament-size-64/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pareto-tournament/objectives-total-error-age/tournament-size-64/"


#expdir="/home/thelmuth/Collab/thelmuth/Results/epigenetic-tags/"

#expdir="/home/thelmuth/Collab/thelmuth/Results/domain-knowledge/kitchen-sink-instructions/"
#expdir="/home/thelmuth/Results/domain-knowledge/transfer-learning-100percent/"

#expdir="/home/thelmuth/Collab/aabdelha/results2/batch-tournament/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/pool-lexicase/pool-size-100/"

#expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-drive-gp/add-case-after-50-gens/"
#expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-25-generations/"
#expdir="/home/thelmuth/Collab/thelmuth/Results/counterexample-driven-gp/add-case-after-100-generations/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.175/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.02/"
expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase/rate-0.01/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase-increase-pop/rate-0.175/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase-increase-pop/rate-0.05/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase-increase-both-pop-and-gens-equally/rate-0.25/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase-increase-both-pop-and-gens-equally/rate-0.175/"
#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/downsample-lexicase-increase-both-pop-and-gens-equally/rate-0.1/"


#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/ifs/e-over-e-plus-1/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/random-threshold-lexicase/"

#expdir="/home/thelmuth/Results/output-instructions/with-popping/"
#expdir="/home/thelmuth/Results/output-instructions/output-instructions-dont-pop/"
#expdir="/home/thelmuth/Results/output-instructions/output-instructions-dont-pop-with-defaults/"

#expdir="/home/thelmuth/Results/parent-selection-v3-UMAD/madcap-epsilon-lexicase/semi-dynamic/rate-of-zero-epsilon-0.25/"



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
    echo "$namespace"
    if [ "$1" != "" ]; then
	python $pythonscript "$expdir$namespace" $1
    else
	python $pythonscript "$expdir$namespace" brief
    fi
done
