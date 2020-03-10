total = 0
number_items = int(input("Number of items:"))
while number_items < 0:
    print("Invalid number of items")
    number = int(input("Number of items:"))
for i in range(number_items):
    price = float(input("Price of item:"))
    total = total + price
if total > 100:
    discount = total * 0.10
    total = total - discount
print("Total price for ", number_items, " items is ${:.2f}".format(total))
