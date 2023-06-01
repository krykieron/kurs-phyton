
--- opcia 1 ---
# list.copy()
# list.sort(*, key=None, reverse=False)
# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.count(x)
#Return the number of times x appears in the list.

trip = ['latarka', 'plecak', 'woda', 'monkey']

# --- opcja 1 ----
# arr = input('Podaj listę słów po spacji')
# # arr = arr.replace(" ", "").split(',')
# # arr = list(arr)
# arr = arr.split
# print(arr)

# --- opcja 2 ----
arr = []
num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):

    item = input("Podaj element, który chcesz dorzucic do list ->")
    
    arr.append(item)

print(arr)

print(arr[0])
print(arr[-1])

if arr[0] == arr[-1]:
    print('Elementy są takie same')
else:
    print('Elementy nie są takie same')