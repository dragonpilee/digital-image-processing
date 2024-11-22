n = int(input("Enter the number: "))
sum_digits = 0
rev = 0

while n != 0:
    digit = n % 10
    sum_digits = sum_digits + digit
    rev = rev * 10 + digit
    n = n // 10

print("Sum of digits =", sum_digits)
print("Reverse of the number:", rev)

