# # Counting the frequencies in a list using a dictionary in Python.
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 :1 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

def count_frequencies(lst):
    frequency_dict = {} #empty dictionary
    for item in lst:#iterates over each item(element) in the list
        if item in frequency_dict:# finds if the item exist as a key in the dictionary?
            frequency_dict[item] += 1 #increments the value of that key in the  dictionary
        else: #executes if the current item(current element) of the list doesn't exist in the dictionary
            frequency_dict[item] = 1 #Adds the current item (current element )as the key in the dictionary, the number on rhs of = means the occurence of that key in the dictionary known as the value of the key forming a key:value pair and updates the same value on the second occurence of that key in the list  using the above if condition.

    return frequency_dict #holds the created dictionary 

input_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
frequency_count = count_frequencies(input_list)
print(frequency_count)
for key,value in frequency_count.items():#iterates on each key value pair and executes the next line.
   print(f"{key}:{value}")#prints the output without space
   
    # print(key,":",value)
'''
1 : 5
5 : 2
3 : 3
4 : 3
2 : 4
prints the output with space
'''
# The frequency_count.items() method is used to get a view of the dictionary's key-value pairs, allowing you to iterate over them and print each key with its corresponding value.





