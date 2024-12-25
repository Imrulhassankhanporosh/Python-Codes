# In Python, lists are more flexible than Java arrays because they can dynamically change size.

size = int(input("Enter the size of the list : "))
summation = 0

# Declare the list with the input size (initially filled with zeros)

array = [0] * size

# Populate the list with user input

for i in range(size):
    array[i] = int(input(f"Enter the element {i + 1}: "))
    summation = summation + array[i]

# Display the list

print("Display the list elements", array, "And the summation is : ", summation)
