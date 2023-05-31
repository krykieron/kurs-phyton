# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# a) Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
# b) Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
# c) Połącz dane w jeden ciąg book za pomocą spacji
# d) Policz liczbę wszystkich znaków w napisie book

tytul = input("Podaj tytuł książki: ")
autor = input("Podaj nazwisko autora:")


if tytul.isalpha() and autor.isalpha() == True:
    print("Tytuł i autor są OK")
else:
    print("Złe dane")

l_stron = input("Podaj liczbę stron:")

if l_stron.isdigit() == True:
    print("L. str. - OK")
else:
    print("Zła liczba str")

popr_tytul = tytul.title(),
popr_autor = autor.capitalize()
print(popr_tytul, " " , popr_autor)