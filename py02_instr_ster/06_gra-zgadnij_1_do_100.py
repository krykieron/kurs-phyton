# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

your_number = int(input("Zgadnij jaką liczbę mam na myśli?\nPodaj liczbę od 1 do 100:\n"))
mine_number = 76

if your_number == mine_number:
    print(f"Gratulacje, zgadłeś, moja liczba to {mine_number}")
else:
    missing=input("Pudło")

