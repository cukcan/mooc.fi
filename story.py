story = ""
prev_word = None

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == prev_word:
        break
    story += word + " "
    prev_word = word

print(story)
