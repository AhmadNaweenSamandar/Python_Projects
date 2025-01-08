#Last Name: Samandar
#First Name: Ahmad Naween
#Student ID: 300446112
#File: Assignment 6 part 1

import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''

    #Prompts the user for a filename and returns the file object if successful.
    while True:
        try:
            filename = input("Enter the filename: ").strip()
            file = open(filename, 'r', encoding='utf-8')
            return file
        except FileNotFoundError:
            print("File not found. Please try again.")

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''

    #Reads the file line by line, processes the content, and returns a dictionary
    #where keys are words and values are sets of line numbers.'''
    word_dict = {}
    line_num = 1

    for line in fp:
        line = line.strip().lower()  # Lowercase the line
        words = line.split()  # Split into words
        words = remove_punctuation(words)  # Remove punctuation and preprocess
        for word in words:
            if word not in word_dict:
                word_dict[word] = set()
            word_dict[word].add(line_num)
        line_num += 1
    
    return word_dict

def remove_punctuation(words):
    '''
    Removes punctuation and filters words according to the rules.'''
    processed = []
    for word in words:
        word = word.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
        word = word.replace("'", "").replace("-", "")  # Remove apostrophes and hyphens
        if word.isalpha() and len(word) > 1:  # Keep words with only alphabetic characters and >1 length
            processed.append(word)
    return processed




def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    #Finds lines that contain all the words in the query.'''

    query_words = query.split()
    missing_words = [word for word in query_words if word not in D]
    if missing_words:
        return [], missing_words  # If any words are missing, return early

    result_set = None
    for word in query_words:
        if result_set is None:
            result_set = D[word]
        else:
            result_set = result_set.intersection(D[word])  # Find common lines

    return sorted(result_set) if result_set else [], []

##############################
# main
##############################
file = open_file()
d = read_file(file)

while True:
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query in {'q', 'Q'}:
        print("Goodbye!")
        break

    results, missing_words = find_coexistance(d, query)
    
    if missing_words:
        for word in missing_words:
            print(f"Word '{word}' not in the file.")
    elif results:
        print("The one or more words you entered coexisted in the following lines of the file:")
        print(", ".join(map(str, results)))
    else:
        print("The one or more words you entered does not coexist in a same line of the file.")
