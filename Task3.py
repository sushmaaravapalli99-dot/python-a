distance = int(input("Enter distance in km: "))
age = int(input("Enter age: "))

fare = distance * 2

if age < 12:
    fare = fare / 2

print("Railway fare =", fare)