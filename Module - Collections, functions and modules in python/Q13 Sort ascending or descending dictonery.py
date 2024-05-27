#Write a Python program to sort a dictionary (ascending /descending) by value.
dict_1 = {'n1':2, 'n2':4, 'n3':1, 'n4':3}

result = {k:v for k,v in sorted(dict_1.items(), key = lambda item:item[1])}

print(f"The sorted dictonery is {result}")

'''
 1.`dict_1.items()`: This retrieves all the key-value pairs from the dictionary `dict_1`.

2. `sorted(dict_1.items(), key=lambda item: item[1])`: This sorts the key-value pairs based on the values (`item[1]`). 
The `key` parameter in the `sorted()` function takes a function that defines the sorting criteria. 
Here, `lambda item: item[1]` is an anonymous function (lambda function) 
that extracts the second element (the value) of each key-value pair for sorting.

3.`{k: v for k, v in ...}`: This is a dictionary comprehension. It iterates over 
each sorted key-value pair (represented as `k, v`) and creates a new dictionary 
where the keys and values remain the same.
So, overall, `result` will be a new dictionary containing the same key-value pairs as `dict_1`, 
but the pairs will be sorted based on their values in ascending order.
'''

'''
dict_1 = {40: 'n1', 50: 'n2', 80: 'n3', 55: 'n4'}
sorted_dict = dict(sorted(dict_1.items()))
print(sorted_dict)

This will output:

{40: 'n1', 50: 'n2', 55: 'n4', 80: 'n3'}


'''