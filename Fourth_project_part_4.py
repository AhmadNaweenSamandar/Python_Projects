#First Name: Ahmad Naween
#Last Name: Samandar
#ID: 300446112

###########################
#### Question 1.4
###########################


def read_raw(file):
    '''str->list of str
    Returns a list of strings that was stored in a file.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i] = raw[i].strip()
    return raw

def clean_up(l):
    '''list of str->list of str

    The functions takes as input a list of characters.
    It returns a new list containing the same characters as l except that
    one of each characters that appears odd number of times in l is removed
    and all the * characters are removed.

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''

    clean_board = []
    
    # It creates a dictionary to count occurrences of each character, excluding '*'
    counts = {}
    for char in l:
        if char != '*':
            counts[char] = counts.get(char, 0) + 1

    # It only adds characters with even occurrences to clean_board
    for char, count in counts.items():
        if count % 2 == 0:
            clean_board.extend([char] * count)
        else:
            clean_board.extend([char] * (count - 1))

    return clean_board


def is_rigorous(l):
    '''list of str->bool
    Returns True if every character in the list appears exactly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: You may assume that every element in the list appears even number of times
    (i.e. that the list is cleaned up by clean_up function)

    >>> is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>> is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''

    
    for char in l:
        if l.count(char) != 2:  # It checks that each character appears exactly 2 times
            return False
    return True

#main
file = input("Enter the name of the file: ")
file = file.strip()
b = read_raw(file)
print("\nBefore clean-up:\n", b)
b = clean_up(b)
print("\nAfter clean-up:\n", b)
if is_rigorous(b):
    print("\nThis list is now rigorous; it has no * and it has " + str(len(b)) + " characters.")
else:
    print("\nThis list has no * but is not rigorous and it has " + str(len(b)) + " characters.")
