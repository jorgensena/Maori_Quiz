"""
Create the second set of questions (Integer to Maori)
This method gets the user to input the answer from a list so spelling does
not matter

By Amy Jorgensen
13/05/22
"""
import random


# Maori numbers
maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Wha", 4], ["Rima", 5],
           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]
# multi choice options
multi_choice = ["A", "B", "C", "D"]

# Ask questions (questions are in order 1-10 for testing purposes)
print("Answer the following integers as a Maori number, e.g. 0 is Kore")
for question in maori_q:
    # remove the answer from the list
    maori_q.remove(question)
    # get 3 random numbers to set as the other choices
    choices = random.sample(maori_q, 3)
    # print()
    # print(choices)
    # print(question)
    # add the question to the multi choice list
    choices.append(question)

    # shuffle the choices list so the choices are in a random order
    # e.g. so that A isn't always the correct
    random.shuffle(choices)
    A = choices[0][0]
    B = choices[1][0]
    C = choices[2][0]
    D = choices[3][0]

    # find which one is the answer
    if A == question[0]:
        answer = "A"
    elif B == question[0]:
        answer = "B"
    elif C == question[0]:
        answer = "C"
    else:
        answer = "D"

    # ask question
    print()
    print(f"What is {question[1]}?")
    # print multi choice answers
    print(f"A) {A}"
          f"\nB) {B}"
          f"\nC) {C}"
          f"\nD) {D}")
    user_answer = input("Your answer: ").title()

    # put the question back into the number list
    maori_q.insert(question[1]-1, question)


    # Check answer and print output
    if user_answer == answer:
        print("Yay! You got it correct :)")
    else:
        print("Oops! That was incorrect :(")
