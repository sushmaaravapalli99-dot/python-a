balance = 5000

amount = int(input("Enter amount: "))
choice = input("Enter deposit or withdraw: ")

if choice == "deposit":
    balance = balance + amount
elif choice == "withdraw" and amount <= balance:
    balance = balance - amount
else:
    print("Invalid transaction")

print("Balance =", balance)