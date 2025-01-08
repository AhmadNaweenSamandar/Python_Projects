def split_tester(N, d):
    """
    This function takes a number N as a string and splits it into pieces of length d.
    It prints the pieces separated by commas and returns True if the sequence is strictly increasing,
    otherwise returns False.
    """
    pieces = []# here as we studied in class I created an empty variable 
    
    # as you can see by using for I iterate trough lengh of N by d
    # as function parameter N and d will be given by user
    for i in range(0, len(N), d):
        pieces.append(N[i:i+d])  # this part will slice the number in first end of i and second end i+d, example if i=0 and d=2 so it will be N[0:2]
    
    # since after iteration the elements in piece will be sperated, I used join to make element displayed in one string seperated by comma 
    print(', '.join(pieces))
    
    # Check if the sequence is strictly increasing
    for i in range(1, len(pieces)):
        if int(pieces[i]) <= int(pieces[i - 1]):  # Compare consecutive pieces
            return False  # Return False if the sequence is not strictly increasing
    
    return True  # If loop completes, return True as the sequence is strictly increasing


def print_general_wel_message(message):
    """
    This function prints a message within a box of stars, stars define the number of stars, I print stars at the top
    then define stars in three row to create start and end individual stars in message area and lastly print stars again to create
    botton row
    """
    stars = '*' * (len(message) + 6)
    print(stars)
    print(f"* {' ' * (len(message) + 2)} *")
    print(f"*   {message} *")
    print(f"* {' ' * (len(message) + 2)} *")
    print(stars)


# here I put my welcome message in star function
print_general_wel_message("__Welcome to my increasing-splits tester__")

# I asked for the user's name
name = input("What is your name? ")

# I defined personalized welcome message for name and put it in star function
welcome_message = f"__{name}, welcome to my increasing-splits tester.__"
print_general_wel_message(welcome_message)

flag = True  # I flagged to keep the loop running
while flag:
    # I asked if the user wants to test a number
    question = input(name + ", would you like to test if a number admits an increasing-split of given size? ")
    question = (question.strip()).lower()
    # as you can see I used two built-in methods for string the give ease of work and better experience as user
    # it means when a user mistakenly write a space with yes or no strip will make our work easy with if statement YES or yes will be counted as correct input
    # .lower() will accept even capital responses to this question avoiding further coding with if or other methods


    if question == 'no':
        flag = False  # Exit the loop if the user says 'no'
        goodbye_message = f"__Goodbye, {name}__!"
        print_general_wel_message(goodbye_message)  # Goodbye message with stars
    elif question == 'yes':
        print("good choice!")
        # Prompt for the number N
        N = input("Please enter a positive integer: ")
        N = (N.strip())
        if not N.isdigit():  # Check if N is a valid positive integer, it means if N is not a number or N is not bigger than zero then it print error message
            print("The input can only contain digits. Try again.")
            continue  # Go back to the start of the loop if input is invalid
        elif int(N) <= 0:
            print("The input has to be a positive integer. Try again.")
            continue
        # Prompt for the number of digits d
        d = input(f"Input the split. The split has to divide the length of {N}, i.e. {len(N)}: ")
        d = (d.strip())
        if not d.isdigit():  # same like N check for validation of d according to three parameters
            print("The input can only contain digits. Try again.")
            continue  # Go back to the start of the loop if input is invalid
        elif int(d) <= 0:
            print("The input has to be a positive integer. Try again.")
            continue
        elif len(N) % int(d) != 0:
            print(f"{d} does not divide {len(N)}. Try again")
            continue
        
        d = int(d)  # Convert d to an integer
        
        # Call split_tester and check the result
        if split_tester(N, d):
            print("The sequence is increasing.")
        else:
            print("The sequence is not  increasing.")
    else:
        print("Please enter 'yes' or 'no'. Try again.")
