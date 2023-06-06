import random


gamer = input("Co wybierasz? p/k/n:")
cpu = random.choice(["p", "k", "n"])
print(f"wybór gracza: {gamer}")
print(f"wybór komputera: {cpu}")

if gamer == cpu:
    print("REMIS")
if gamer == "k" and cpu == "p":
    print("wygrywa CPU - papier zawija kamień")
if gamer == "k" and cpu == "n":
    print("wygrywa GRACZ - kamień tępi nożyczki")
if gamer == "p" and cpu == "k":
    print("wygrywa GRACZ - papier zawija kamień")
if gamer == "p" and cpu == "n":
    print("wygrywa CPU - nożyczki tną papier")
if gamer == "n" and cpu == "k":
    print("wygrywa CPU - kamień tępi nożyczki")
if gamer == "n" and cpu == "p":
    print("wygrywa GRACZ - nożyczki przecinają papier")
