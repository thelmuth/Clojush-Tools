
pythonscript="Tools/efficient_mean_fitness_and_solution_counts.py"

#expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/genops-original/"
expdir="/home/thelmuth/Collab/thelmuth/Results/novelty-lexicase/gens-1000/no-novelty-genops-original/"

#expdir="/home/thelmuth/Results/plushi/"
#expdir="/home/thelmuth/Results/elitist-survival-2018/rate-80/lexicase/"
#expdir="/home/thelmuth/Results/elitist-survival-2018-not-UMAD/rate-50/lexicase/"


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
