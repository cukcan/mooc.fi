sentence = input("Please type in a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize the index to 0
index = 0

# Continue looping until we reach the end of the list of words
while index < len(words):
    # Print the first letter of the current word
    print(words[index][0])
    # Move to the next word by incrementing the index
    index += 1
