year = int(input("Year: "))
leap_year = year
year+=1
while True:
    if year % 4 != 0:
        year+=1
    elif year % 400 != 0 and year % 100 ==0:
        year+=1
    elif year % 4==0  and year % 400 !=0 and year %100 ==0:
        year+=4
    else: 
        break
print(f"The next leap year after {leap_year} is {year}")
