while True:
    string = input("Please type in a string: ")
    if string != "":
        print(string)
        print(len(string) * "-")
    else:
        break
