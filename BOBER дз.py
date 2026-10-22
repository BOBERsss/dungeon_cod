import random

NAMES = ["Шрек", "Наруто", "Спанч Боб", "Сайтама", "Ґоку"]
CLASSES = ["Воїн", "Маг", "Лучник", "Паладин", "Ассасин"]


def generate_party(count=5):
    party = []
    for _ in range(count):
        hero = {
            "name": random.choice(NAMES),
            "class": random.choice(CLASSES),
            "hp": random.randint(80, 150),
            "attack": random.randint(15, 30),
        }
        party.append(hero)
    return party


def power(hero):
    return hero["hp"] // 10 + hero["attack"] * 2


def best_hero(party):
    if not party:
        return None

    strongest = party[0]
    for hero in party[1:]:
        if power(hero) > power(strongest):
            strongest = hero
    return strongest


def main():
    for run in range(1, 4):
        print(f"=== Запуск №{run} ===")
        party = generate_party(5)

        for hero in party:
            print(
                f"Герой: {hero['name']} | Клас: {hero['class']} | HP: {hero['hp']} | Атака: {hero['attack']} | Сила: {power(hero)}"
            )

        champion = best_hero(party)
        print(
            f"--> Найсильніший: {champion['name']} ({champion['class']}) із силою {power(champion)}\n"
        )


if __name__ == "__main__":
    main()


