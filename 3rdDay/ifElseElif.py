import random
height = int(input("How tall are you in cm?"))

if height <= 0:
	height = random.randrange(50, 200, 1)
	print(f"I don't think that's true, I'll guess your height to be {height}.")

age = int(input("How old are you in years?"))

if age <= 0:
	age = random.randrange(1, 100, 1)
	print(f"I don't think that's true, I'll guess your age to be {age}.")

if height >= 120:
	if age < 12:
		print("Please pay $7.")
	elif age <= 14:
		print("Please pay $9.")
	elif age <= 18:
		print("Please pay $12.")
	else:
		print("Please pay $20.")
else:
	print(f"Go away you're too small at {height} cm.")
