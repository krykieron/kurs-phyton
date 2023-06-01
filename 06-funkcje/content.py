import random

with open('cytaty.txt', 'r', encoding='utf-8') as fopen:
    for line in fopen:
        print('Quote of the day is:')
        print('*' * 100)
        cytat = fopen.readlines()
        losowy_cytat = random.choice(cytat)
        print(losowy_cytat.strip())
        print('*' * 100)