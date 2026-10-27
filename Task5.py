n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/other): ")

    amount = price * qty

    if category == "food":
        amount = amount + amount * 0.05
    else:
        amount = amount + amount * 0.10

    total = total + amount
    print(name, "Amount =", amount)

discount = 0
if total >= 2000:
    discount = total * 0.10

if discount > 500:
    discount = 500

print("Total bill =", total - discount)