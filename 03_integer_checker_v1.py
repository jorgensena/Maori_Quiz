"""
Create the integer checker

By Amy Jorgensen
10/05/22
"""


def int_checker(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer number")


# MAIN ROUTINE
# get number
number = int_checker("Enter a number: ")
print(f"You entered {number}")

