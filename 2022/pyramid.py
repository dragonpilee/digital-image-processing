def print_pyramid(rows):
    """
    Print a pyramid of numbers.
    """
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="")
        
        # Print left half of the pyramid
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print right half of the pyramid
        for k in range(i - 1, 0, -1):
            print(k, end="")
        
        # Move to the next line
        print()

# Get the number of rows from the user
rows = int(input("Enter the number of rows for the pyramid: "))

# Call the function to print the pyramid
print_pyramid(rows)
