chisla = int(input("Кол-во чисел: "))
chislo1 = float(input("Введите чиcло: "))
if chisla < 2:
    print("Нужно больше 2")
i = 2
while i <= chisla:
    taken = input('Действие: ( + , - , * , /, stepen): ')
    chislo2 = float(input("Введите число: "))
    if taken == "+":
        chislo1 = chislo1 + chislo2
        print(f"результат: {chislo1}")
    elif taken == "-":
        chislo1 = chislo1 - chislo2
        print(f"результат: {chislo1}")
    elif taken == "*":
        chislo1 = chislo1 * chislo2
        print(f"результат: {chislo1}")
    elif taken == "/":
        if chislo2 == 0:
            print("На ноль не делим")
        else:
            chislo1 = chislo1 / chislo2
            print(f"результат: {chislo1}")
    elif taken == "stepen":
        chislo1 = chislo1 ** chislo2
        print(f"результат:{chislo1}")
    i += 1