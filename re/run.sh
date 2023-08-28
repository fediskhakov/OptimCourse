#!/bin/bash

# Script to convert question bank from yaml to xml
PATTERNS=conversions.yml
FILE=../06.optimization_fundamentals.md0
OUTPUT=../06.optimization_fundamentals.md

# python3 repl.py $PATTERNS $FILE -o $OUTPUT

FILE=../06.exercises.E.md
OUTPUT=../06.exercises.E.md

# python3 repl.py $PATTERNS $FILE -o $OUTPUT

FILE=../../01.solutions/exercise_solutions/06.solutions_E.md 
OUTPUT=../../01.solutions/exercise_solutions/06.solutions_E.md 

python3 repl.py $PATTERNS $FILE -o $OUTPUT
