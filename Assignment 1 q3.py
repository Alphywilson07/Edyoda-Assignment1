'''Write a Python program to count the number of even and odd numbers from a series of numbers.



Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

Expected Output :

Number of even numbers : 4

Number of odd numbers : 5'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
even_count= 0
odd_count = 0
 
# Seperating odds and evens and acquiring their quantities
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)