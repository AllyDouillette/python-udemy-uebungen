city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your first pet?\n")
bandname = city + " " + pet
print(f"To honour your birthplace of {city} and your first pet being named {pet}, your band name could be:\n{bandname}")
print("So your pets name was {} and you grew up in {}".format(pet, city))
print("So your pets name was {1} and you grew up in {0}".format(city, pet))
