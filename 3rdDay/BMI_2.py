height = abs(int(input("Height in cm\n")))
weight = abs(int(input("Weight in kg\n")))
BMI = weight / ((height / 100) ** 2)

print(BMI)

if BMI <= 18.5:
	print("You are underweight.")
elif BMI < 25:
	print("You are a normal weight.")
elif BMI < 30:
	print("You are slightly overweight.")
elif BMI < 35:
	print("You are overweight.")
else:
	print("You are clinically obese.")
