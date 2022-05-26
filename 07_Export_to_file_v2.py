"""
Export the lists to .txt file
Add .txt to the end of the filenames

By Amy Jorgensen
24/05/22
"""
# Data to be outputted
scores = ["1/3", "2/3", "1/3", "2/3", "3/3", "3/3"]
wrong = ["What is Tahi", "What is Rua", "What is Rua", "What is Tahi",
         "What is Toru", "What is Toru"]

# Get filename, can't be blank / invalid
# Assume valid data for now
filename1 = input("Enter a filename for the scores file: ")
filename2 = input("Enter a filename for the questions wrong file: ")

filename1 = filename1 + ".txt"
filename2 = filename2 + ".txt"

# Create file to hole data
f1 = open(filename1, "w+")
f2 = open(filename2, "w+")

for item in scores:
    f1.write(item + "\n")
for item in wrong:
    f2.write(item + "\n")

# close file
f1.close()
f2.close()
