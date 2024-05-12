#Write a Python program to check whether a list contains a sublist.
Alist = ['apple',1,'orange',2,'mango']
sublist = [1,2]

print("Main List: ", Alist)
print("Given sublist: ", sublist)

# It uses a generator expression (x in Alist for x in sublist) inside the all() function to check if each element x in sublist is present in Alist.
# The all() function in Python returns True if all elements in an iterable are truthy (i.e., they evaluate to True when converted to a Boolean value). If any element in the iterable is falsy, all() returns False.
# syntax = all(iterable)
# example
# # Check if all elements in a list are greater than zero
# numbers = [1, 2, 3, 4, 5]
# print(all(x > 0 for x in numbers))  # Output: True

# # Check if all elements in a list are even
# numbers = [2, 4, 6, 8, 9]
# print(all(x % 2 == 0 for x in numbers))  # Output: False, because 9 is not even
# The all() function is commonly used with generator expressions, list comprehensions, and other iterables to check if all elements satisfy a certain condition.
if (all(x in Alist for x in sublist)):
    print("Main list contains sublist")
else:
    print("Main list doesn't contains the sublist")
    
    
    