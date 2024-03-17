# Old Bag Burger
#   + Süßkartoffelpommes
#   + Ketchup und Mayo
# Tiroler Burger normal
#   + Philly Cheese Fries
#   + Jalapeño Mayo 2x
# Tiroler Burger OHNE BACON MIT VEGANEM PATTY
#   NIX POMMES
# Avocadoburger
#   belgische
#   + 2x sweet honey mustard

# fill alphabet
small_alphabet = []
big_alphabet = []
for i in range(0, 26):
  unicode_a = ord("a")
  unicode_A = ord("A")
  small_alphabet.append(chr(unicode_a + i))
  big_alphabet.append(chr(unicode_A + i))

def isValidChar(letter):
  if ord(letter) in range(65, 65+26) or ord(letter) in range(97, 97+26):
    return True
  else:
    return False

def getShiftArray(letter):
  if ord(letter) in range(65, 65+26):
    return big_alphabet
  if ord(letter) in range(97, 97+26):
    return small_alphabet

def shiftLetter(letter, shift):
  if isValidChar(letter) == False:
    return letter

  shiftArray = getShiftArray(letter)
  currentIndex = shiftArray.index(letter)
  # make shift something between - length and + length of the damn array
  newIndex = (currentIndex + shift) % len(shiftArray)
  return shiftArray[newIndex]

def encrypt(word, shift):
  encrypted = ""
  for i in range(0, len(word)):
    currentChar = word[i]
    encrypted += shiftLetter(currentChar, shift)
  return encrypted

def decrypt(word, shift):
  return encrypt(word, -shift)

word = "Lol was geht my guys"
shift = 42
testEncrypt = encrypt(word, shift)
testDecrypt = decrypt(testEncrypt, shift)
print(testEncrypt)
print(testDecrypt)
