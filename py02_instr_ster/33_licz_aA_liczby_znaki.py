# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery,
# wielkie litery, cyfry i znaki specjalne.

user_txt = input("Wprowadź tekst:")

lower_l = 0
upper_l = 0
digits = 0
other_ch = 0

for znak in user_txt:
    if znak.islower():
        lower_l +=1
    elif znak.isupper():
        upper_l += 1
    elif znak.isdigit():
        digits += 1
    else:
        other_ch += 1

print("Malych liter jest:", lower_l)
print("Duzych liter jest:", upper_l)
print("Liczb w tekscie jest:", digits)
print("Pozostałych znaków:", other_ch)