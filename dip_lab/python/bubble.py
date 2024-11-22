x = []
print('How many elements? ', end='')
n = int(input())

for i in range(n):
    print("Enter element: ", end='')
    x.append(int(input()))

print("Original list: ", x)

flag = False

for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            # Swap elements if they are in the wrong order
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            flag = True

    if flag == False:
        # If no swaps occurred, the list is already sorted
        break
    else:
        flag = False

print("Sorted list: ", x)

