def fib(n):
    first = 0
    second = 1
    fib_series = [first, second]

    for i in range(2, n):
        third = first + second
        fib_series.append(third)
        first = second
        second = third

    return fib_series

n = int(input("Enter the number of elements: "))
print("The Fibonacci series is:")
print(fib(n))

