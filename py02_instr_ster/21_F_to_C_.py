# Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

# # dla WHILE
Fahr = 0
print("Pętla WHILE")
while Fahr <= 200:
    Celc = round( 5 / 9 * (Fahr - 32), 2)
    print(f"Dla {Fahr} F --> {Celc}C")
    Fahr += 20

# dla FOR
print("Pętla FOR")
for temp in range(0, 201, 20):
    Celc = round(5 / 9 * (Fahr - 32), 2)

    print(f"Dla {Fahr} F --> {Celc} C")
    Fahr += 20