# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku:
# niedowaga / waga normalna / nadwaga / otyłość.


wzrost = float(input('Podaj swój wzrost w metrach\n'))
waga = float(input('Podaj swoją wagę w kilogramach\n'))

bmi = waga / (wzrost ** 2)

if bmi < 18.5:
    print('Underweight', round(bmi, 2))
if bmi >= 18.5 and bmi < 25:
    print('Healthy Weight', round(bmi, 2))
if bmi >= 25 and bmi <= 30:
    print('Overweight', round(bmi, 2))
if bmi > 30:
    print('Obesity', round(bmi, 2))



