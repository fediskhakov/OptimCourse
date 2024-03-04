#!bash
# This script runs git command to find changes between the current branch and the one given in first argument,
# and checks out all modified and appended files from the the given other branch
# These changes can then be inspected one-by-one in git changes in the current branch

if [ $# -eq 0 ]
  then
    echo "Need name of the git branch to checkout files from"
    exit 0
fi

current_branch=$(git rev-parse --abbrev-ref HEAD)

# check if given branch exists
git show-ref --verify --quiet "refs/heads/$1"
if [[ $? -ne 0 ]]; then
    echo "Branch '$1' does not exist."
    exit 0
fi

echo Current branch: $current_branch
echo "This script will check out modified and appended files from branch '$1'"

# list=$(git diff --name-status --find-renames --diff-filter=d $current_branch..$1)
list=(git diff --name-status --find-renames --diff-filter=d $current_branch..$1)
# https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-diff.html
# Possible status letters are:
# A: addition of a file
# C: copy of a file into a new one
# D: deletion of a file
# M: modification of the contents or mode of a file
# R: renaming of a file
# T: change in the type of the file (regular file, symbolic link or submodule)
# U: file is unmerged (you must complete the merge before it can be committed)
# X: "unknown" change type (most probably a bug, please report it)

"${list[@]}" | while IFS= read -r c; do
  read -r status filename <<< "$c"

  echo -n  "$filename: "

  git checkout $1 $filename

done

echo "All done!"
