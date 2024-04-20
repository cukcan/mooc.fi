from datetime import date

# Input the target date
target_day = int(input("Enter the day: "))
target_month = int(input("Enter the month: "))

# Today's date
today = date.today()

# Target date in the current year
target_date = date(today.year, target_month, target_day)

# Calculate the difference in days
if today > target_date:
    # If the target date has already passed this year, calculate for next year
    target_date = date(today.year + 1, target_month, target_day)

days_left = (target_date - today).days

print(f"{days_left} days left until {target_date.strftime('%B')} {target_day}!")
