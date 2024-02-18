print("Welcome!")
choice = input("Left or right?\n")

if choice == "right":
	print("Game over")
else:
	choice = input("swim or wait?\n")
	if choice == "swim":
		print("Game over")
	else:
		choice = input("which door?\n")
		if choice == "yellow":
			print("you win!")
		else:
			print("Game over")
