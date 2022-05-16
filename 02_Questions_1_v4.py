"""
Create the first set of questions (Maori to an integer)

By Amy Jorgensen
10/05/22
"""

import random


# integer checker
def int_checker(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer number")


# Maori numbers
maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Whā", 4], ["Rima", 5],
           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

# Ask questions (assume input is integer for testing purposes)
print("Answer the following Maori numbers as an integer")
# shuffle the question list into a random order
random.shuffle(maori_q)
for question in maori_q:
    answer = int_checker(f"What is {question[0]}? \n")

    # Check answer and print output
    if answer == question[1]:
        print("Yay! You got it correct :)")
    else:
        print("Oops! That was incorrect :(")
