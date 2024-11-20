def month_to_season(n):
    if  12 <= n <= 2:
        return "Зима"
    elif 3 <= n <= 5:
        return "Весна"
    elif 6 <= n <= 8:
        return "Лето"
    elif 9 <= n <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"

try:
    n = int(input("Номер месяца (1-12): "))
    print(month_to_season(n))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")