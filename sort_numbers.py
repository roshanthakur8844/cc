#  Sorting Numbers in Python
numbers_str = input("Enter numbers separated by spaces: ")

# Convert string input to a list of integers
num_list = [int(x) for x in numbers_str.split()]

# Sort the list
num_list.sort()

print("Sorted List:", num_list)
