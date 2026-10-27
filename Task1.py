marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 75 and attendance >= 75 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible")