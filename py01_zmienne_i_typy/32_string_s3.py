# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
# utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = input('Podaj 1 wyraz: ')
s2 = input('Podaj 2 wyraz: ')

# liczby
liczba_s1 = len(s1)
liczba_s2 = len(s2)
polowa_s1 = int(liczba_s1 / 2)
#stringi
lewa_s1 = s1[:polowa_s1]
print('Lewa strona pierwszego wyrazu to:', lewa_s1)

zmiana_s1_na_ujemna = polowa_s1 - (2 * polowa_s1)
prawa_s1 = s1[zmiana_s1_na_ujemna:]
print('Prawa strona pierwszego wyrazu to:', prawa_s1)
print('**********')

#nowe słowo s3
s3 = lewa_s1 + s2 + prawa_s1
print(lewa_s1)
print(prawa_s1)
print('Nowopowstały wyraz to:', s3)
