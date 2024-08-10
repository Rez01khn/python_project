menu = {
    'pizza': 500,
    'Pasta': 300,
    'Burger': 400,
    'Salad': 700,
    'Coffee': 120,
}
print("Welcome to Restaurant ")
print("Pizza: Rs500\nPasta: Rs300\nBurger: Rs400\nSalad: Rs700\nCoffee: Rs120")

order_total = 0

item1 = input("Enter the name of the item you want to order: ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"order item {item1} is not available yet! ")

another_order = input("Do you want to need anything else: ")
if another_order == "yes":
    item2 = input("Enter the name of the item you want to order: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Ordered item {item2} has been added to your order")
    else:
        print(f"ordered item {item2} is not available ")
print(f"The total amount of items to pay is {order_total} ")
