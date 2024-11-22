# Create File sample1.txt
with open("sample1.txt", "a") as f:
    f.write("Welcome")

# Read and print content of sample1.txt
with open("sample1.txt", "r") as f:
    print(f.read())

# Create File sample2.txt
with open("sample2.txt", "a") as f:
    f.write("Good morning")

# Read and print content of sample2.txt
with open("sample2.txt", "r") as f:
    print(f.read())

# Append content of sample1.txt to sample2.txt
with open("sample1.txt", "r") as f1:
    content = f1.read()

with open("sample2.txt", "a") as f2:
    f2.write(content)

# Read and print the updated content of sample2.txt
with open("sample2.txt", "r") as f2:
    print(f2.read())

