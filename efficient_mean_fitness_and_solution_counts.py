#!/usr/bin/python
import os, sys
from sys import maxint

# Set these before running:

#######################################################################################
########################### Parent Selection Experiments ##############################
#######################################################################################

#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/WORSE-small-evalpush-limit/lexicase/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/WORSE-small-evalpush-limit/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/collatz-numbers/WORSE-small-evalpush-limit/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/compare-string-lengths/NO-BETTER-more-train-cases/lexicase/logs/"

#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/count-odds/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/double-letters/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/even-squares/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/even-squares/WORSE-fewer-errors/lexicase/"
#outputDirectory = "Results/bench-prog-synth/even-squares/WORSE-fewer-errors/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/even-squares/WORSE-fewer-errors/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/for-loop-index/extra-errors/lexicase/"

#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/last-index-of-zero/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/mirror-image/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/parent-selection/ifs-7/"
#outputDirectory = "Results/clustering-bench/negative-to-zero/NO-BETTER-new-error-fn/lexicase/logs/"

#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/number-io/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/pig-latin/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/scrabble-score/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/small-or-large/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/string-differences/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/WORSE-20-training-cases/lexicase/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/WORSE-20-training-cases/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/sum-of-squares/WORSE-20-training-cases/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/super-anagrams/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vector-average/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/WORSE-extra-errors/lexicase/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/WORSE-extra-errors/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/vectors-summed/WORSE-extra-errors/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/WORSE-fewer-errors/lexicase/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/WORSE-fewer-errors/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/x-word-lines/WORSE-fewer-errors/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/parent-selection/ifs-7/"
#outputDirectory = "Results/bench-prog-synth/wallis-pi/extra-errors/lexicase/"

#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/word-stats/parent-selection/ifs-7/"

## Yuriy's problems

#outputDirectory = "Results/bench-prog-synth/checksum/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/checksum/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/checksum/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/digits/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/grade/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/median/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/median/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/median/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/smallest/parent-selection/ifs-7/"

#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/lexicase/"
#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/tourney-7/"
#outputDirectory = "Results/bench-prog-synth/syllables/parent-selection/ifs-7/"



##########################################################################################
### EHC
##########################################################################################

# 2) Normal EHC - max evals 3e10, silence mut on, hill climbing on
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/lexicase/EHC/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experimetns/tourney-7/EHC/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/ifs-7/EHC/"

# 3) max evals 3e10, silence mut on, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/EHC-testing/ifs-7/"

# 4) max gens 300, silence mut on, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-gens-300-silence-mut-on/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-gens-300-silence-mut-on/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-gens-300-silence-mut-on/ifs-7/"

# 5) max evals 3e10, silence mut off, hill climbing off
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/max-evals-3e10-silence-mut-off/ifs-7/"

# 6) max gens 300, silence mut off, hill climbing off, init max prog size 200
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/init-size-200/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/init-size-200/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/epiline-without-hill-climbing/init-size-200/ifs-7/"

# W) max evals 3e10, silence mut off, hill climbing off, init max prog size 400, half genes silenced
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/ehc-experiments/tourney-7/standard-half-silenced/"

# X) these are to see how many point evaluations are used in a typical GP run of this problem
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/lexicase/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/tourney-7/"
# outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/EHC-testing/ifs-7/"


########## EHC GECCO Paper

#outputDirectory = "Results/bench-prog-synth/count-odds/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/count-odds/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/double-letters/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/double-letters/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/grade/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/grade/ehc-experiments/tourney/EHC/"

#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/string-lengths-backwards/ehc-experiments/lexicase/standard/"

#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/negative-to-zero/ehc-experiments/lexicase/standard/"

#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/standard-half-silenced/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/epigenetic-silence-mutation/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/tourney/EHC/"
#outputDirectory = "Results/bench-prog-synth/syllables/ehc-experiments/lexicase/standard/"

# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/standard-half-silenced/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/epigenetic-silence-mutation/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/tourney/EHC/"
# outputDirectory = "Results/bench-prog-synth/vector-average/ehc-experiments/lexicase/standard/"


##########################################################################################
### Multi-Chance Lexicase
##########################################################################################

#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-2/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-3/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-4/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-5/"
#outputDirectory = "Results/bench-prog-synth/replace-space-with-newline/multi-chance-lexicase/chances-90/"


#######################################################################################
########################### Clustering Experiments ####################################
#######################################################################################

#outputDirectory = "Results/clustering-bench/replace-space-with-newline/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/replace-space-with-newline/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/replace-space-with-newline/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/replace-space-with-newline/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/syllables/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/syllables/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/syllables/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/syllables/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/string-lengths-backwards/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/string-lengths-backwards/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/string-lengths-backwards/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/string-lengths-backwards/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/negative-to-zero/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/negative-to-zero/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/negative-to-zero/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/negative-to-zero/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/double-letters/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/double-letters/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/double-letters/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/double-letters/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/scrabble-score/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/scrabble-score/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/scrabble-score/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/scrabble-score/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/checksum/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/checksum/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/checksum/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/checksum/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/checksum/more-test-cases/lexicase/logs/"

#outputDirectory = "Results/clustering-bench/count-odds/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/count-odds/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/count-odds/ifs-7/logs/"
#outputDirectory = "Results/clustering-bench/count-odds/baseline-uniform/logs/"

#outputDirectory = "Results/clustering-bench/vector-average/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/vector-average/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/vector-average/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/vector-average/more-test-cases/lexicase/logs/"

#outputDirectory = "Results/clustering-bench/number-io/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/mirror-image/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/smallest/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/median/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/last-index-of-zero/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/compare-string-lengths/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/small-or-large/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/sum-of-squares/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/digits/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/even-squares/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/super-anagrams/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/vectors-summed/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/x-word-lines/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/for-loop-index/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/string-differences/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/wallis-pi/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/pig-latin/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/word-stats/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/grade/baseline-uniform/logs/"
#outputDirectory = "Results/clustering-bench/collatz-numbers/baseline-uniform/logs/"

#######################################################################################
################# Deterministic Decimation (later called Elitist Survival)
#######################################################################################

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/replace-space-with-newline/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/replace-space-with-newline/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/replace-space-with-newline/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/replace-space-with-newline/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/replace-space-with-newline/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/replace-space-with-newline/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/vector-average/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/vector-average/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/vector-average/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/vector-average/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/vector-average/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/vector-average/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/string-lengths-backwards/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/string-lengths-backwards/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/string-lengths-backwards/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/string-lengths-backwards/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/string-lengths-backwards/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/string-lengths-backwards/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/negative-to-zero/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/negative-to-zero/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/negative-to-zero/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/negative-to-zero/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/negative-to-zero/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/negative-to-zero/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/x-word-lines/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/x-word-lines/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/x-word-lines/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/x-word-lines/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/x-word-lines/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/x-word-lines/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/syllables/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/syllables/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/syllables/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/syllables/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/syllables/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/syllables/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/mirror-image/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/mirror-image/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/mirror-image/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/mirror-image/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/mirror-image/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/mirror-image/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/count-odds/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/count-odds/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/count-odds/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/count-odds/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/count-odds/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/count-odds/tourney-7/logs/"

#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/double-letters/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/double-letters/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/double-letters/lexicase/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.25/double-letters/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.5/double-letters/tourney-7/logs/"
#outputDirectory = "Results/clustering-bench/determin-decim/ratio-0.75/double-letters/tourney-7/logs/"


#######################################################################################
############################### Lexicase Tournament Experiments #######################
#######################################################################################

#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/replace-space-with-newline/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/replace-space-with-newline/logs/"

#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/syllables/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/syllables/logs/"

#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/string-lengths-backwards/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/string-lengths-backwards/logs/"

#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/negative-to-zero/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/negative-to-zero/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/x-word-lines/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/x-word-lines/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/count-odds/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/count-odds/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/mirror-image/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/mirror-image/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/double-letters/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/double-letters/logs/"

# outputDirectory = "Results/clustering-bench/Lexicase-Tournament/keep-zeros/vector-average/logs/"
#outputDirectory = "Results/clustering-bench/Lexicase-Tournament/remove-zeros/vector-average/logs/"


#######################################################################################
############################### Hyper Selection #######################
#######################################################################################

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/double-letters/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/double-letters/tourney-7/logs/"

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/mirror-image/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/mirror-image/tourney-7/logs/"

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/count-odds/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/count-odds/tourney-7/logs/"

# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/x-word-lines/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/x-word-lines/tourney-7/logs/"

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/vector-average/lexicase/logs/"
# outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/vector-average/tourney-7/logs/"

#outputDirectory = "Results/dissertation/Hyper-Selection-Tracking/string-lengths-backwards/tourney-7/logs/"


#######################################################################################
############################### Autoconstruction ######################################
#######################################################################################

#outputDirectory = "Results/autoconstruction/replace-space-with-newline/trial1/"
#outputDirectory = "Results/autoconstruction/syllables/trial1/"
#outputDirectory = "Results/autoconstruction/string-differences/trial1/"

#outputDirectory = "Results/autoconstruction/replace-space-with-newline/csv-printing/logs/"
#outputDirectory = "Results/autoconstruction/replace-space-with-newline/csv-printing2/logs/"
#outputDirectory = "Results/autoconstruction/replace-space-with-newline/csv-printing-better-parent-tracking/logs/"

### Recursive variance
#outputDirectory = "Results/autoconstruction/recursive-variance-v2/replace-space-with-newline/csv-printing/logs/"
#outputDirectory = "Results/autoconstruction/recursive-variance-v3/replace-space-with-newline/csv-printing/logs/"

#outputDirectory = "Results/autoconstruction/recursive-variance-v3/string-differences/attempts-for-gptp-16/"
#outputDirectory = "Results/autoconstruction/recursive-variance-v3/pig-latin/attempts-for-gptp-16/"
#outputDirectory = "Results/autoconstruction/recursive-variance-v3/factorial/attempts-for-gptp-16/"
#outputDirectory = "Results/autoconstruction/recursive-variance-v3/mux-6/attempts-for-gptp-16/"

#outputDirectory = "Results/autoconstruction/recursive-variance-v3/recursively-variant-2replace-space-with-newline"

#outputDirectory = "Results/autoconstruction/v3-recursive-variance/random-cases-per-generation/levenshtein/no-autoconstruction/"
#outputDirectory = "Results/autoconstruction/v3-recursive-variance/random-cases-per-generation/levenshtein/yes-autoconstruction/"

#outputDirectory = "Results/autoconstruction/v3-recursive-variance/random-cases-per-generation-10/levenshtein/autoconstruction-False/"
#outputDirectory = "Results/autoconstruction/v3-recursive-variance/random-cases-per-generation-10/levenshtein/autoconstruction-True/"

### Higher Diversification
#outputDirectory = "Results/autoconstruction/v4-higher-diversification-threshold/replace-space-with-newline/autoconstruction-True/"

#######################################################################################
###### GPTP 16 - Plush ########
#######################################################################################

######### Genetic Operators #####################################
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/replace-space-with-newline/no-alternation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/syllables/no-alternation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/negative-to-zero/no-alternation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/x-word-lines/no-alternation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/count-odds/no-alternation"

#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/replace-space-with-newline/no-close-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/syllables/no-close-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/negative-to-zero/no-close-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/count-odds/no-close-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/x-word-lines/no-close-mutation"

#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/replace-space-with-newline/no-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/syllables/no-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/negative-to-zero/no-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/count-odds/no-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/x-word-lines/no-uniform-mutation"

#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/replace-space-with-newline/only-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/syllables/only-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/negative-to-zero/only-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/count-odds/only-uniform-mutation"
#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/x-word-lines/only-uniform-mutation"

#outputDirectory = "Results/gptp-2016/genetic-operator-experiments/replace-space-with-newline/only-uniform-mutation/csv-runs/logs/"

######### No-Auto-Parens Runs ##################################
#outputDirectory = "Results/gptp-2016/no-auto-parens/replace-space-with-newline"
#outputDirectory = "Results/gptp-2016/no-auto-parens/negative-to-zero"
#outputDirectory = "Results/gptp-2016/no-auto-parens/x-word-lines"
#outputDirectory = "Results/gptp-2016/no-auto-parens/count-odds"
#outputDirectory = "Results/gptp-2016/no-auto-parens/digits"

#######################################################################################
################ GECCO16 Diversity Workshop - Diversity Recovery ######################
#######################################################################################

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters"


####################################
# Diversity Recovery Continuations #
####################################

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/replace-space-with-newline/continuations/tournament/run0/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/lexicase/run6/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/replace-space-with-newline/continuations/tournament/run6/"

#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/lexicase/run0/"
#outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/replace-space-with-newline/continuations/tournament/run0/"

##### Double Letters #####
#------------------------#

# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/lexicase/run0/"
# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-drop-25/double-letters/continuations/tournament/run0/"

# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/lexicase/run0/"
# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/lex-div-90/double-letters/continuations/tournament/run0/"

# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/lexicase/run0/"
# outputDirectory = "Results/GECCO16/diversity-recovery/storing-populations/tourney-div-15/double-letters/continuations/tournament/run0/"


#######################################################################################
#### Sarah Troise's Runs: Weighted Lexicase Selection
#######################################################################################

#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-zeros/replace-space-with-newline/"
#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-zeros/syllables/"

#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-zeros-inverse/replace-space-with-newline/"
#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-zeros-inverse/syllables/"

#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-nonzero/replace-space-with-newline/"
#outputDirectory = "/home/stroise/results/weighted-lexicase/number-of-nonzero/syllables/"

#outputDirectory = "/home/stroise/results/weighted-lexicase/variance/replace-space-with-newline/"
#outputDirectory = "/home/stroise/results/weighted-lexicase/variance/syllables/"

#outputDirectory = "/home/stroise/results/ranked-lexicase/number-of-nonzero/replace-space-with-newline/"
#outputDirectory = "/home/stroise/results/ranked-lexicase/number-of-nonzero/syllables/"

#outputDirectory = "/home/stroise/results/bias-lexicase/number-of-nonzero/replace-space-with-newline/"

#outputDirectory = "/home/stroise/results/bias-lexicase/number-of-nonzero-inverse/syllables/"

#outputDirectory = "/home/stroise/results/bias-lexicase/average/replace-space-with-newline/"


#######################################################################################
#### Hammad Ahmad's Runs: Initialization Tests
#######################################################################################

#outputDirectory = "/home/ahmadh19/Results/enforced-diverse-pop/count-odds/"
#outputDirectory = "/home/ahmadh19/Results/enforced-diverse-pop-tourney/replace-space-with-newline/"

#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#
##########################################################################################
########################### Parent Selection Experiments v2 ##############################
##########################################################################################

outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/replace-space-with-newline/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/syllables/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/double-letters/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/string-lengths-backwards/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/x-word-lines/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/number-io/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/small-or-large/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/for-loop-index/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/compare-string-lengths/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/collatz-numbers/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/string-differences/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/even-squares/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/wallis-pi/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/last-index-of-zero/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/vector-average/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/count-odds/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/mirror-image/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/super-anagrams/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/sum-of-squares/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/negative-to-zero/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/vectors-summed/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/median/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/smallest/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/digits/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/pig-latin/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/scrabble-score/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/word-stats/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/grade/"
#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase/checksum/"

#outputDirectory = "/home/thelmuth/Results/parent-selection-v2/lexicase-3000-gens/string-differences/"

# TMH
#######################################################################################
#### Divide and Conquer Lexicase
#######################################################################################

#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-2/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-2/syllables/"
#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-3/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-3/syllables/"
#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-5/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/divide-and-conquer-lexicase/group-size-5/syllables/"


#######################################################################################
#### SMAC Parameters
#######################################################################################
#outputDirectory = "/home/thelmuth/Results/SMAC-params/v1/replace-space-with-newline/"
#outputDirectory = "/home/thelmuth/Results/SMAC-params/v1/syllables/"
#outputDirectory = "/home/thelmuth/Results/SMAC-params/v1/string-lengths-backwards/"
#outputDirectory = "/home/thelmuth/Results/SMAC-params/v1/double-letters/"
#outputDirectory = "/home/thelmuth/Results/SMAC-params/v1/x-word-lines/"

#######################################################################################
#### Paired-Lexicase
#######################################################################################

#outputDirectory = "Results/renewed-parent-selection-tests/paired-lexicase/tuple-size-2/replace-space-with-newline/"
#outputDirectory = "Results/renewed-parent-selection-tests/paired-lexicase/tuple-size-3/replace-space-with-newline/"

#outputDirectory = "Results/renewed-parent-selection-tests/paired-lexicase/tuple-size-2/syllables/"
#outputDirectory = "Results/renewed-parent-selection-tests/paired-lexicase/tuple-size-3/syllables/"

#######################################################################################
#### Interleaved Sampling
#######################################################################################

#outputDirectory = "Results/parent-selection-v2/interleaved-sampling/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/interleaved-sampling/syllables/"
#outputDirectory = "Results/parent-selection-v2/interleaved-sampling/double-letters/"
#outputDirectory = "Results/parent-selection-v2/interleaved-sampling/string-lengths-backwards/"

#######################################################################################
#### Eliteness-Based Tournament
#######################################################################################

#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-2/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-4/replace-space-with-newline/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-7/replace-space-with-newline/"

#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-2/syllables/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-4/syllables/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-7/syllables/"

#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-2/string-lengths-backwards/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-4/string-lengths-backwards/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-7/string-lengths-backwards/"

#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-2/double-letters/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-4/double-letters/"
#outputDirectory = "Results/parent-selection-v2/eliteness-based-tournament/size-7/double-letters/"

###################
## A few disparate tests

#outputDirectory = "Results/autoconstruction/autoconstruction-False/generations-2000/replace-space-with-newline/"


####################################################
## Epsilon Lexicase - program synthesis experiment

#outputDirectory = "Results/epsilon-lexicase/not-epsilon-lexicase/sextic/"

#outputDirectory = "Results/epsilon-lexicase/dynamic/sextic/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/number-io/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/vector-average/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/wallis-pi/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/double-letters/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/x-word-lines/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/count-odds/"
#outputDirectory = "Results/epsilon-lexicase/dynamic/replace-space-with-newline/"

#outputDirectory = "Results/epsilon-lexicase/static/sextic/"
#outputDirectory = "Results/epsilon-lexicase/static/number-io/"
#outputDirectory = "Results/epsilon-lexicase/static/vector-average/"
#outputDirectory = "Results/epsilon-lexicase/static/wallis-pi/"
#outputDirectory = "Results/epsilon-lexicase/static/double-letters/"
#outputDirectory = "Results/epsilon-lexicase/static/x-word-lines/"
#outputDirectory = "Results/epsilon-lexicase/static/count-odds/"
#outputDirectory = "Results/epsilon-lexicase/static/replace-space-with-newline/"

#outputDirectory = "Results/epsilon-lexicase/super-dynamic/sextic/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/number-io/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/vector-average/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/wallis-pi/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/double-letters/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/x-word-lines/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/count-odds/"
#outputDirectory = "Results/epsilon-lexicase/super-dynamic/replace-space-with-newline/"

outputFilePrefix = "log"
outputFileSuffix = ".txt"


#outputFilePrefix = "bio-ultralog"
#outputFilePrefix = "bio-normallog"

errorType = "float"

# Some functions
def median(lst):
    if len(lst) <= 0:
        return False
    sorts = sorted(lst)
    length = len(lst)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def mean(nums):
    if len(nums) <= 0:
        return False
    return sum(nums) / float(len(nums))

def reverse_readline(filename, buf_size=8192):
    """a generator that returns the lines of a file in reverse order
       From: https://stackoverflow.com/questions/2301789/read-a-file-in-reverse-order-using-python"""
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        total_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(total_size, offset + buf_size)
            fh.seek(-offset, os.SEEK_END)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # the first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # if the previous chunk starts right from the beginning of line
                # do not concact the segment to the last line of new chunk
                # instead, yield the segment first 
                if buffer[-1] is not '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if len(lines[index]):
                    yield lines[index]
        yield segment


# Main area
i = 0

if outputDirectory[-1] != '/':
    outputDirectory += '/'
dirList = os.listdir(outputDirectory)

print
print "           Directory of results:"
print outputDirectory

bestFitnessesOfRuns = []
testFitnessOfBest = []
testFitnessOfSimplifiedBest = []
errorThreshold = maxint
errorThresholdPerCase = maxint

fileName0 = (outputFilePrefix + str(i) + outputFileSuffix)
f0 = open(outputDirectory + fileName0)

for line in f0:
    if line.startswith("error-threshold"):
        try:
            errorThreshold = int(line.split()[-1])
        except ValueError, e:
            errorThreshold = float(line.split()[-1])
        if errorThreshold == 0:
            errorThresholdPerCase = 0

    if errorThresholdPerCase == maxint and line.startswith("Errors:"):
        numCases = len(line.split()) - 1
        errorThresholdPerCase = float(errorThreshold) / numCases

    if errorThresholdPerCase != maxint:
        break

while (outputFilePrefix + str(i) + outputFileSuffix) in dirList:
    sys.stdout.write("%4i" % i)
    sys.stdout.flush()
    if i % 25 == 24:
        print

    runs = i + 1 # After this loop ends, runs should be correct
    fileName = (outputFilePrefix + str(i) + outputFileSuffix)
#    f = open(outputDirectory + fileName)

    #final = False
    gen = 0
    best_mean_error = maxint
    done = False

    bestTest = maxint
    simpBestTest = maxint

    for line in reverse_readline(outputDirectory + fileName):

        if line.startswith(";; -*- Report") and gen == 0:
            gen = int(line.split()[-1])

        if gen != 0 and best_mean_error < maxint:
            break

        if line.startswith("SUCCESS"):
            done = "SUCCESS"

        if line.startswith("FAILURE"):
            done = "FAILURE"

        if line.startswith("Mean:"):
            gen_best_error = -1
            if errorType == "float":
                gen_best_error = float(line.split()[-1])
            elif errorType == "int" or errorType == "integer":
                gen_best_error = int(line.split()[-1])
            else:
                raise Exception("errorType of %s is not recognized" % errorType)

            if gen_best_error < best_mean_error:
                best_mean_error = gen_best_error

        if line.startswith("Test total error for best:") and done:
            try:
                bestTest = int(line.split()[-1].strip("Nn"))
            except ValueError, e:
                bestTest = float(line.split()[-1].strip("Nn"))

        if line.startswith("Test total error for best:") and not done:
            try:
                simpBestTest = int(line.split()[-1].strip("Nn"))
            except ValueError, e:
                simpBestTest = float(line.split()[-1].strip("Nn"))


    bestFitnessesOfRuns.append((gen, best_mean_error, done))
    testFitnessOfBest.append(bestTest)
    testFitnessOfSimplifiedBest.append(simpBestTest)
            
    i += 1

print "Error threshold per case:", errorThresholdPerCase
print "-------------------------------------------------"

for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    doneSym = ""
    if fitness <= errorThresholdPerCase:
        doneSym = " <- suc"
        if not done:
            doneSym += "$$$$$$ ERROR $$$$$$" #Should never get here
        if len(testFitnessOfBest) > i and testFitnessOfBest[i] < maxint:
            if isinstance(testFitnessOfBest[i], int):
                doneSym += " | test = %i" % testFitnessOfBest[i]
            else:
                doneSym += " | test = %.3f" % testFitnessOfBest[i]
        if len(testFitnessOfSimplifiedBest) > i and testFitnessOfSimplifiedBest[i] < maxint:
            if isinstance(testFitnessOfSimplifiedBest[i], int):
                doneSym += " | test on simplified = %i" % testFitnessOfSimplifiedBest[i]
            else:
                doneSym += " | test on simplified = %.4f" % testFitnessOfSimplifiedBest[i] #TMH this line changed
    elif not done:
        doneSym = " -- not done"
    if fitness >= 0.001 or fitness == 0.0:
        print "Run: %3i  | Gen: %5i  | Best Fitness (mean) = %8.4f%s" % (i, gen, fitness, doneSym)
    else:
        print "Run: %3i  | Gen: %5i  | Best Fitness (mean) = %.4e%s" % (i, gen, fitness, doneSym)

totalFitness = 0
inds = 0
perfectSolutions = 0
perfectOnTestSet = 0
simpPerfectOnTestSet = 0
trainSolutionGens = []
testSolutionGens = []

for i, (gen, fitness, done) in enumerate(bestFitnessesOfRuns):
    if done:
        totalFitness += fitness
        inds += 1
        if fitness <= errorThresholdPerCase:
            perfectSolutions += 1
            trainSolutionGens.append(gen)
            if len(testFitnessOfBest) > i:
                if testFitnessOfBest[i] <= errorThresholdPerCase:
                    perfectOnTestSet += 1
                    testSolutionGens.append(gen)
            if len(testFitnessOfSimplifiedBest) > i:
                if testFitnessOfSimplifiedBest[i] <= errorThresholdPerCase:
                    simpPerfectOnTestSet += 1

if len(trainSolutionGens) > 0:
    print "------------------------------------------------------------"
    print "Training Solution Generations:"
    print "Mean:      ", mean(trainSolutionGens)
    print "Minimum:   ", min(trainSolutionGens)
    print "Median:    ", median(trainSolutionGens)
    print "Maximum:   ", max(trainSolutionGens)

    if len(testSolutionGens) > 0:
        print "--------------------------"
        print "Test Solution Generations:"
        print "Mean:      ", mean(testSolutionGens)
        print "Minimum:   ", min(testSolutionGens)
        print "Median:    ", median(testSolutionGens)
        print "Maximum:   ", max(testSolutionGens)

print "------------------------------------------------------------"

print "Number of finished runs:            %4i" % inds
print "Solutions found:                    %4i" % (perfectSolutions)
print "Zero error on test set:             %4i" % perfectOnTestSet
print "Simplified zero error on test set:  %4i" % simpPerfectOnTestSet

print "------------------------------------------------------------"

if inds > 0:
    print "MBF: %.5f" % (totalFitness / float(inds))
