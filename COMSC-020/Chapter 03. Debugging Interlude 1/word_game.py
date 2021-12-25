#
# Problem: https://docs.google.com/document/d/1HBz9_wu8gA0eLTig7cXqvqjEVGLR2155AgibBHfeg1o/edit?usp=sharing
#



# prompt the user for the name, age, city, college, profession, animal, and its name
name = input("Enter a name: ")
age = int(input("Enter a age (as an integer): "))
city = input("Enter a city: ")
college = input("Enter a college: ")
profession = input("Enter a profession: ")
animal = input("Enter a type of animal: ")
petname = input("Enter a pet's name: ")

print() # for readability

# display the story
print(f"There once was a person named {name} who lived in {city}.")
print(f"At the age of {age}, {name} went to college at {college}. {name} graduated and went to work as a {profession}.")
print(f"Then, {name} adopted a(n) {animal} named {petname}. They both lived happily ever after!")
