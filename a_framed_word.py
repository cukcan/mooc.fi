word = input("Word: ")

# Calculate the number of spaces needed on each side of the word
spaces = (30 - len(word) - 2) // 2

# Adjust the spacing if the length of the framed word is not 30
if len(word) % 2 != 0:
    spaces_left = spaces
    spaces_right = spaces + 1
else:
    spaces_left = spaces_right = spaces

# Construct the framed word with appropriate spacing
framed_word = "*" + " " * spaces_left + word + " " * spaces_right + "*"

# Print the frame with the framed word in the center
print("*" * 30)
print(framed_word)
print("*" * 30)
