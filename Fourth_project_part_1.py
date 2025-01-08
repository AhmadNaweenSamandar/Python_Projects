#First Name: Ahmad Naween
#Last Name: Samandar
#ID: 300446112

###########################
#######Question 1.1
###########################


def number_divisible(numbers, n):
    """
    The function take list components as numbers and n as divisor, it will
    divide list components on n and return the divisble number. The second part
    pop up input question for user, that way it gets the numbers and n
    """
    count = 0  # It initializes a counter to count elements divisible by n
    for number in numbers:
        if number % n == 0:  # It checks if the number is divisible by n
            count += 1       # It increments the counter if divisible
    return count  


def main():
    # It prompts the user to enter a list of numbers separated by space
    raw_input = input("Please input a list of numbers separated by space: ").strip().split()
    
    # It converts each item in raw_input from string to integer and store in a new list
    numbers = [int(num) for num in raw_input]
    
    # It prompts the user to enter a single integer for n
    n = int(input("Please input an integer to divide by: "))
    
    # It calls the number_divisible function and store the result
    result = number_divisible(numbers, n)
    
    print("The number of elements divisible by", n, "is:", result)


main()
