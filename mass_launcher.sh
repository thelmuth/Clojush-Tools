
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

expdir="/home/thelmuth/Collab/ccourtne/UCD-UMAD-test/"

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
    # "sum-of-squares"
    # "vectors-summed"
    # "pig-latin"
    # "checksum"
    # "digits"
    # "grade"
    # "median"


    # "collatz-numbers"
    # "wallis-pi"
    # "word-stats"

    #### PSB2
    # basement
    # bouncing-balls
    # bowling
    # camel-case
    # coin-sums
    # cut-vector
    # dice-game
    # find-pair
    # fizz-buzz
    # fuel-cost
    # gcd
    # indices-of-substring
    # leaders
    # luhn
    # mastermind
    # middle-character
    # paired-digits
    # shopping-list
    # snow-day
    # solve-boolean
    # spin-words
    # square-digits
    # substitution-cipher
    # twitter
    # vector-distance

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
