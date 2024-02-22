#!/bin/bash

# Script Name:                  Ops Challenge - Arrays
# Author:                       Gilbert Collado
# Date of latest revision:      02/21/2024
# Purpose:                      To learn how to do arrays
# Source                        https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays

# Create four directories
mkdir mangu tostones sancocho  moro

# Put the names of the four directories in an array
directories=("mangu" "tostones" "sancocho" "moro")

# Reference the array variable to create a new .txt file in each directory
for dir in "${directories[@]}"; do
    touch "$dir/dominicanfood.txt"
done

echo "Script executed successfully!"
