rows = int(input("Enter the Number of rows:"))
columns = int(input("Enter the Number of columns:"))

print("Enter the elements of First Matrix:")
matrix_a = [[int(input()) for j in range(columns)] for i in range(rows)]

print("First Matrix is:")
for n in matrix_a:
    print(n)

print("Enter the elements of Second Matrix:")
matrix_b = [[int(input()) for j in range(columns)] for i in range(rows)]

print("Second Matrix is:")
for n in matrix_b:
    print(n)

result = [[0 for j in range(columns)] for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("The sum of the above two Matrices is:")
for r in result:
    print(r)

