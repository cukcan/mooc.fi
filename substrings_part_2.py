string = input("Please type in a string: ")
b = len(string)
a = b - 1

while a >= 0:
    print(string[a:b])
    a -= 1
