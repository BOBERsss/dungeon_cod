from heroes import CLASSES, create_hero, show_hero

print("Ласкаво просимо до Dungeon Code!")
print("Доступні класи:", ", ".join(CLASSES))

name = input("Як звати твого героя? ")
hero_class = input("Обери клас: ")

if hero_class in CLASSES:
    hero = create_hero(name, hero_class)
    show_hero(hero)
else:
    print("Такого класу немає. Спробуй ще раз!")
