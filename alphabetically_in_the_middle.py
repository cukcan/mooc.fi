letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter3 > letter1 > letter2 or letter2 > letter1 > letter3:
    print(f"The letter in the middle is {letter1}")
elif letter1 > letter2 > letter3 or letter3 > letter2 > letter1:
    print(f"The letter in the middle is {letter2}")
else:
    print(f"The letter in the middle is {letter3}")
