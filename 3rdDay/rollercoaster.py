import random
height = int(input("How tall are you in cm?"))

if height <= 0:
	height = random.randrange(50, 200, 1)
	print(f"I don't think that's true, I'll guess your height to be {height}.")

age = int(input("How old are you in years?"))

if age <= 0:
	age = random.randrange(1, 100, 1)
	print(f"I don't think that's true, I'll guess your age to be {age}.")

bill = 0

if height >= 120:
	if age < 12:
		print("Please pay $5.")
		bill = 5.
	elif age <= 18:
		print("Please pay $7.")
		bill = 7.
	elif age >= 45 and age <= 55:
		print("Your life sucks, you can ride for free.")
	elif age >= 18:
		print("Please pay $12.")
		bill = 12

	wants_photo = input("Do you want a photo? press Y for yes")
	if wants_photo == "Y":
		bill += 3

else:
	print(f"Go away you're too small at {height} cm.")

print(f"Your total bill is ${bill}")
