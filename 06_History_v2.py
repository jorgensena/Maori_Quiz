"""
Store the Results History in a list and print output in most recent order
Trial #2 - print lists in reverse order

By Amy Jorgensen
23/05/22
"""

# Set up empty lists
all_scores = []
all_wrong = []

# get five scores - five tests with three questions
for i in range (5):
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
print("----Full Lists-----")
print(all_scores)
print(all_wrong)

print()

print("----Most recent 3----")
for item in range(3):
    print(all_scores[len(all_scores) - item - 1])

print()
print("----Most recent wrong----")
print(all_wrong[-1])
