user_age = int(input("What is your age? "))

if 0 <= user_age < 5:
    print("I suspect you can't write quite yet...")
elif user_age < 0:
    print("That must be a mistake") 
else:
    print(f"Ok, you're {user_age} years old")
