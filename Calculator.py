while True:
    try:
        operation = int(input(f"\n___Меню для пользователя___\n"
                              f"1 - сложение\n"
                              f"2 - вычитание\n"
                              f"3 - деление\n"
                              f"4 - умножение\n"
                              f"5 - возведение в степень\n"
                              f"6 - остаток от деления\n"
                              f"7 - целочисленное деление\n"
                              f"0 - остановка программы\n"
                              f"Выбери действие: "))

        if operation == 0:
            print("Good by")
            break

        if operation < 1 or operation > 7:
            print("Такого пункта нет в меню")
            continue

        num_1 = float(input(" введите 1ое число "))
        num_2 = float(input(" введите 2ое число "))

        if operation == 1:
            print(num_1 + num_2)
        elif operation == 2:
            print(num_1 - num_2)
        elif operation == 3:
            try:
                print(num_1 / num_2)
            except ZeroDivisionError:
                print("Error2: на ноль делить нельзя")
        elif operation == 4:
            print(num_1 * num_2)
        elif operation == 5:
            print(num_1 ** num_2)
        elif operation == 6:
            try:
                print(num_1 % num_2)
            except ZeroDivisionError:
                print("Error2: на ноль делить нельзя")
        elif operation == 7:
            try:
                print(num_1 // num_2)
            except ZeroDivisionError:
                print("Error2: на ноль делить нельзя")

    except ValueError:
        print("Error1: нужно вводить числа")
