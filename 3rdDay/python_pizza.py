print("Thank you for choosing Python Pizza Deliveries.")
size = input("What size do you want, S, M, or L? ").upper()
add_pepperoni = input("Do you want extra pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()

bill = 0

if size == "S":
	bill = 15
elif size == "M":
	bill = 20
elif size == "L":
	bill = 25
else:
	print("You haven't selected a valid size!")

if add_pepperoni == "Y":
	if size == "S":
		bill += 2
	if size == "M" or size == "L":
		bill += 3

if extra_cheese == "Y":
	bill += 1

print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
