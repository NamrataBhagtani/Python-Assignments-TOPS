# Write a Python function that takes a list and returns a new list with unique elements

def get_unique_elements(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements_set = set(input_list)
    # Convert the set back to a list
    unique_elements_list = list(unique_elements_set)
    # Return the list with unique elements
    return unique_elements_list

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = get_unique_elements(input_list)
print(f"Original list: {input_list}")
print(f"List with unique elements: {unique_list}")
