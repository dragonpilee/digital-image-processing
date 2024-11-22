def rgb_to_cmy(r, g, b):
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    return (c, m, y)

try:
    r = int(input("Enter the red value (0-255): "))
    g = int(input("Enter the green value (0-255): "))
    b = int(input("Enter the blue value (0-255): "))

    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("RGB values must be in the range 0-255.")

    cmy_values = rgb_to_cmy(r, g, b)
    print("CMY values:", cmy_values)

except ValueError as e:
    print(f"Error: {e}. Please enter valid integer values for RGB.")

