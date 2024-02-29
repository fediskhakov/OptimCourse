#!bash
# This script copies solutions of the exercises from the private repository/folder
# Argument should be the prefix for the file name to copy, compulsory

# Outside folder with exercises
source_dir="../../01.tutorials"

if [ $# -eq 0 ]
  then
    echo "Need prefix for the files to copy"
  else
    cp $source_dir/$1*_formulation.md .
    cp $source_dir/$1*_hint.md .
    cp $source_dir/$1*_solution.md .
    # also copy static files
    cp -r $source_dir/_static ../
fi

