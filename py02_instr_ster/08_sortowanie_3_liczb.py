# Sortowanie.
# Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.
num1 = int(input("Podaj 1 liczbę: "))
num2 = int(input("Podaj 2 liczbę: "))
num3 = int(input("Podaj 3 liczbę: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print("Pierwsza z podanych liczb jest największa i jest to", num1, '\n', num1, num2, num3)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print("Pierwsza z podanych liczb jest największa i jest to", num1, '\n', num1, num3, num2)

elif num2 > num1 and num2 > num3 and num3 > num1:
    print("Druga z podanych liczb jest największa i jest to", num2, '\n', num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3:
    print("Druga z podanych liczb jest największa i jest to", num2, '\n', num2, num1, num3)

elif num3 > num1 and num3 > num2 and num1 >num2 :
     print("Ostatnia z podanych liczb jest największa i jest to ", num3, '\n', num3, num1, num2)
elif num3 > num1 and num3 > num2 and num2 >num1 :
     print("Ostatnia z podanych liczb jest największa i jest to ", num3, '\n', num3, num2, num1)

else:
    num1 == num2 or num2 == num3 or num3 == num1
    print("Błąd!\nConajmniej dwie z podanych przez Ciebie liczb są sobie równe")
