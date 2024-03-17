from wonderwords import RandomWord
wordgenerator = RandomWord()

lives = 10

def getWord():
  newWord = wordgenerator.word(word_min_length = 5, include_parts_of_speech=["noun"])
  return newWord

word = getWord().lower()

guessedLetters = []
def getLetterFromUser():
  letter = ""
  while len(letter) != 1 or letter in guessedLetters:
    letter = input("Give me one letter: ").lower()
  guessedLetters.append(letter)
  return letter

def obscureWord(unobscuredWord, lettersToDisplay):
  obscuredLetterList = []
  unobscuredLetterList = list(unobscuredWord.lower())
  for letter in unobscuredLetterList:
    if letter in lettersToDisplay:
      obscuredLetterList.append(letter)
    else:
      obscuredLetterList.append("_")
  return " ".join(obscuredLetterList)

def printCurrentState():
  obscuredWord = obscureWord(word, guessedLetters)
  print(obscuredWord, f"\t\tguessed already: {guessedLetters}")

while lives > 0 and "_" in obscureWord(word, guessedLetters):
  printCurrentState()
  newLetter = getLetterFromUser()
  if newLetter in word:
    print(f"✅ {newLetter} is in the word!")
  else:
    lives -= 1
    print(f"❌ Lives remaining: {lives}")

if lives == 0:
  print(f"😱 Get fucked, you lost. The word was: {word}")
else:
  print(f"🥳 Congratulations! The word was indeed {word}")
