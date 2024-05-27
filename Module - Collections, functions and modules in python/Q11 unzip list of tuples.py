#Write a Python program to unzip a list of tuples into individual lists.
def unzip_tuples(tuples_list):
    unzipped_lists = list(zip(*tuples_list))
    
    return [list(t) for t in unzipped_lists]

tuples_list = [(1,'a','Apple'), (2,'b','Bat'),(3,'c','Cat')]
unzipped_lists = unzip_tuples(tuples_list)

for i,lst in enumerate(unzipped_lists):
    print(f"List {i + 1}:{lst}")