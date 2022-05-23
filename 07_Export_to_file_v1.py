"""
Export the lists to .txt file

By Amy Jorgensen
23/05/22
"""
# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# Assume valid data for now
filename = input("Enter a filename: ")

# Create file to hole data
f = open(filename, "w+")

for item in data:
    f.write(item)

# close file
f.close()
