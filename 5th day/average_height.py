heights = [151, 145, 178]
sum = 0
count = 0
for current_height in heights:
  # keep track of how many heights we have seen
  count = count + 1
  # add it to the sum
  sum = sum + current_height

# at the end we calculate the final sum divided by final count
avg_height = int(round(sum / count, 0))

print(f"""total height = {sum}
number of students = {count}
average height = {avg_height}""")
