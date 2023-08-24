#!/bin/bash

# Script to convert question bank from yaml to xml
FILE=../05.linear_algebra.md
PATTERNS=conversions.yml
OUTPUT=test.md

python3 repl.py $PATTERNS $FILE -o $OUTPUT
