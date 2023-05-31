# Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:

quote = 'Honesty is the first chapter in the book of wisdom.'
dlugosc = len(quote)
polowa = int(dlugosc / 2)

print('a) Policz wszystkie znaki w napisie:\n', dlugosc)
print('b) Nie modyfikując zmiennej wyświetl słowo wisdom:\n',quote[-7:])
print('c) Wyświetl tylko pierwszą połowę tekstu:\n', quote[ : polowa-1])
print('d) Wyświetl tylko kropkę:\n', quote[-1:])
print('e) Wyświetl od połowy tylko co trzecią literę cytatu\n',quote[polowa -1 :: 3])
print('f) Wyświetl ‘Hnsyi h is hpe ntebo fwso.:\n',quote[ :: 2])
print('g) Wyświetl cały cytat odwrotnie:\n', quote[::-1])
print('h) Zamień wisdom na słowo friendship:\n',  quote.replace("wisdom", "friendship"))


