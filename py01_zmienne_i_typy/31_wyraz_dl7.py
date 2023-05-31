# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

wyraz = input('Podaj wyraz: ')
dlugosc = len(wyraz)

if dlugosc > 7 and dlugosc % 2 != 0 :
    print('Długość wyrazu jest nieparzysta i wynosi: ', dlugosc)
    srodek_w = int((dlugosc / 2)-1)
    print(srodek_w)
    koniec_w = srodek_w + 3
    print(koniec_w)
    print(wyraz[srodek_w:koniec_w])

else:
    print("Wyraz jest za krótki lub ma parzystą liczbę liter, uruchom ponownie program")