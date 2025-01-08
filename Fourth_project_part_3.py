#First Name: Ahmad Naween
#Last Name: Samandar
#ID: 300446112

########################
##### Question 1.3
########################

def longest_run(numbers):
    if not numbers:
        return 0  
    
    max_run_length = 1  # It tracks the longest run found
    current_run_length = 1  # It tracks the current run length
    
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:  # It checks if current number is the same as the previous
            current_run_length += 1  # It increases the current run length
        else:
            # It updates the maximum run length if the current run is longer
            if current_run_length > max_run_length:
                max_run_length = current_run_length
            current_run_length = 1  # It resets the current run length

    # Final check to ensure the longest run is recorded
    if current_run_length > max_run_length:
        max_run_length = current_run_length
    
    return max_run_length


def main():
    # It prompts  user to enter a list of numbers separated by space
    raw_input = input("Please input a list of numbers separated by space: ").strip().split()
    
    # It converts each item in raw_input from string to float and store in a new list
    numbers = [float(num) for num in raw_input]
    
    # It calls the longest_run function and store the result
    result = longest_run(numbers)
    
    
    print("The length of the longest run is:", result)

main()
