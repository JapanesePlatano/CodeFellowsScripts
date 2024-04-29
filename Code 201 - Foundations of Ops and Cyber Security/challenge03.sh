#!/bin/bash

# Script Name:                  To show login history
# Author:                       Gilbert Collado
# Date of latest revision:      02/21/2024
# Purpose:                      To show login history

print_login_history() {
    # Use the 'last' command to retrieve login history
    login_history=$(last)

    # Print the login history
    echo "$login_history"
    echo "This is the login history"
}

# Calling the login history function
print_login_history
print_login_history
print_login_history

# End