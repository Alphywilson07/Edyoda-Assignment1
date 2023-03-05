# Python program to reverse a string 


str = 'Edyoda'

# find reverse of string
reverse = ''
for i in range(len(str), 0, -1):
   reverse += str[i-1]

# print reverse of string
print('The reverse string is', reverse)

