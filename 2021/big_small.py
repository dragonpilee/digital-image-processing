def find_max_min(numbers):
    """
    Find the maximum and minimum elements in a list.

    Parameters:
    numbers (list of int/float): The list of numbers.

    Returns:
    tuple: A tuple containing the maximum and minimum elements.
    """
    if not numbers:
        return None, None

    max_num = min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    num_list = []

    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        num_list.append(num)

    max_num, min_num = find_max_min(num_list)

    if max_num is not None and min_num is not None:
        print("The biggest element in the list is:", max_num)
        print("The smallest element in the list is:", min_num)
    else:
        print("List is empty.")
