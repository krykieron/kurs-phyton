# Utwórz zmienną przechowującą dowolny ciąg znaków.


ciag = str(input("Wprowadz tresc"))
dlugosc_c = len(ciag)
print(dlugosc_c)

# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
if dlugosc_c > 5:
    print("Ciąg zawiera więcej niż 5 znaków")

# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.