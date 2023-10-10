def get_table(a, b, m, func):
    step = (b - a) / m
    table = {}
    for j in range(0, m + 1):
        z = a + j * step
        table[z] = func(z)
    return table


def sort_table(table):
    table_sorted = {k: v for k, v in sorted(table.items(), key=lambda item: abs(item[1] - x))}
    table_sorted_keys = list(table_sorted.keys())
    table_new = {}
    i = 0
    while i <= n:
        table_new[table_sorted_keys[i]] = table_sorted[table_sorted_keys[i]]
        i += 1
    return table_new


def print_table(table):
    print("     x    |    f(x)")
    for key in table.keys():
        if key >= 0:
            print(" " + "{:.6f}".format(key), end=" | ")
        else:
            print("{:.6f}".format(key), end=" | ")
        if table[key] >= 0:
            print(" " + "{:.6f}".format(table[key]))
        else:
            print("{:.6f}".format(table[key]))


# table: dict {x0 : f(x0)}
def LagrangeInterpolation(table, x, n):
    args = list(table.keys())
    res = 0
    for k in range(0, n + 1):
        x_k = args[k]
        x_k_value = table[x_k]
        local_res = 1
        for i in range(0, n + 1):
            if k != i:
                local_res *= (x - args[i]) / (args[k] - args[i])
        res += x_k_value * local_res
    return res


#get divided differences
def GetDiv(table, arguments):
    if len(arguments) == 2:
        return (table[arguments[1]] - table[arguments[0]])/(arguments[1] - arguments[0])
    else :
        numOfArguments = len(arguments)
        return (GetDiv(table, arguments[1 : numOfArguments]) - GetDiv(table, arguments[0 : numOfArguments - 1]))/(
            arguments[numOfArguments - 1] - arguments[0])

# table: dict {x0 : f(x0)}
def NewtonInterpolation(table, x, n):
    arguments = list(table.keys())
    result = 0
    rightMultiplicant = 1

    pairIndex = 0
    result += table[arguments[0]]
    for arguementValuePair in table:
        if pairIndex == 0:
            pairIndex += 1
            continue

        rightMultiplicant *= (x - arguments[pairIndex - 1])
        leftMultiplicant = GetDiv(table, arguments[0 : pairIndex + 1])
        result += leftMultiplicant * rightMultiplicant
        pairIndex += 1
    return result

if __name__ == "__main__":
    print("Задача алгебраического интерполирования\n"
          "Интерполяционный многочлен в форме Ньютона и в форме Лагранжа\n")
    print("Вариант №6")
    print("f(x): x^2 / (1 + x^2)\n"
          "A = -0.5, B = 1\n"
          "m+1 = 31, n = 8")
    func = lambda y: y ** 2 / (1 + y ** 2)

    exit_program = False

    while not exit_program:
        args_count = int(input("Введите число значений в таблице (m+1): "))
        m = args_count - 1
        a = float(input("Введите A (начало отрезка): "))
        b = float(input("Введите B (конец отрезка): "))

        table = get_table(a, b, m, func)
        print()
        print_table(table)
        print()

        x = float(input("Введите X (точка интерполирования): "))
        n = int(input("Введите N (степень интерполяционного многочлена, не превышающая m): "))
        while n > m:
            n = int(input("Получено недопустимое значение n, введите другое: "))

        sorted_table = sort_table(table)
        print()
        print_table(sorted_table)
        print()

        lagrange = LagrangeInterpolation(sorted_table, x, n)
        print(f"L({x}) = {lagrange}")
        print(f"|f(x)-L(x)|: {abs(func(x) - lagrange)}")
        print()

        newton = NewtonInterpolation(sorted_table, x, n)
        print(f"N({x}) = {newton}")
        print(f"|f(x)-N(x)|: {abs(func(x) - newton)}")
        print()

        exit_program = input('Завершить программу? (y/n): ').lower().strip() == 'y'
        print()
