menu = {
    'salad': 300,
    'pepe': 60,
    'apple': 90,
    'tomato': 40,
    'sag': 20,
    'meat': 600,
    'met': 800,
}
print("Welcome to my shop")
print("salad: Tk300\npepe: Tk60\napple: Tk90\ntomato: Tk40\nsag: Tk20\nbeef meat: Tk600\nmeat: Tk800")

order_tk = 0

item3 = input("Enter a name of a food you want to order:")
if item3 in menu:
    order_tk += menu[item3]
    print(f"order {item3} is redy to serve ")
else:
    print(f"order{item3} item is not available ")

another_item = input("Enter if you want to order something else:")
if another_item == 'yes':
    item4 = input("Enter a name of a food you want to order:")
    if item4 in menu:
        order_tk += menu[item4]
        print(f"order {item4} is also redy to serve ")
    else:
        print(f"order item {item4} is not available ")

print(f"The total amount is {order_tk}")