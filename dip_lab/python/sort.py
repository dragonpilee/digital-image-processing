strings_list = []
n = int(input("How many strings: "))

for i in range(n):
    print("Enter String:", end=" ")
    strings_list.append(input())

sorted_strings = sorted(strings_list)

print("Sorted list:")
for string in sorted_strings:
    print(string)

