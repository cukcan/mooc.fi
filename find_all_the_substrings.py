word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)

# Find the first occurrence of the character
while index != -1:
    # Check if there are at least three characters remaining after the index
    if len(word) - index >= 3:
        print(word[index:index+3])
    # Find the next occurrence of the character, if any
    index = word.find(char, index + 1)
