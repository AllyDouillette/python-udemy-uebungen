import math

def paint_calc(height, width, cover):
  numOfCans = (height * width) / cover
  roundUp = math.ceil(numOfCans)
  print(f"You'll need {roundUp} cans of paint.")

paint_calc(3,9,5)
