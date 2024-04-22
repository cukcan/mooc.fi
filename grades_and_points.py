points = int(input("How many points [0-100]:"))

if points < 0 or points > 100:
    print("Grade: impossible!")
elif 0 < points < 50:
    print("Grade: fail")
elif 49 < points < 60:
    print("Grade: 1")
elif 59 < points < 70:
    print("Grade: 2")
elif 69 < points < 80:
    print("Grade: 3")
elif 79 < points < 90:
    print("Grade: 4")
elif 89 < points < 101:
    print("Grade: 5")
