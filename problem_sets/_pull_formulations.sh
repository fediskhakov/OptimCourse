#!bash
# This script copies formulations+hints of the exercises from the private repository/folder
# Argument should be the prefix for the file name to copy, compulsory

# Outside folder with exercises
source_dir="../../02.tutorials"

if [ $# -eq 0 ]
  then
    echo "Need prefix for the files to copy"
  else
    cp $source_dir/$1*_formulation.md .
    cp $source_dir/$1*_hint.md .
    # create empty solution file
    for file in $(ls -v $source_dir/$1*_solution.md); do
      fn=$(basename "$file")
      cnt=${fn#*$1}
      cnt=${cnt%_solution*}
      echo "⏱" > $1$cnt"_solution.md"
    done
    # also copy static files
    cp -r $source_dir/_static ../
fi

