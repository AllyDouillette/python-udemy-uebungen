def fizzbuzz (upperBoundary):
  for num in range(1, upperBoundary+1):
    text = ""
    if num % 3 == 0:
      text += "Fizz"

    if num % 5 == 0:
      text += "Buzz"

    if text == "":
      print(num)
    else:
      print(text)

fizzbuzz(100)
