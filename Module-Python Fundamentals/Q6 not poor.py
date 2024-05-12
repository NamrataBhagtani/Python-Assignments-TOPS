#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string
def replace_not_poor(string):
    #find returns -1 if the substring isnt found in the string
    index_not = string.find('not') 
    index_poor  = string.find('poor')
    
    
    # Check if 'not' appears before 'poor' and if both substrings are found
    #The index index_not + 3 ensures that we skip over the characters 'not' and include all characters after 'poor'. 
    if index_not != -1 and index_not != -1 and index_not > index_poor:
        new_string =  string[:index_poor]+'good'+string[index_not + 3:]
    else:
        return string    
    return new_string
input_string = input("Enter a string: ")
result = replace_not_poor(input_string)
print("Result: ", result)