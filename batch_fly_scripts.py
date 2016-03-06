import os, stat, random

##########################################################################
# Settings

script = "Tools/selection_stats_by_success_failure.py"

#script_arg_tuples = [
#                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/replace-space-with-newline/logs/",),
#                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/syllables/logs/",),
#                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/string-lengths-backwards/logs/",),
#                     ]

# script_arg_tuples = [("Results/clustering-bench/Lexicase-Tournament/keep-zeros/negative-to-zero/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/negative-to-zero/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/x-word-lines/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/x-word-lines/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/count-odds/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/count-odds/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/mirror-image/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/mirror-image/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/double-letters/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/double-letters/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/vector-average/logs/",),
#                      ("Results/clustering-bench/Lexicase-Tournament/remove-zeros/vector-average/logs/",)
#                      ]

script_arg_tuples = [("Results/clustering-bench/Lexicase-Tournament/keep-zeros/negative-to-zero/logs/",),
                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/x-word-lines/logs/",),
                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/count-odds/logs/",),
                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/mirror-image/logs/",),
                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/double-letters/logs/",),
                     ("Results/clustering-bench/Lexicase-Tournament/keep-zeros/vector-average/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/double-letters/lexicase/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/mirror-image/lexicase/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/count-odds/lexicase/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/x-word-lines/lexicase/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/vector-average/lexicase/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/double-letters/tourney-7/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/mirror-image/tourney-7/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/count-odds/tourney-7/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/x-word-lines/tourney-7/logs/",),
                     ("Results/dissertation/Hyper-Selection-Tracking/vector-average/tourney-7/logs/",),
                     ]

title_string = "Batch processing selection counts | success/failure hyper selection"

alfname = "hyper-selection-success-failure"

service_tag = "tom"

##########################################################################
# You don't need to change anything below here

# Make alf file
alf_file_string = "alf_scripts/" + alfname + "_" + ('%010x' % random.randrange(16**10)) + ".alf"

alf_f = open(alf_file_string, "w")

alfcode = """##AlfredToDo 3.0
Job -title {%s} -subtasks {
""" % (title_string)

for arg_tuple in script_arg_tuples:

    command = "cd /home/thelmuth; /opt/pixar/tractor-blade-1.7.2/python/bin/python2.6 " + script

    for arg in arg_tuple:
        command += " " + str(arg)

    alfcode += """    Task -title {%s} -cmds {
        RemoteCmd {/bin/sh -c {%s}} -service {%s}
    }
""" % (title_string, command, service_tag)

alfcode += "}\n"

alf_f.writelines(alfcode)
alf_f.close()

# Run tractor command
source_string = "source /etc/sysconfig/pixar"
pixar_string = "/opt/pixar/tractor-blade-1.7.2/python/bin/python2.6 /opt/pixar/tractor-blade-1.7.2/tractor-spool.py --engine=fly:8000"

os.system("%s;%s %s" % (source_string, pixar_string, alf_file_string))
