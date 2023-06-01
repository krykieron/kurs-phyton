# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

# a) Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
tytul = input("Podaj tytuł książki: ")
bez_sp_tytul = tytul.replace(" ", "")
czy_litery_tyt = bez_sp_tytul.isalpha()
print("Prawidłowy tytuł?:", czy_litery_tyt)

autor = input("Podaj nazwisko autora:")
bez_sp_autor = autor.replace(" ", "")
czy_litery_au = bez_sp_autor.isalpha()
print("Prawidłowy autor?:", czy_litery_au)

l_stron = input("Podaj liczbę stron:")
czy_liczba = l_stron.isdigit()
print("Prawidłowy liczba?:", czy_liczba)

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
popr_tytul = tytul.capitalize()
popr_autor = autor.title()

# Połącz dane w jeden ciąg book za pomocą spacji
polaczone = "".join(popr_tytul + " " + popr_autor + " " + l_stron)
print("Połącz dane w jeden ciąg book za pomocą spacji:\n", polaczone)

# Policz liczbę wszystkich znaków w napisie book
zlicz = polaczone.__len__()
print(zlicz)



