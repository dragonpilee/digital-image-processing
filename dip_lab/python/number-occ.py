lst = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Given list is:", lst)

number = int(input('Enter the number you want to check the occurrence in the list:'))
occur = lst.count(number)
print('Number of occurrences of', number, 'is', occur)

