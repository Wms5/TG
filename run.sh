#!/bin/bash

run() {
  echo "Running $1..."
}

if [ $# -eq 0 ]; then
  echo "Error: No name provided"
  exit 1
fi

run "$1"

pytest QuixBugs/python_testcases/test_$1.py

python3 ast_comp.py $1
