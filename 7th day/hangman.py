from wonderwords import RandomWord
wordgenerator = RandomWord()

lives = 10
# while lives <= 0:
#   lives = int(input("Choose the number of lives you want to have: "))

def getWord():
  return wordgenerator.word(word_min_length = 5, include_parts_of_speech=["noun"])

word = getWord()

guessedLetters = []
def getUserInput():
  letter = ""
  while len(letter) != 1:
    letter = input(f"\nGuess #{len(guessedLetters)+1}: ").lower()
    if len(letter) > 1:
      print(f"Choose ONE letter.")
      letter = ""
    elif len(letter) == 0:
      print(f"Enter something.")
      letter = ""
    elif letter not in guessedLetters:
      guessedLetters.append(letter.lower())
      guessedLetters.sort()
      break
    else:
      print(f"You picked that one already. Choose one that's not in these: {guessedLetters}.")
      letter = ""
  return letter

# generate a random word
def obscureWord(word, guessedLetters):
  word.lower()
  guessedLetters = list(map(lambda letter: letter.lower(), guessedLetters))
  obscuredLetterList = []
  letterList = list(word)
  for letter in letterList:
    if letter in guessedLetters:
      obscuredLetterList.append(letter)
    else:
      obscuredLetterList.append("_")
  return " ".join(obscuredLetterList)

def getCurrentState():
  print(obscureWord(word, guessedLetters))

def completed():
  return "_" not in obscureWord(word, guessedLetters)

while lives > 0 and completed() == False:
  getCurrentState()
  chosenLetter = getUserInput()
  if chosenLetter in list(word.lower()):
    print(f"\n✅ {chosenLetter} is in the word!\n")
  else:
    lives -= 1
    print(f"\n❌ {chosenLetter} is NOT in the word!\nYou have {lives} lives left.\n")

if lives == 0:
  print(f"😤 You lost.\n🤯 The word would've been \"{word}\".")
else:
  print(f"🥳 Congrats, you won!\nThe word is indeed \"{word}\".")
