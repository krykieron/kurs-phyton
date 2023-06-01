# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
l1 = int(input("Podaj pierwszą liczbę:"))
l2 = int(input("Podaj drugą liczbę:"))
suma = l1 + l2

# Jeśli suma jest większa niż 100, wyświetl wynik,
if suma > 100:
    print("Suma liczb wynosi", suma)
else:
    print("KONIEC")
# w przeciwnym wypadku wyświetl “Koniec”.