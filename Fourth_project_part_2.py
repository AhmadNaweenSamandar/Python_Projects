#First Name: Ahmad Naween
#Last Name: Samandar
#ID: 300446112

#####################
###### Question 1.2
#####################




def two_length_run(numbers):
    """
    This function has two parts, the_length_run takes values as numbers and see if
    at least one run of length two (one digit with at least with two times written) exist
    in the list, if it does it prints true otherwise false.
    """
    for i in range(len(numbers) - 1):  # It loops through the list, stopping at the second-last element
        if numbers[i] == numbers[i + 1]:  # It checks if current element is the same as the next
            return True
    return False


def main():
    # It prompts the user to enter a list of numbers separated by space
    raw_input = input("Please input a list of numbers separated by space: ").strip().split()
    
    # It converts each item in raw_input from string to float and store in a new list
    numbers = [float(num) for num in raw_input]
    
    # It calls the two_length_run function and store the result
    result = two_length_run(numbers)
    
    print("The list has a run of length at least two:", result)


main()
