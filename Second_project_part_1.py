import math
import random

# Function to solve elementary school quiz
def elementary_school_quiz(flag, n):
    # I write elementary_school_quiz function here 
    # my code include  dosctrings and the body of the function
    correct_answers = 0

    for ch in range(n):
        #Generate a random number
        #I took this code from random library (random.randit()
        random_number = random.randint(0, 10)
        #Preconditions: flag is 0 or 1, n is 1 or 2
        if flag == 0:
            answer = 2 ** random_number
            print(f"Question {ch + 1}:")
            #I used ch+1 here to print the question numbers according to elementary_school_functions numbers
            question = f"2 to what is {answer}? i.e. what is the result of log_2({answer})?"
        elif flag == 1:
            question = f"Question {ch + 1}: What is the result of 2^{random_number}?"
        else:
            return 0

        pupil_answer = input(question + " ")

        if flag == 0:
            correct_answer = random_number
        else:
            correct_answer = 2 ** random_number

        if int(pupil_answer) == correct_answer:
            correct_answers += 1

    return correct_answers

# Function to solve the quadratic equation for high school quiz
def high_school_quiz(a, b, c):
    # I write high_school_quiz function here 
    # my code include  dosctrings and the body of the function
    print(f"The quadratic equation {a}·x^2 + {b}·x + {c} = 0")

    # here I have created the delta function as follows:
    delta = b**2 - 4*a*c
    
    # Following if function will handle different cases based on the delta
    if a == 0:
        if b != 0:
            print(f"The linear equation {b}·x + {c} = 0 has the solution: {-c / b}")
        else:
            if c == 0:
                print("The equation is satisfied for all numbers x.")
            else:
                print("The equation is satisfied for no number x.")
    else:
        if delta > 0:
            root1 = (-b + math.sqrt(delta)) / (2*a)
            root2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"The equation has two real roots: {root1} and {root2}")
        elif delta == 0:
            root = -b / (2*a)
            print(f"The equation has one real root: {root}")
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(-delta) / (2*a)
            print(f"The equation has two complex roots: {real_part} + i {imaginary_part} and {real_part} - i {imaginary_part}")

# Function to display greetings surrounded with stars
def display_greeting(message):
    print("*" * (len(message) + 6))
    print(f"*  {message}  *")
    print("*" * (len(message) + 6))

# Main part of the program
def main():
    display_greeting("__Welcome to my math quiz-generator__")

    name = input("What is your name? ")

    status = input(f"Hi {name}. Are you in? Enter\n1 for elementary school\n2 for high school\n3 or other character(s) for none of the above?\n")

    if status == '1':
        display_greeting(f"__{name}, welcome to my quiz-generator for elementary school students.__")
        flag = int(input(f"{name}, what would you like to practice? Enter\n0 for inverse of exponentiation\n1 for exponentiation\n"))

        if flag not in [0, 1]:
            print("Invalid choice. Only 0 or 1 is accepted.")
            print(f"Good bye {name}!")
            return

        n = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))

        if n not in [0, 1, 2]:
            print("Only 0, 1, or 2 are valid choices for the number of questions.")
            print(f"Good bye {name}!")
            return

        if n == 0:
            print(f"Zero questions. OK. Good bye {name}!")
            return

        correct_answers = elementary_school_quiz(flag, n)
        if correct_answers == n:
            print(f"Congratulations {name}! You'll probably get an A tomorrow.")
        elif correct_answers == n // 2:
            print(f"You did ok {name}, but I know you can do better.")
        else:
            print(f"I think you need some more practice {name}.")
        print(f"Good bye {name}!")

    elif status == '2':
        display_greeting(f"__quadratic equation solver for {name}__")
        
        flag = True
        while flag:
            question = input(f"{name}, would you like a quadratic equation solved? ").strip().lower()

            if question != "yes":
                flag = False
            else:
                print("Good choice!")
                a = float(input("Enter a number for the coefficient a: "))
                b = float(input("Enter a number for the coefficient b: "))
                c = float(input("Enter a number for the coefficient c: "))
                high_school_quiz(a, b, c)

        print(f"Good bye {name}!")

    else:
        print(f"{name}, you are not a target audience for this software.")
        print(f"Good bye {name}!")

# Call the main function to start the program
main()
