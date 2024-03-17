def prime_checker(number):
  if number <= 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      # print(f"{number} yis not a prime number, for example it's divisible by {i}.")
      return False
  # print(f"{number} is a prime number.")
  return True

prime_numbers = []
for i in range(0, 101):
  if prime_checker(i):
    prime_numbers.append(i)

def prime_numbers_up_to(upper_bound):
  known_multiples = []
  known_primes = []
  for i in range(2, upper_bound+1):
    if i in known_multiples:
      continue
    else:
      print("checking i in BIG FUNCTION", i)
      if prime_checker(i):
        known_primes.append(i)
      # in any case: add the multiples to the known multiples
      j = 2
      while i * j <= upper_bound:
        if not j * i in known_multiples:
          known_multiples.append(j * i)
        j += 1
  return known_primes

print(prime_numbers_up_to(100))

for i in range(0, 101):
  print("checking i in FOR LOOP", i)
  prime_checker(i)
