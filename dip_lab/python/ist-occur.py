str_input = input("Enter elements separated by commas:").split(',')
lst = [int(num) for num in str_input]
tup = tuple(lst)

print("The tuple is:", tup)

ele = int(input("Enter an element to search: "))

try:
    pos = tup.index(ele)
    print("Element position no:", pos + 1)
except ValueError:
    print("Element not found in tuple")

