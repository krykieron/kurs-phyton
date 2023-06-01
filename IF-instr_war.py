lower_letters = 0
upper_letters = 0
digits = 0
other_chars = 0

txt = input('Enter text: ')
txt_len = len(txt)

for i in txt:
    if i.isupper():
        upper_letters +=1
    elif i.islower():
        lower_letters +=1
    elif i.isdigit():
        digits += 1
    else: other_chars +=1

print('lower_letters: ', lower_letters)
print('upper_letters ', upper_letters)
print('digits ', digits)
print('other_chars ', other_chars)