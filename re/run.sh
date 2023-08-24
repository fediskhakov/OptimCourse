#!/bin/bash

# Script to convert question bank from yaml to xml
PATTERNS=conversions.yml
FILE=../05.linear_algebra.md_orig
OUTPUT=../05.linear_algebra_converted.md
FILE=../05.linear_algebra.md_orig
OUTPUT=../05.linear_algebra_converted.md

# python3 repl.py $PATTERNS $FILE -o $OUTPUT

FILE=../05.exercises.D.md
OUTPUT=../05.exercises.D.md

python3 repl.py $PATTERNS $FILE -o $OUTPUT

FILE=../../01.solutions/exercise_solutions/05.solutions_D.md 
OUTPUT=../../01.solutions/exercise_solutions/05.solutions_D.md 

python3 repl.py $PATTERNS $FILE -o $OUTPUT
