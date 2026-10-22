import random
# HERO = {
#     "name": "BOBER",
#     "class":"homeless",
#     "hp": 100,
#     "dmg":15
# }
# print("Name",HERO["name"])
# print("Class",HERO["class"])
# print("Hp",HERO["hp"])
# print("Dmg",HERO["dmg"])

CLASSES = {
    "homeless":{"hp": (70,100), "dmg":(10,15) },
    "zombi":{"hp":(35,50), "dmg":(20,35)}
}

def create_hero(name,hero_class):
    stat = CLASSES[hero_class]
    return {
        "name":name,
        "class":hero_class,
        "hp":random.randint(*stat["hp"]),
        "dmg": random.randint(*stat["dmg"])
    }
def show_hero(hero):
    print(f"{hero["name"]} - {hero["class"]}" )
    print(f"HP: {hero["hp"]}" )
    print(f"DMG: {hero["dmg"]}")

hero = create_hero("BOBER", "homeless")
show_hero(hero)
