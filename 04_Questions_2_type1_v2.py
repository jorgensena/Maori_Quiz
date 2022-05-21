"""
Create the second set of questions (Integer to Maori)
This method gets the user to input the answer which means spelling has to
be correct

By Amy Jorgensen
13/05/22
"""
import random


# get next question so it is random but does not repeat
def get_next(q_list, q_num):
    num = random.choice(q_num)
    q_num.remove(num)
    # return random question and new number list
    return q_list[num], q_num


# Maori numbers
maori_q = [["Tahi", 1], ["Rua", 2], ["Toru", 3], ["Wha", 4], ["Rima", 5],
           ["Ono", 6], ["Whitu", 7], ["Waru", 8], ["Iwa", 9], ["Tekau", 10]]
# potential question position
q_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ask questions (questions are in order 1-10 for testing purposes)
print("Answer the following integers as a Maori number, e.g. 0 is Kore")

# loop 10 times for testing purposes (would be initiated by button press in
# final program)
for i in range(10):
    # get next question without using a for loop
    question, q_num_list = get_next(maori_q, q_num_list)
    # print(q_num_list)
    # print(question)
    # ask question
    answer = input(f"What is {question[1]}? \n").title()

    # Check answer and print output
    if answer == question[0]:
        print("Yay! You got it correct :)")
    else:
        print("Oops! That was incorrect :(")
