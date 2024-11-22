def search_string_position(main_string, substring):
    """
    Search for the position of a substring within a given string.

    Parameters:
    main_string (str): The main string to search within.
    substring (str): The substring to search for.

    Returns:
    int: The position of the substring in the main string, or -1 if not found.
    """
    return main_string.find(substring)

if __name__ == "__main__":
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to search for: ")

    position = search_string_position(main_string, substring)

    if position != -1:
        print(f"The substring '{substring}' is found at position {position}.")
    else:
        print(f"The substring '{substring}' is not found in the main string.")
