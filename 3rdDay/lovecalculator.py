print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

fullName = name1 + name2
fullName = fullName.lower()

countTrue = 0
countLove = 0

countTrue += fullName.count("t")
countTrue += fullName.count("r")
countTrue += fullName.count("u")
countTrue += fullName.count("e")

countLove += fullName.count("l")
countLove += fullName.count("o")
countLove += fullName.count("v")
countLove += fullName.count("e")

finalCount = int(str(countTrue) + str(countLove))

if finalCount < 10 or finalCount > 90:
	print(f"Your score is {finalCount}, you go together like coke and mentos.")
elif finalCount >= 40 and finalCount <= 50:
	print(f"Your score is {finalCount}, you are alright together.")
else:
	print(f"Your score is {finalCount}.")
