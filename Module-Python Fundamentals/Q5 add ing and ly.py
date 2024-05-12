# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
# string is less than 3, leave it unchanged 

def add_ing(string):
    if len(string) < 3:
        new_string = string
    elif string.endswith("ing"):
        new_string = string[:-3] + "ly"
    else:
        new_string = string + "ing"
    return new_string

string_input = input("Enter a string: ")
result = add_ing(string_input)
print("Result: ", result)

