# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

def sum_list_numbers(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
my_list = [8, 2, 3, 0, 7]
total = sum_list_numbers(my_list)
print(total)








