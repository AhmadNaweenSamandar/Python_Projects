#Last Name: Samandar
#First Name: Ahmad Naween
#ID: 300446112


###############################
###### Question 2.1
###############################

print("Question 2.1")

def sum_odd_divisors(n):
    """
    I defined the function as sum_odd_function with a variable n. first if it equal one
    the result will be none. further to identify range from 1 to n for input I used i and abs(n) of n
    where it deal with negative numbers as well then add it with 1. In if condition (n%i == 0) identify
    if digit is devisble and i % 2 != 2 identify whether it's odd number
    """
    # It returns None if n is 0
    if n == 0:
        return None
    
    # It initializes the sum to 0
    total_sum = 0
    
    # It iterates over all numbers from 1 to |n| (absolute value of n)
    for i in range(1, abs(n) + 1):
        # It checks if i is an odd divisor of n
        if n % i == 0 and i % 2 != 0:
            total_sum += i
    
    return total_sum

print('>>> sum_odd_divisors(-9)')
print(sum_odd_divisors(-9))
print('>>> sum_odd_divisors(1)')
print(sum_odd_divisors(1))
print('>>> sum_odd_divisors(2)')
print(sum_odd_divisors(2))
print('>>> sum_odd_divisors(3)')
print(sum_odd_divisors(3))
print('>>> sum_odd_divisors(7)')
print(sum_odd_divisors(7))
print('>>> sum_odd_divisors(-2001)')
print(sum_odd_divisors(-2001))


###############################
###### Question 2.2
###############################

print("Question 2.2")


def series_sum():
    """
    as instructed I defined the function as series_sum. In the second step n take input
    from user as integer. If the input is less than 0, the program prompt none. Other wise
    based on next line of codes it first take n numbers in k and power it to two than divide
    one on k value and add it to total_sum (1000)
    """
    # It prompts the user for a non-negative integer
    n = int(input("Please enter a non-negative integer: "))
    
    # It returns None if the input is negative
    if n < 0:
        return None
    
    # It initializes the sum with the base value 1000
    total_sum = 1000
    
    # It adds terms to the sum based on the series 1/k^2
    for k in range(1, n + 1):
        total_sum += 1 / (k ** 2)
    
    return total_sum

print('>>> series_sum()')
print(series_sum())
print('>>> series_sum()')
print(series_sum())
print('>>> series_sum()')
print(series_sum())



###############################
###### Question 2.3
###############################

print("Question 2.3")


#for question number 2.3 first I write the following code:
"""
def pell(n):
    
    if n < 0:
        return None
    
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    
    else:
        return 2 * pell(n - 1) + pell(n - 2)


print(pell(0))  
print(pell(1))  
print(pell(2))  
print(pell(3))  
print(pell(4))  
print(pell(5))  

"""
# However it dosen't prompt any number, after research in internet I found that in my case (n)cannot handle larger number since pell may have a larger input

# Therefore I add several variables to my code to make it efficient for dealing with large numbers
def pell(n):
    """
    This function is designed same as previous, what I did is that I made three new variables,
    these variable take pell(n) values from last two p values (like p(n-1) and p(n-2), it is called
    iteration method rather than using recursion method. As the value starts from n = 2, so prev_prev = 0
    and prev = 1, than current will be calculated as (current = 2 * prev + prev_prev = 2 * 1 + 0 = 2), this
    way it will take values from previous iteration of p to prevent messing us the numbers
    """
    # If n is negative, return None
    if n < 0:
        return None
    
    # Base cases for n = 0 and n = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # It uses iteration to calculate the Pell number for n > 1
    prev_prev = 0  # P0
    prev = 1       # P1
    current = 0    # It will hold Pn
    
    for i in range(2, n + 1):
        current = 2 * prev + prev_prev
        prev_prev = prev
        prev = current
    
    return current


print('>>> pell(0)')
print(pell(0))
print('>>> pell(1)')
print(pell(1))
print('>>> pell(2)')
print(pell(2))
print('>>> pell(3)')
print(pell(3))
print('>>> pell(-45)')
print(pell(-45))
print('>>> pell(6)')
print(pell(6))
print('>>> pell(1743)')
print(pell(1743))



###############################
###### Question 2.4
###############################

print("Question 2.4")

def countMembers(s):
    extraordinary_count = 0  # Initialize a counter
    """
    I designed this function very simple, there is no string code as instructed,
    I used if and elif conditional statement to identify if extraordinary numbers exist
    in input and if so it should be counted
    """
    
    # Loop through each character in the string
    for char in s:
        # It checks if the character is between 'e' and 'j'
        if 'e' <= char <= 'j':
            extraordinary_count += 1
        # It checks if the character is between 'F' and 'X'
        elif 'F' <= char <= 'X':
            extraordinary_count += 1
        # It checks if the character is a numeral between '2' and '6'
        elif '2' <= char <= '6':
            extraordinary_count += 1
        # It checks if the character is '!', ',' or '\'
        elif char == '!' or char == ',' or char == '\\':
            extraordinary_count += 1
            
    return extraordinary_count

print('>>> countMembers("\\")')
print(countMembers("\\"))
print('>>> countMembers("2\")')
print(countMembers("2\'"))
print('>>> countMembers("1\")')
print(countMembers("1\'"))
print('>>> countMembers("2aAb3?eE_13")')
print(countMembers("2aAb3?eE'_13"))
print('>>> countMembers("one, Two")')
print(countMembers("one, Two"))



###############################
###### Question 2.5
###############################

print("Question 2.5")

def casual_number(s):
    """
    The function is defined as casual_number that takes s as input, in my code I defined
    a cleaned_string as input variable to take values further. If char is not equal to ,
    the value will be added to cleaned_string, next it will convert digit to integer and
    added it in cleaned_string, if value is invalid it will return none.
    """
    # It checks if the string starts with a minus sign
    if s[0] == '-':
        is_negative = True
        s = s[1:]  # It removes the minus sign for further processing
    else:
        is_negative = False

    # It removes commas from the string
    cleaned_string = ''
    for char in s:
        if char != ',':
            cleaned_string += char  # It adds non-comma characters to the cleaned string
    
    # It checks if the cleaned string contains only digits
    if cleaned_string.isdigit():
        result = int(cleaned_string)  # It converts to integer and return
        return -result if is_negative else result  # It adds back the negative sign if necessary
    else:
        return None  # It returns None if the string doesn't represent a valid number
  # It returns None if the string doesn't represent a valid number

print('>>> casual_number("251")')
print(casual_number("251"))
print('>>> casual_number(1,aba,251")')
print(casual_number("1,aba,251"))
print('>>> casual_number("1,251")')
print(casual_number("1,251"))
print('>>> casual_number("1251")')
print(casual_number("1251"))
print('>>> casual_number("-97,251")')
print(casual_number("-97,251"))
print('>>> casual_number("-97251")')
print(casual_number("-97251"))
print('>>> casual_number("-,,,,")')
print(casual_number("-,,,,"))
print('>>> casual_number("--97,251")')
print(casual_number("--97,251"))
print('>>> casual_number("-")')
print(casual_number("-"))
print('>>> casual_number("-1,000,001")')
print(casual_number("-1,000,001"))
print('>>> casual_number("999,999,999,876")')
print(casual_number("999,999,999,876"))
print('>>> casual_number("-2")')
print(casual_number("-2"))



###############################
###### Question 2.6
###############################

print("Question 2.6")

def alienNumbers(s):
    """
    as instructed the function is defined as alienNumbers that take input as (s), as defined in tables I asign values for
    each symbol in a list called value. In return the values for all symbol that may be written in input will be sumed up
    """
    # It defines a a list with symbol-value pairs
    values = {'T': 1024, 'y': 598, '!': 121, 'a': 42, 'N': 6, 'U': 1}
    
    # It sums up the total value for each character in the string
    return sum(values[char] for char in s)


print('>>>alienNumbers("a!ya!U!NaU")')
print(alienNumbers("a!ya!U!NaU"))
print('>>>alienNumbers("aaaUUU")')
print(alienNumbers("aaaUUU"))
print('alienNumbers("")')
print(alienNumbers(""))



###############################
###### Question 2.7
###############################

print("Question 2.7")

def alienNumbersAgain(s):
    """
    as described this function is same as preivous one just with a minor difference of using
    while loop instead of any possible string method. In this function while will iterate through alll
    values of values list to recall it when the symbol are entered in input and sum it up at the end
    """
    # It defines a list with symbol-value pairs
    values = {'T': 1024, 'y': 598, '!': 121, 'a': 42, 'N': 6, 'U': 1}
    
    total = 0  
    
    # It uses a for loop to go through each character in the string s
    i = 0
    while i < len(s):
        char = s[i]  # It gets the current character
        total += values[char]  # It adds the value of the current character to the total
        i += 1  # It moves to the next character
    
    return total


print('>>>alienNumbersAgain("a!ya!U!NaU")')
print(alienNumbersAgain("a!ya!U!NaU"))
print('>>>alienNumbersAgain("aaaUUU")')
print(alienNumbersAgain("aaaUUU"))
print('alienNumbersAgain("")')
print(alienNumbersAgain(""))


###############################
###### Question 2.8
###############################

print("Question 2.8")

def encrypt(s):
    """
    I used combination of several statements to encrypt the message as described and displayed in examples at the end of questionn.
    At the beginning the function reverse the input, next an empty variable is created to store encrypt message
    with for function it will go through and combine values form both side, if middle is odd middle character will be added
    this way the output will be encrypted message. (most likely as the output of the question)
    """
    # It reverses the string
    reversed_s = s[::-1]
    
    # It initializes an empty result string
    encrypted_message = ""
    
    # It calculates the length of the reversed string
    n = len(reversed_s)
    
    # It loops through and combine characters from both ends
    for i in range(n // 2):  # It loops until the middle
        encrypted_message += reversed_s[i]  # Character from the front
        encrypted_message += reversed_s[n - 1 - i]  # Character from the back
    
    # If the length is odd, add the middle character
    if n % 2 != 0:
        encrypted_message += reversed_s[n // 2]  # It adds the middle character once
    
    return encrypted_message

print('>>> encrypt("Hello ,world")')
print(encrypt("Hello, world"))
print('>>> encrypt("1234")')
print(encrypt("1234"))
print('>>> encrypt("12345")')
print(encrypt("12345"))
print('>>> encrypt("1")')
print(encrypt("1"))
print('>>> encrypt("123")')
print(encrypt("123"))
print('>>> encrypt("12")')
print(encrypt("12"))
print('>>> encrypt("Secret Message")')
print(encrypt("Secret Message"))
print('>>> encrypt(",4r")')
print(encrypt(",'4'r"))                


###############################
###### Question 2.9
###############################

print("Question 2.9")

def oPify(s):
    """
    as instructed the function is defined as oPify which takes input as (s), the function
    mainly uses for loop and if statement. As hinted I used an empty variable result that will help
    my function to accumlate the values in for statement if two consecutive numbers are found it will be added
    to the result, next funciton will check the state of input based on alphabetic, upper and lower case
    state for specifc results as requested
    """
    if len(s) <= 1:  # It defines if the string is 1 character or empty
        return s
    
    result = ""  # It initializes an empty accumulator string
    
    # It loops through the string to check each pair of consecutive characters
    for i in range(len(s) - 1):
        first_char = s[i]     # The first character of the pair
        second_char = s[i + 1] # The second character of the pair
        
        # It adds the first character to the result
        result += first_char
        
        # It checks if both characters are alphabetic
        if first_char.isalpha() and second_char.isalpha():
            # It inserts 'O' or 'o' based on the case of the first character
            if first_char.isupper():
                result += 'O'
            else:
                result += 'o'
            
            # It inserts 'P' or 'p' based on the case of the second character
            if second_char.isupper():
                result += 'P'
            else:
                result += 'p'
    
        result += s[-1]
    
    return result

print('>>> oPify("aa")')
print(oPify("aa"))
print('>>> oPify("aB")')
print(oPify("aB"))
print('>>> oPify("ooo")')
print(oPify("ooo"))
print('>>> oPify("ax1")')
print(oPify("ax1"))
print('>>> oPify("abcdef22")')
print(oPify("abcdef22"))
print('>>> oPify("abcdef22x")')
print(oPify("abcdef22x"))
print('>>> oPify("aBCDef22x")')
print(oPify("aBCdef22x"))
print('>>> oPify("x")')
print(oPify("x"))
print('>>> oPify("123456")')
print(oPify("123456"))



###############################
###### Question 2.10
###############################

print("Question 2.10")

def nonrepetitive(s):
    """
    as instructed the function nonrepetitive take value as s, using for loop I iterate
    through lenght and characters of, I give them two names if subwords are equal it repetation
    otherwise it's true
    """
    # It iterates over all possible subword lengths from 1 up to half the length of the string
    for length in range(1, len(s) // 2 + 1):
        # It checks every position in the string where a consecutive repetition of a subword could occur
        for i in range(len(s) - 2 * length + 1):
            # It extracts two consecutive subwords of the given length
            subword1 = s[i:i+length]
            subword2 = s[i+length:i+2*length]
            # If the subwords are the same, the word is repetitive
            if subword1 == subword2:
                return False
    # If no repetition was found, the word is nonrepetitive
    return True

print('nonrepetitive("")')
print(nonrepetitive(""))
print('nonrepetitive("a")')
print(nonrepetitive("a"))
print('nonrepetitive("zrtzghtghtghtq")')
print(nonrepetitive("zrtzghtghtghtq"))
print('nonrepetitive("abcab")')
print(nonrepetitive("abcab"))
print('nonrepetitive("12341341")')
print(nonrepetitive("12341341"))
print('nonrepetitive("44")')
print(nonrepetitive("44"))




