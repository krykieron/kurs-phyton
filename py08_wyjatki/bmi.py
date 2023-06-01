# W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
# Co jeśli użytkownik poda wartość 60 kg ?
# Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.


def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "standard"
    elif bmi < 30:
        return "overweight"
    else:
        return "obesity"

