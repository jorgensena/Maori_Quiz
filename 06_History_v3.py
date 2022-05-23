"""
Store the Results History in a list and print output in most recent order
Final version based on Trial 2 method
Adds break loop and checks for empty list

By Amy Jorgensen
23/05/22
"""

# Set up empty lists
all_scores = []
all_wrong = []

# get five scores - five tests with three questions
get_item = ""
while get_item != "n":
    get_item = input("Do another quiz? (y/n): ")

    if get_item == "n":
        break
    # For testing purposes always answer as int
    question_1 = int(input("What is Tahi?: "))
    question_2 = int(input("What is Rua?: "))
    question_3 = int(input("What is Toru?: "))
    print()

    num_correct = 0
    # Check answers and add any wrong answer to list
    if question_1 == 1:
        num_correct += 1
    else:
        all_wrong.append("What is Tahi?")

    if question_2 == 2:
        num_correct += 1
    else:
        all_wrong.append("What is Rua?")

    if question_3 == 3:
        num_correct += 1
    else:
        all_wrong.append("What is Toru")

    # Add score to list
    if num_correct == 3:
        all_scores.append("3/3")
    elif num_correct == 2:
        all_scores.append("2/3")
    elif num_correct == 1:
        all_scores.append("1/3")
    else:
        all_scores.append("0/3")


# Show that everything made it into the list
print()

if len(all_scores) == 0:
    print("Oops, the list is empty")
else:
    print("----Full Lists-----")
    print(all_scores)
    print(all_wrong)

    print()

    if len(all_scores) >= 3:
        print("----Most recent 3----")
        for item in range(3):
            print(all_scores[len(all_scores) - item - 1])

    else:
        print("----Newest to Oldest----")
        for item in all_scores:
            print(all_scores[len(all_scores) - all_scores.index(item) - 1])

    print()

    if len(all_wrong) == 0:
        print("All questions were answered correctly!")
    else:
        print("----Most recent wrong----")
        print(all_wrong[-1])
