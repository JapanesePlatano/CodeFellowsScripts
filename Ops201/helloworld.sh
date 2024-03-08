#!/bin/bash

# Script Name:                  Platano
# Author:                       Gilbert Collado
# Date of latest revision:      02/20/2024
# Purpose:                      Educational

# Declaration of variables
food="mangu"
color="brown"

# Declaration of functions
display_info() {
    echo "Food: $1"
    echo "Color: $2"
}

# Main
echo "Better than mashed potatoes!"

# Accessing Variables
echo "$food is $color."

# Calling a function
display_info "$food" "$color"

# End
