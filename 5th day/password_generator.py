#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# get a password container
password = ""
# make a count list:
counts = [nr_letters, nr_numbers, nr_symbols]
# make a corresponding list with the possible characters:
chars = [letters, numbers, symbols]
# total length is all numbers together!
for i in range(0, nr_letters + nr_numbers + nr_symbols + 1):
  # choose a random number between all available categories
  categoryId = ""
  while True:
    categoryId = random.randint(0, len(counts)-1)
    # check the counts remaining at that position, if we still need more than 0 continue
    if counts[categoryId] > 0:
      counts[categoryId] -= 1
      break

  # now categoryId is something between 0 and 2
  # get that character set
  possibleChars = chars[categoryId]
  # get a random number out of that character sets length
  charId = random.randint(0, len(possibleChars)-1)
  # get the associated char
  newChar = possibleChars[charId]
  # and smash it at the end of the passwordd
  password += newChar
  # just to be sure, null newChar
  newChar = ""

print(password, len(password))
