# Script Name:                  Ops Challenge - Python Collections
# Author:                       Gilbert Collado
# Date of latest revision:      04/03/2024
# Purpose:                      Create a python that create lists
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-08/challenges/DEMO.md
# Source2:                      https://g.co/gemini/share/46e70ab57b4a      

#!/usr/bin/env python3

# Assign a list of ten dish names to a variable
dishes_list = ["pasta", "sushi", "pizza", "steak", "curry", "burger", "soup", "salad", "tacos", "lasagna"]

# Print the fourth dish in the list
print("Fourth dish in the list:", dishes_list[3])

# Print the sixth through tenth dishes in the list
print("Sixth through tenth dishes in the list:", dishes_list[5:])

# Change the value of the seventh dish to "onion soup"
dishes_list[6] = "onion soup"

# Print the updated list of dishes
print("Updated list of dishes:", dishes_list)
