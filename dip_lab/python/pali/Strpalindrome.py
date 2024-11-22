def palindrome(string):
    string = string.lower()  # Convert the string to lowercase for case-insensitive comparison
    strrev = ""

    for i in string:
        strrev = i + strrev

    if string == strrev:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Example usage:
input_string = input("Enter a string: ")
palindrome(input_string)

