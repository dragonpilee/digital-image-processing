def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
