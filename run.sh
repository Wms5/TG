#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Error: No name provided"
  exit 1
fi

echo "Run $1 in execution $2"

dir=$(pwd)

output_file="$dir/Results_1_ChatGPT/python_programs_run$2/$1/notes.txt"

command1="pytest QuixBugs/python_testcases/test_$1.py"

command2="python3 ast_comp.py $1"

$command1 > $output_file 2>&1
$command2 >> $output_file 2>&1
