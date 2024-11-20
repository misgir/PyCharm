def is_year_leap(n):
    return "True" if n % 4 == 0 else "False"

num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"год {num} - {result}")