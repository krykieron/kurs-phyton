#  Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

podaj_imiona = input('Podaj imiona po przeciunku: ')
name = podaj_imiona.replace(" ", "").split(",")
for n in name:
    print(f"Witaj {n} miło Cię poznać")
