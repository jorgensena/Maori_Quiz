"""
Create the first set of questions (Maori to an integer)

By Amy Jorgensen
09/05/22
"""

import random


# Maori numbers
maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Whā", 4], ["Rima", 5],
           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

# Ask questions (assume input is integer for testing purposes)
print("Answer the following Maori numbers as an integer")
# shuffle the question list into a random order
random.shuffle(maori_q)
for question in maori_q:
    answer = int(input(f"What is {question[0]}? \n"))

    # Check answer and print output
    if answer == question[1]:
        print("Yay! You got it correct :)")
    else:
        print("Oops! That was incorrect :(")
