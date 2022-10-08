class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 200
        self.energy = 100

    def sleep(self): #increases the pet's energy by 25
        self.energy += 25
        return self

    def eat(self): #increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print(f"{self.name} is full.")
        return self

    def play(self): #increases the pet's health by 5
        self.health += 5
        self.energy -= 10
        print(f"{self.name} had fun but is now tired.")
        return self

    def noise(self): #prints out the pet's sound
        print("Growl")
        return self


# Shenron = Pet("Shenron", "reptile", "roll-over") #not needed since file is imported elsewhere