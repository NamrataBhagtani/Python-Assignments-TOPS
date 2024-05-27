#Write a Python program to convert a list of tuples into a dictionary
def list_of_tuples_to_dict(tuples_list):
    """
    Converts a list of tuples into a dictionary.

    Parameters:
    tuples_list (list of tuples): The list of tuples to convert.

    Returns:
    dict: A dictionary with the first elements of the tuples as keys
          and the second elements as values.
    """
    return {key:value for key, value in tuple_list}

tuple_list = { (1, 'a'),(2, 'b'),(3, 'c'),(4, 'b')}
result_dict = list_of_tuples_to_dict(tuple_list)


print(result_dict)