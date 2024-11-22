filename = "Integers.txt"

try:
    with open(filename, "r") as f:
        sum_values = 0
        count = 0

        for line in f.readlines():
            line = line.strip()  # Remove leading and trailing whitespaces, including newlines
            if line:  # Check if the line is not empty
                count += 1
                sum_values += int(line)

        if count > 0:
            avg = sum_values / count
            print("Average of the numbers in the file:", avg)

            # Open the file in write mode to overwrite existing content
            with open(filename, "w") as f:
                f.write("Average of the above numbers is: ")
                f.write(str(avg))
        else:
            print("No numbers in the file.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except ValueError as e:
    print(f"Error: {e}")

