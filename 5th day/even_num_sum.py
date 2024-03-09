target = 1_000_000
even_sum = 0
for current_num in range(0, target+1):
  if current_num % 2 == 0:
    even_sum += current_num

print(even_sum)

# even_sum = 0
# for current_num in range(0, target+1, 2):
#   even_sum += current_num

# print(even_sum)
