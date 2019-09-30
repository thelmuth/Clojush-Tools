

pythonscript="/home/thelmuth/Tools/best_programs_and_errors.py"

declare -a namespaces=(
    "compare-string-lengths"
    "double-letters"
    "last-index-of-zero"
    "negative-to-zero"
    "scrabble-score"
    "smallest"
    "small-or-large"
    "vector-average"
)

declare -a rates=(
    "10p"
#    "25p"
#    "50p"
)

for namespace in "${namespaces[@]}"
do
    for rate in "${rates[@]}"
    do
	#echo "$namespace"
	expdir="/home/thelmuth/Results/UMAD/size-neutral-add-delete/$namespace/"
	#expdir="/home/thelmuth/Collab/aabdelha/results/$namespace$rate/lexicase/$namespace"
	#python $pythonscript $expdir | tee "$namespace-$rate.txt"
	python $pythonscript $expdir | tee "lexicase-$namespace.txt"
    done
done
