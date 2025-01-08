#Last Name: Samandar
#First Name: Ahmad Naween
#Student ID: 300446112
#File: Assignment 6 part 3

def digit_sum(n):
    """
    Recursively computes the sum of all digits of a non-negative integer n.
    """
    # If n is a single-digit number (less than 10), return n directly (base case for recursion)
    if n < 10:
        return n
    # This ensures the function recursively sums all digits of the number.
    # called on the rest of the number (n // 10, which removes the last digit).
    return n % 10 + digit_sum(n // 10)

def digital_root(n):
    """
    Recursively computes the digital root of a non-negative integer n.
    The digital root is obtained by repeatedly summing the digits of n
    until a single-digit value is obtained.
    """
    # Base case: If n is a single-digit number (less than 10), return n as it is already the digital root.  

    if n < 10:
        return n
    # Recursive case: Calculate the sum of the digits of n using digit_sum, then recursively call digital_root 
    # on the resulting sum to reduce it to a single digit. 
    return digital_root(digit_sum(n))

# I tasted the function with question examples
print(digit_sum(69701))  # Should print 23
print(digital_root(1969))  # Should print 7

