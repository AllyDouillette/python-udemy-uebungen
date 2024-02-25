import random

choices = ["rock", "paper", "scissors"]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

print(f"You chose {choices[player]}, computer chose {choices[computer]}.")
you_win = False

if player == computer:
	print("no one wins")
	exit
elif player == 0:
	if computer == 2:
		you_win = True
elif player == 1:
	if computer == 0:
		you_win = True
elif player == 2:
	if computer == 0:
		you_win == True

if you_win:
	print("You win")
else:
	print("You lose")
