# Przekopiuj zawartość do zmiennej.
tresc = ("""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")

print()
print('* ' *40)
print()
print("1. Policz liczbę wystąpień słowa better.", tresc.count('better'))
print("2. Usuń z tekstu symbol gwiazdki:\n",tresc.replace('*',''))
print("3. Zamień jedno wystąpienie explain na understand:\n", tresc.replace('explain', 'understand', 1))
print("Usuń spacje i połącz wszystkie słowa myślnikiem:\n", tresc.replace(' ','-'))
print("Podziel tekst na osobne zdania za pomocą kropki: <------???? przecież są zdania?")

