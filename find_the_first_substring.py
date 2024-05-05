word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)

if index >= 0 and index <= len(word)-3:
    print(word[index:index+3])
