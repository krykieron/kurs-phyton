otworz_plik = "PT.txt"
with open(otworz_plik, 'r') as f:
    content = f.read()
    print(content)

# with open(filename, 'w') as f:
#  f.write(data)
#
# with open(filename, 'a') as f:
#  f.write('\\n' + data)