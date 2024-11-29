from math import ceil
a = float(input("Сторона: "))
def square(a):
    formula = a * a
    return formula


rounded = ceil(square(a))
print("Площадь квадрата: " + str(rounded))