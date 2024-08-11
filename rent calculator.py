rent = float(input("Enter your hostel/flat rent = "))
food = float(input("Enter the amount of food ordered = "))
electricity_spend = float(input("Enter the electricity spend = "))
charge_per_unit = float(input("Enter the charge per unit = "))
persons = float(input("Enter the number of persons living in room/flat = "))
total_bill = electricity_spend * charge_per_unit
print("The total bill is = ", total_bill)

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)