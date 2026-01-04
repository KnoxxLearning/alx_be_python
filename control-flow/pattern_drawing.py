# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the square pattern
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()
    row += 1
