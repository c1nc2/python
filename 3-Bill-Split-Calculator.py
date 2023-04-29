
# welcome
print("TIP CALCULATOR")
print("==============")


# variables
bill = float(input("Total Bill? \n"))

tip = int(input("How much tip would you like to give? 5, 10, 15? \n"))

people = int(input("How many people to split the bill? \n"))

# calculation
bill_with_tip = tip / 100 * bill + bill
print(f"Each one has to pay: ${bill_with_tip}")

