#Write a Python program to find the highest 3 values in a dictionary.
dict_1 = {40:'n1', 50:'n2', 80:'n3', 55:'n4'}

result  = sorted(dict_1.items(), key = lambda x: x[1], reverse = True)
# result = {k:v for k,v in sorted(dict_1.items(), key = lambda item:item[1])} sorting method when the dictionary is in having string value : integer key
print(f"Original dictionary: {result}")
print(f"The higest 3 values of the dictonery is {result[1:]}")

#x[0] : prints dscending order of dictionary
#x[1]: prints ascending order of dictionary
