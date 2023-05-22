# 1. Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. \
# Załóżmy, że spalanie na 100km wynosi 6,4 l,
# trasa to 120km,
# litr benzyny kosztuje 5,04 zł.

# cena_benzyny = 5.04
# trasa = 120
# spalanie = 6.4
# koszt_wyprawy = trasa * spalanie * cena_benzyny / 100
# print('Całkowity koszt wyprawy wyniesie', round(koszt_wyprawy,2), 'złote')


# 2. Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
cena_benzyny = float(input('Jaka jest obecnie cena benzyny?'))
trasa = float(input('Podaj dystans do pokonania: '))
spalanie = float(input('Ile spala Twoje auto?'))
koszt_wyprawy = trasa * spalanie * cena_benzyny / 100
print('Całkowity koszt wyprawy wyniesie', round(koszt_wyprawy,2), 'złote')


