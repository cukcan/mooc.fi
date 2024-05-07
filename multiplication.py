number = int(input("Please type in a number: "))

# Initialize variables for the first operand and the second operand
i = 1

# Outer loop for the first operand
while i <= number:
    j = 1  # Reset the second operand for each iteration of the outer loop
    # Inner loop for the second operand
    while j <= number:
        # Print the multiplication operation
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
