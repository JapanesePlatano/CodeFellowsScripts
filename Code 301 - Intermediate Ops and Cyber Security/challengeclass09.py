# Script Name:                  Ops Challenge - Python Conditionals
# Author:                       Gilbert Collado
# Date of latest revision:      04/04/2024
# Purpose:                      Create a script that uses condiitionals in python
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/blob/main/class-09/challenges/DEMO.md
# Source2:                      https://g.co/gemini/share/0dbe4696314e

#!/usr/bin/env python3

# Variable Declarations
animal1 = "cat"
animal2 = "dog"

# Main

# if Statement
if animal1 == animal2:
    print("Both animals are the same.")
else:
    print("The animals are different.")

# elif statement
animal = "cat"

if animal == "dog":
    print("It's a dog!")
elif animal == "fish":
    print("It's a fish!")
elif animal == "cat":
    print("It's a cat!")
else:
    print("It's some other animal.")

# elif-else statement
animal = "cat"

if animal == "dog":
    print("It's a dog!")
elif animal == "fish":
    print("It's a fish!")
else:
    print("It's a cat or some other animal.")

