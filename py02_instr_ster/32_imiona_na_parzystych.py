# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

tekst = 'Podaj mi jakis tekst do wyswietlenia i obrobki'

for i in tekst:
    print(i)

    txt = input('Give me any text with any characters ->')

    lower_letters = 0
    upper_letters = 0
    digits = 0
    other_chars = 0

    for char in txt:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
        elif char.isdigit():
            digits += 1
        else:
            other_chars += 1

    print("lower letters:", lower_letters)
    print("upper letters:", upper_letters)
    print("digits:", digits)
    print("other:", other_chars)


