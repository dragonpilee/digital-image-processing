def factorial(n):
    """
    Calculate the factorial of a number using recursive function.

    Parameters:
    n (int): The number for which factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print("Factorial of", num, "is", fact)
