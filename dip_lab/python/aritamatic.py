n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = int(input("Enter your choice from the above: "))

if ch == 1:
    sum_result = n1 + n2
    print("Sum =", sum_result)
elif ch == 2:
    sub_result = n1 - n2
    print("Difference =", sub_result)
elif ch == 3:
    mul_result = n1 * n2
    print("Product =", mul_result)
elif ch == 4:
    div_result = n1 / n2
    print("Quotient =", div_result)
else:
    print("Incorrect Choice")

