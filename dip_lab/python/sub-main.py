str_input = input("Enter a string: ")
sub_input = input("Enter a substring: ")
position = int(input("Enter the position number: "))

position -= 1  # Adjusting to Python's zero-based indexing

str_output = str_input[:position] + sub_input + str_input[position:]

print(str_output)

