# Write a Python program to square the elements of a list using map() function.



# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]
numbers = [4, 5, 2, 9]

# Define a lambda function to square a given number
square = lambda x: x**2

# Use map() 
squared_numbers = list(map(square, numbers))

#  original and squared lists
print("Original numbers:", numbers)
print("Square of list numbers:", squared_numbers)


