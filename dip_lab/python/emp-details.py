emp = []
n = int(input('How many employees? '))

for i in range(n):
    print('Enter id:', end=' ')
    emp.append(int(input()))
    print('Enter Name:', end=' ')
    emp.append(input())
    print('Enter Salary:', end=' ')
    emp.append(float(input()))  # Assuming salary is a float
    print('---')

print('The list is created with employee data')

id_to_find = int(input("Enter employee id:"))
found = False

for i in range(0, len(emp), 3):  # Loop with step 3 since each employee has 3 elements in the list
    if id_to_find == emp[i]:
        print('Id={}, Name={}, Salary={:.2f}'.format(emp[i], emp[i + 1], emp[i + 2]))
        found = True
        break

if not found:
    print('Employee not found.')

