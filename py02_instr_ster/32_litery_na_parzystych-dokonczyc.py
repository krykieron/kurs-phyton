# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = "To jest jakiś tam tekst do wyswietlenia i obrobki"
# txt = input("Wprowadź tekst: ")
txt_l = list(txt)
print(txt_l)
txt_dl = len(txt_l)
print(txt_dl)

for i in txt_l:
    print(i)