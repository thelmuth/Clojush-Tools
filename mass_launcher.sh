

pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/"
expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/"

declare -a namespaces=(
    "replace-space-with-newline"
    "syllables"
    "vector-average"
    "mirror-image"
    "double-letters"
    "last-index-of-zero"
    "compare-string-lengths"
    "negative-to-zero"
    "scrabble-score"
    "x-word-lines"
    "pig-latin"
)

for namespace in "${namespaces[@]}"
do
    #echo "$namespace"
    python $pythonscript "$expdir$namespace" brief

done
