class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feeding(self, food):
        self.weight += food
        return "feeding"


class Poultry(Animals):

    def we_get(self):
        return "eggs"


class Goose(Poultry):
    species = "Goose"

    def voice(self):
        return "Ga-Ga-Ga!"


class Chicken(Poultry):
    species = "Chicken"

    def voice(self):
        return "Ko-Ko-Ko!"


class Duck(Poultry):
    species = "Duck"

    def voice(self):
        return "Krya-Krya!"


class livestock(Animals):

    def we_get(self):
        return "wool"


class Cow(livestock):
    species = "Cow"

    def we_get(self):
        return "milk of cow"

    def voice(self):
        return "Muu!"


class Ram(livestock):
    species = "Ram"

    def voice(self):
        return "Bee!"


class Goat(livestock):
    species = "Goat"

    def we_get(self):
        return "milk of goat"

    def voice(self):
        return "Meee!"


food = int(input("Please feed the animals on the farm! Enter the amount of feed: "))
print()
farm = [
    Chicken("Ко-ко", 3),
    Chicken("Кукареку", 4),
    Goose("Белый", 5),
    Goose("Серый", 4),
    Duck("Кряква", 4),
    Ram("Барашек", 65),
    Ram("Кудрявый", 70),
    Cow("Манька", 400),
    Goat("Рога", 40),
    Goat("Копыта", 50),
]
max_weight = 0
sum_weight = 0
print('Animals on farm:\n')
for animals in farm:
    print(
        f"""{animals.species}: name: "{animals.name}", voice: {animals.voice()}, weight: {animals.weight}kg, gives: {animals.we_get()}""")
    animals.feeding(food)
    sum_weight += animals.weight
    if animals.weight > max_weight:
        max_weight = animals.weight
        species_name = animals.species
print(f"Weight of all animals = {sum_weight}")
print(f"The name of the heaviest animal: {species_name} with weight {max_weight} kg")
