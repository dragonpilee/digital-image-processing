def convert(num):
    if num > 1:
        convert(num // 2)
    print(num % 2, end=' ')

n = int(input("Enter a number: "))
convert(n)
print(" is binary equivalent of", n)

