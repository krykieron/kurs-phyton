# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20
# ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

mine_num = 6
your_numer = int(input("Find mine number 0-20\n"))

while your_numer != mine_num:
    print("Try again")

    your_numer = int(input("Find mine number 0-20\n"))