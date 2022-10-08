import dojo_pets_pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self): #walks ninja's pet invoking pet play() method
        self.pet.play()
        return self
        
    
    def feed(self): #feeds ninja's pet invoking pet eat() method
        self.pet.eat()
        return self

    def bathe(self): #cleans ninja's pet invoking pet noise() method
        self.pet.noise()
        return self


# class Pet:
#     def __init__(self, name, type, tricks):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.health = 200
#         self.energy = 100

#     def sleep(self): #increases the pet's energy by 25
#         self.energy += 25
#         return self

#     def eat(self): #increases the pet's energy by 5 & health by 10
#         self.energy += 5
#         self.health += 10
#         print(f"{self.name} is full.")
#         return self

#     def play(self): #increases the pet's health by 5
#         self.health += 5
#         self.energy -= 10
#         print(f"{self.name} had fun but is now tired.")
#         return self

#     def noise(self): #prints out the pet's sound
#         print("Growl")
#         return self


Shenron = dojo_pets_pet.Pet("Shenron", "reptile", "roll-over")
Bruce = Ninja("Bruce", "Lee", Shenron, "bones", "meat")

# Bruce.pet = Shenron
print(Bruce.pet.name)


Bruce.walk().feed().bathe()


##### Need to try Sensei Bonus #####