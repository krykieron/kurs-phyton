# Komputer losuje liczbę z zakresu od 1 do 100.
# Użytkownik podaje swój traf.
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
# Jeśli użytkownik zgadnie wygrywa gracz.
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

cpu = random.randint(1,3)
user =int(input("Zgadnij liczbę 1-3:\n"))
steps = 6

while (steps > 0):
    if cpu != user:
        print("Zimno")
        steps -= 1
        print("Spróbuj jeszcze raz")
        user =int(input("Zgadnij liczbę 1-3:\n"))
    else:
        print("Wygrałeś")
    break

    #



