def month_to_season(n_month):
    if n_month in (12, 1, 2):
        print("Зима")
    elif n_month in (3, 4, 5):
        print("Весна")
    elif n_month in(6,7,8):
        print("Лето")
    elif n_month in (9,10,11):
        print("Осень")
try:
    n_montn = int(input("Номер месяца (1-12): "))
    print(month_to_season(n_montn))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")