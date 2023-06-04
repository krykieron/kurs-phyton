# Napisz program, który wyświetli kolejne wyniki
# dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

liczba = int(input('Podaj liczbę mniejszą od 8 : '))
silnia = 1

if liczba < 8:
   for i in range(2,liczba+1):
      silnia = silnia * i
   print(silnia)
else:
   print("Podana liczba nie jest mniejsza od 8.")