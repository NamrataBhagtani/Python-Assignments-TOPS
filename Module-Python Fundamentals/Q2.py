#Write a Python program to count occurrences of a substring in a string
main_string = input("Enter the string: ")
substring = input("Enter the substring you want to count in the above string: ")
def count_substring_occurences(main_string, substring):
    count = main_string.count(substring)
    return count

occurences = count_substring_occurences(main_string, substring)
print("Number of {} in {}: {}".format(substring, main_string, occurences))