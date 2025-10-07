## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Person leaving in room

## Output
# Total amount you've to pay is

rent = int(input("Enter your hostal rent = "))
food = int(input("Enter the amount of food ordered = "))
Electricity_spend = int(input("Enter the total of electricity spend = "))
Charge_per_unit = int(input("Enter the charge per unit = "))
Persons = int(input("Enter the number of persons living in room = "))

Total_bill = Electricity_spend * Charge_per_unit

amount_per_person = (rent + food + Total_bill) / Persons
print(f"Each person will pay =", amount_per_person)
