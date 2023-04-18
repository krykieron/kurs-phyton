w = input("Ile ważysz?")
h = input("a jaki jest Twój wzrost w metrach? ")

w = float(weight.repleace(",", "."))
h = float(high.repleace(",", "."))

bmi = weight / (high **2)
print('Twoje BMI wynosi =', round(bmi,2))

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))