#! /bin/bash

# This script converts all .pdf files in a given directory
# to png image files, and saves them here.
# Tested and works on Fedor's mac

# argument: path to the directory to be converted

if [ $# -eq 0 ]; then
    echo No arguments passed, need directory path
    exit 1
fi

dirname=$1
# remote trailing / if given
dirname=${dirname%/}

echo "Converting all *.pdf files in directory $dirname"

for filename in $dirname/*.pdf; do
  # if [[ ! -e "$filename" ]]; then continue; fi

  echo "$filename --> png"
  fn=$(basename "$filename")
	fn=${fn%.pdf}

	# convert to png
	sips -s format png $fn.pdf --out ./$fn.png > /dev/null
	#  &>/dev/null
  # pdf2ps "$fn.pdf" "$fn.eps" &>/dev/null

done

# rm -rf _frame.*

echo "All done!"
