print("Welcome to the tip calculator.")
totalAmount = input("What was the total bill?\n$")
totalAmount = float(totalAmount)
# totalAmount = 124.56

tipPercentage = input("What percentage tip would you like to give?\n")
tipPercentage = int(tipPercentage)
# tipPercentage = 12

numPeople = input("How many people split the bill?\n")
numPeople = int(numPeople)
# numPeople = 7

amountPerPerson = round((totalAmount * (1 + tipPercentage / 100)) / numPeople, 2)
print(f"Each person should pay ${amountPerPerson}.")
