# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę,
# 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = str('Zenobiusz89')

if len(password) < 8:
    print("Error: password is to short")
if password.isalnum() and password.isalpha():
    print("Error: missing digits in alphanumeric password.")
if password.isalpha() and password.isdigit():
    print("Error: missing letter in alphanumeric password.")
if password.islower():
    print("Error: missing at least one uppercase")
if password.isupper():
    print("Error: missing at least on lowercase")
print(f'Your not sdfa password {password}')
