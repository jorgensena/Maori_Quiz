"""
Create the second set of questions (Integer to Maori)
This method gets the user to input the answer which means spelling has to
be correct

By Amy Jorgensen
13/05/22
"""

# Maori numbers
maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Wha", 4], ["Rima", 5],
           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]

# Ask questions (questions are in order 1-10 for testing purposes)
print("Answer the following integers as a Maori number, e.g. 0 is Kore")
for question in maori_q:
    answer = input(f"What is {question[1]}? \n").title()

    # Check answer and print output
    if answer == question[0]:
        print("Yay! You got it correct :)")
    else:
        print("Oops! That was incorrect :(")
