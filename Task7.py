attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
target = int(input("Enter required attendance percentage: "))

percentage = attended / total * 100
print("Current attendance =", percentage, "%")

if percentage >= target:
    print("Already eligible")
else:
    needed = 0

    while (attended + needed) / (total + needed) * 100 < target:
        needed = needed + 1

    print("Classes needed =", needed)