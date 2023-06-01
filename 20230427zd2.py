#75 godzin ile to pełnych tygodni
how_much_h= float(input('Ile godzin dziennie możesz się uczyć?'))
knowlege_h = 75
day_in_week = 7

need = knowlege_h // (how_much_h * day_in_week)

print('Bedziesz się uczyc ', need, 'tygodni')