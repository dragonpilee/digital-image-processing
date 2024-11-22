def multiply_numbers(numbers):
    """
    Multiplies all the numbers in a list.

    Parameters:
    numbers (list of int/float): The list of numbers to be multiplied.

    Returns:
    int/float: The product of all the numbers in the list.
    """
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage:
if __name__ == "__main__":
    numbers = [2, 3, 4, 5]
    product = multiply_numbers(numbers)
    print("Product of numbers:", product)
