print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give?"))
people = int(input("How many people should split the bill?"))

bill /= people
tip = bill * (percentage *0.010)
final_amount = "{:.2f}".format(bill + tip)
print(f"Each person should pay: ${final_amount}")
