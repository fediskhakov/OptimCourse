#!/bin/bash

# Script to convert question bank from yaml to xml
PATTERNS=conversions.yml
FILE=../08.temp.md
OUTPUT=../08.temp_out.md

# python3 repl.py $PATTERNS $FILE -o $OUTPUT
# python3 repl.py $PATTERNS $FILE -o $OUTPUT

# FILE=../../01.solutions/exercise_solutions/06.solutions_E.md 
# OUTPUT=../../01.solutions/exercise_solutions/06.solutions_E.md 

python3 repl.py $PATTERNS $FILE -o $OUTPUT
