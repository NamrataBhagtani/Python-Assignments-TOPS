#Write a Python program to count the occurrences of each word in a given sentence.
def count_word_ocuurences(sentence):
    #Split the sentence into words
    words = sentence.split()
    
    #create an empty dictonery
    word_counts = {}
    
    #iterate for each word in words
    for word in words:
        #if word already exist in dictonery, increment its count
        if word in word_counts:
            word_counts[word] += 1
        #else if word in not in the dictonery, add it with count of 1
        else:
            word_counts[word] = 1
    
    return word_counts

#user input
sentence = input("Enter the sentence: ")
word_occurences = count_word_ocuurences(sentence)
print("Occurences of each word in the sentence ")
for word, count in word_occurences.items():
    print(f"{word}:{count}")