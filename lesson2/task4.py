n = int(input("fizz_buzz:"))


def fizz_buzz(n):
    for n in range(1,n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print(f"{n} - FizzBuzz")
        elif n % 3 == 0:
            print(f"{n} - Fizz")
        elif n % 5 == 0:
            print(f"{n} - buzz")


print(f"{n} - fizz_buzz")





