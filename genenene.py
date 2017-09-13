
import random

pokeList = [
    "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew",
    "Sandslash", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales",
    "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat",
    "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe",
    "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp",
    "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta",
    "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer",
    "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler",
    "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung",
    "Koffing", "Weezing"
]


def rw():
    return random.choice(pokeList)


def m1():
    for i in range(15):
        print('(', end="")

        print('"', end="")
        print(random.choice(pokeList), end="")
        print('",', end="")

        print('"', end="")
        print(random.choice(["CSE", "CT", "IT"]), end="")
        print('",', end="")

        print('"', end="")
        print(random.choice(range(2013, 2019)), end="")
        print('"', end="")

        print('),', end="")
        print()


def m2():
    for i in range(30):
        print('(', end="")

        print('"', end="")
        print('book_', end="")
        print(rw(), end="")
        print('"', end="")

        print(',"', end="")
        print('author_', end="")
        print(rw(), end="")
        print('"', end="")

        print(',"', end="")
        print('pub_', end="")
        print(rw(), end="")
        print('"', end="")

        print(',"', end="")
        print('subject_', end="")
        print(rw(), end="")
        print('"', end="")

        print(',', end="")
        print(random.randint(1, 20), end="")
        print('', end="")
        print('),', end="")

        print()


def m3():
    for i in range(30):
        print('(', end="")

        print(random.randint(49, 76), end="")
        print(',', end="")

        print('', end="")
        print(random.randint(47, 76), end="")
        print(',', end="")

        print('"', end="")
        print(random.randint(0, 27), end="")
        print('/', end="")
        print(random.randint(0, 13), end="")
        print('/2017', end="")
        print('",', end="")

        print('"', end="")
        print(random.randint(0, 27), end="")
        print('/', end="")
        print(random.randint(0, 13), end="")
        print('/2017', end="")
        print('"', end="")

        print('),', end="")
        print()


m3()
