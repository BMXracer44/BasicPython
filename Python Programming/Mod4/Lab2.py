#Alex Ferguson
#Python
#Mod 4 Lab 2
#04/26/2023

class Pet:
    #init is the function that runs when an object is created
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def __str__(self):
        return f"This {self.species} is named {self.name} and has a sound of {self.sound}"
    
    def speak(self):
        print(f"The {self.species} goes {self.sound}")

pet_one = Pet("Spot", "Dog", "Bark")

print(pet_one)
print(pet_one.speak())

pets = []

pets.append(pet_one)
pets.append(Pet("Tucker", "Cat", "Meow"))
pets.append(Pet("Jolie", "Dog", "Woof"))

for pet in pets:
    print(pet)
    pet.speak()