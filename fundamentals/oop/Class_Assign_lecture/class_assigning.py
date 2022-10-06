class Item:
    def __init__(self,name,size,_color,weight):
        self.name = name
        self.size = size
        self.color = _color
        self.weight = weight

class Player:
    def __init__(self,data):
        self.name = data["name"]
        self.race = data["race"]
        self._class = data["class"]
        self.hp = data["hp"]
        self.backpack = []

    def addItem(self,item):
        self.backpack.append(item)
        return self

    def showBackPack(self):
        for item in self.backpack:
            print(item.name)

    def showWeight(self):
        total = 0
        for item in self.backpack:
            total += item.weight
        print(f"{self.name}'s Backpack weight is {total} pounds")
        return total


player = {
    "name":"Nathan",
    "race":"Orc",
    "class":"Wizard",
    "hp":4,
}

nathan = Player(player)
print(nathan.name)

spellbook = Item("Spellbook", 2, "grey", 1)
shield = Item("Shield", 3, "Silver,blue,yellow", 4)
staminaPotion = Item("Stamina Potion", 1, "green", 1)

nathan.addItem(spellbook).addItem(staminaPotion).addItem(staminaPotion)
nathan.showBackPack()
print(nathan.showWeight())