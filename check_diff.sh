#!/bin/bash
# This script checks for the differences in original and modified files.

modified_files=$(git ls-files -m)

if  [ ! -z "$modified_files" ]
then
	diff_ext="_diff.diff"
	my_dir="modified_files_directory"
	mkdir $my_dir 

	for file in $modified_files
	do
		IFS='/' read -ra ADDR <<< "$file"
		
		filename=${ADDR[2]}

		git diff $file > $my_dir/$filename$diff_ext
		
	done
else
	echo "No modified files!"
fi