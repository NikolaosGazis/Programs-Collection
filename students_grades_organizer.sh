#!/bin/bash

# Global Variables #
counter=0 # of Students.
grades_loc="$HOME/Desktop/grades.txt"
organized_dir="$HOME/Desktop/organized"

# Check if a directory parameter is given by the user #
if [ $# -eq 0 ]; then # none given
    echo "[SYSTEM] You must pass a directory as an argument...try again."
    exit 1
fi

# Check if the given directory exists #
if [ ! -d "$1" ]; then # ! = "not"
    echo "[SYSTEM] Attention! Couldn't find the directory. Ending program..."
    exit 1
fi

# If grades.txt exists #
if [ -e "$grades_location" ]; then
    echo "[SYSTEM] The file already exists and will be recreated!"
    rm $grades_location
fi
touch "$grades_loc"
echo "[SYSTEM] Created grades.txt!"

# Collect student data #
for student in "$1"/*; do # for every (*) student folder in the given directory.
    counter=$((counter+1)) # increment counter.
    
    # Location of the report file #
    report_file="$student/report.txt"
    
    # Collect data from the report #
    stu_name=$(awk '{print $1}' "$report_file")
    reg_number=$(awk '{print $2}' "$report_file")
    
    # scores - remain 0 if they student does not meet the requirements #
    project1_score=0
    project2_score=0
    
    # Project 1 - execute so it can compare the numeric data #
    pro1_result=$(gcc -o "$student/project1" "$student/project1.c" && "$student/project1")
    if [ "$pro1_result" -eq 20 ]; then # full grade
    	project1_score=30
    fi
    
    # Project 2 - execute so it can compare numeric data #
    pro2_result=$(gcc -o "$student/project2" "$student/project2.c" && "$student/project2")
    if [ "$pro2_result" -eq 10 ]; then # full grade
    	project2_score=70
    fi
    
    # Calculate total score #
    total=$((project1_score+project2_score))
    
    # Pass the data to the grades.txt #
    echo "$stu_name $reg_number project1: $project1_score project2: $project2_score total_grade: $total">>"$grades_location"
    
    # Check if directory exists #
    if [ "$counter" -eq 1 ]; then # first student.
        if [ -d "$organized" ]; then
    	    echo "[SYSTEM] Organized already exists and will be recreated."
    	    rm -r "$organized" # may contain files, so us rm.
        fi
        mkdir "$organized_dir"
        echo "[SYSTEM] Created organized directory!"
    fi    
    
    # Move files to the directory according to user input #
    read -p "Organize the files of the particular student? (y/n): " user_answer # input
    if [ "$user_answer" = "y" ]; then
    	cp "$student/project1.c" "$organized/${stu_name}_${reg_number}_project1.c"
    	cp "$student/project2.c" "$organized/${stu_name}_${reg_number}_project2.c"
    fi
done
