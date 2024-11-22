def print_multiplication_table(number):
    """
    Print the multiplication table of the given number.
    """
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Get the number from the user
number = int(input("Enter the number to print its multiplication table: "))

# Print the multiplication table
print_multiplication_table(number)
