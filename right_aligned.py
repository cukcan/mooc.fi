string = input("Please type in a string: ")

# Check if the length of the string is less than 20
if len(string) < 20:
    # Calculate the number of "*" characters needed
    num_stars = 20 - len(string)
    # Prepend the "*" characters to the string
    string = "*" * num_stars + string

print(string)
