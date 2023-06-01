tekst = input("Podaj tekst:")
bez_spacji = tekst.replace(" ", "").lower()

print("Czy to jest palindrom?:", bez_spacji == bez_spacji[::-1])