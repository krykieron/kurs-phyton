# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
opinia1 = int(input("Na ile oceniasz książkę 1 (1-10) ->:"))
opinia2 = int(input("Na ile oceniasz książkę 2 (1-10) ->:"))
opinia3 = int(input("Na ile oceniasz książkę 3 (1-10) ->:"))

# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.

srednia = (opinia1 + opinia2 + opinia3)/3
zaokragl = round(srednia,3)
print(zaokragl)

if zaokragl >= 7:
    print("Bardzo dobra")

elif zaokragl >=4:
    print("Przeciętna")

else:
    print("niewarta uwagi")



# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.