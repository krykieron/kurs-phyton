# Utwórz zmienną przechowującą dowolny ciąg znaków.

ciag = str(input("Wprowadz tresc:\n"))

# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis

if len(ciag) > 5:
    print("Ciąg zawiera więcej niż 5 znaków, a jego treść to:\n", ciag.replace('a', 'z'))