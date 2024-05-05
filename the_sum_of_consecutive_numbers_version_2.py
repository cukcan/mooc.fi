limit = int(input("Limit: "))
total = 0
calculation = "The consecutive sum: "
count = 1

while total + count <= limit:
    total += count
    calculation += str(count)
    if total < limit:
        calculation += " + "
    count += 1

# If the last number exceeds the limit, add it to the calculation string
if total < limit:
    calculation += str(count)
    calculation += f" = {total + count}"  # Update the total to include the last number
else:
    calculation += f" = {total}"

print(calculation)
