n = int(input("Enter number of passengers: "))

for i in range(n):
    age = int(input("Enter age: "))
    distance = int(input("Enter distance: "))
    travel_class = input("Enter class (sleeper/AC): ")

    if distance <= 100:
        fare = distance * 1
    elif distance <= 500:
        fare = 100 + (distance - 100) * 1.5
    else:
        fare = 700 + (distance - 500) * 2

    if travel_class == "AC":
        fare = fare * 2

    if age < 12:
        fare = fare * 0.5
    elif age >= 60:
        fare = fare * 0.8

    fare = fare + 50
    print("Ticket fare =", fare)

    cancel = input("Cancel ticket? (yes/no): ")
    if cancel == "yes":
        print("Refund =", fare * 0.8)