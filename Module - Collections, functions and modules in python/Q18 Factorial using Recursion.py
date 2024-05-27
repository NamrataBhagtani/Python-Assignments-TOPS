# Python Program to Find Factorial of Number Using Recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Example usage
number = 5  # You can change this value to test with other numbers
result = factorial(number)
print(f"The factorial of {number} is {result}")

'''
Function Definition:

The function factorial is defined with a parameter n.
Base Case:

If n is 0 or 1, the function returns 1 because the factorial of 0 and 1 is 1.
Recursive Case:

If n is greater than 1, the function returns n multiplied by the factorial of n-1. This is the recursive step where the function calls itself with a decremented value of n.
Example Usage:

An example is given with the number 5. The program calculates the factorial of 5 and prints the result.

'''