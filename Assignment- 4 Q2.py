# Write a Python program to triple all numbers of a given list of integers. Use Python map.



# sample list: [1, 2, 3, 4, 5, 6, 7]



# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]

numbers = [1, 2, 3, 4, 5, 6, 7]


triple = lambda x: x * 3

tripled_numbers = list(map(triple, numbers))

# Print the original and tripled lists
print("Original numbers:", numbers)
print("Triple of list numbers:", tripled_numbers)
