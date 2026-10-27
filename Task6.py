n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input("Enter subject marks: "))
    marks.append(m)

    if m < 35 and m >= 30:
        marks[i] = m + 5

    if marks[i] > 100:
        marks[i] = 100

print("Final marks:", marks)

if all(m >= 35 for m in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")

total = sum(marks)
average = total / n

print("Total marks =", total)
print("Average =", average)