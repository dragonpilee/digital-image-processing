# Create a sample list
my_list = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", my_list)

# Append an element to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Insert an element at a specific index
my_list.insert(2, 10)
print("List after inserting 10 at index 2:", my_list)

# Remove the first occurrence of a value
my_list.remove(3)
print("List after removing the first occurrence of 3:", my_list)

# Remove an element by index and return it
popped_element = my_list.pop(3)
print("Popped element at index 3:", popped_element)
print("List after popping element at index 3:", my_list)

# Extend the list with another list
my_list.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", my_list)

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# Sort the list
my_list.sort()
print("Sorted list:", my_list)

# Count occurrences of a value
count_2 = my_list.count(2)
print("Number of occurrences of 2:", count_2)

# Find index of a value
index_5 = my_list.index(5)
print("Index of value 5:", index_5)

# Copy the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Clear the list
my_list.clear()
print("List after clearing:", my_list)
