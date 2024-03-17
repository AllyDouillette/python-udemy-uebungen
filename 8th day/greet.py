# def greet():
#   print("Hello!")
#   print("World!")
#   print("uwu")

# def greet_by_name(name = "homie"):
#   print(f"Hello {name}!")
#   if (name != "Robert" and name != "Andrea"):
#     print(f"How do you do, {name}?")
#   else:
#     print("uwu hallo Mausi!")

# greet_by_name("Andrea")
# greet_by_name("Eli")
# greet_by_name()

def greet_with(location, name):
  if name == "":
    name = "Test"
  print(f"Hi {name}!")
  print(f"What is it like in {location}?")

greet_with("lol","")
