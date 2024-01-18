#!/bin/bash
counter=0 # student counter

# Check if a directory parameter is given by the user - check total arguments #
if [ $# -eq 0 ]; then # none given
    echo "• You must pass a directory as an argument...try again."
    exit 1 # end
fi

# Check if the given directory exists or not #
if [ ! -d "$1" ]; then # ! = "not"
    echo "• Attention! Couldn't find the directory. Ending program..."
    exit 1 # end
fi

# Check if the grades file exists #
grades_location="$HOME/Desktop/grades.txt"

if [ -e "$grades_location" ]; then
    echo "• The file already exists and will be recreated!"
    rm $grades_location
fi

# Create it #
touch grades.txt
echo "• Created grades.txt!"

# Collect student data #
for student in "$1"/*; do # for every (*) student folder in the given directory
    counter=$((counter+1)) # increase
    # location of the report file #
    report_file="$student/report.txt"
    # collect data from the report #
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
    
    # Project 2 - again execute to compare numeric data #
    pro2_result=$(gcc -o "$student/project2" "$student/project2.c" && "$student/project2")
    if [ "$pro2_result" -eq 10 ]; then # full grade
    	project2_score=70
    fi
    
    # Total score #
    total=$((project1_score+project2_score))
    
    # Pass the data to the grades.txt #
    echo "$stu_name $reg_number project1: $project1_score project2: $project2_score total_grade: $total">>"$grades_location"
    
    # Check if directory exists and act accordingly #
    organized="$HOME/Desktop/organized"
    if [ "$counter" -eq 1 ]; then # we are at the first student
        if [ -d "$organized" ]; then
    	    echo "• Organized already exists and will be recreated."
    	    rm -r "$organized" # may contain files, so rm instead or rmdir
        fi
        mkdir "$organized"
        echo "• Created organized directory!"
    fi    
    
    # Move files to the directory according to user #
    read -p "Organize the files of the particular student? (y/n): " user_answer # input
    if [ "$user_answer" = "y" ]; then
    	cp "$student/project1.c" "$organized/${stu_name}_${reg_number}_project1.c"
    	cp "$student/project2.c" "$organized/${stu_name}_${reg_number}_project2.c"
    fi
done
