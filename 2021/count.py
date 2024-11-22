def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    uppercase, lowercase = count_upper_lower(input_string)

    print("Number of uppercase letters:", uppercase)
    print("Number of lowercase letters:", lowercase)
