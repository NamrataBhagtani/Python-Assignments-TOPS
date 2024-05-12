#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

while(True):
    def swap_first_two_chars(string1, string2):
        new_string1 = string2[:2] + string1[2:]
        new_string2 = string1[:2] + string2[2:]
        
        result = new_string1 + ' ' + new_string2
        return result
        
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string :")

    result = swap_first_two_chars(string1, string2)
    print("Result after swapping first two characters:")
    print(result)