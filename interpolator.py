def get_table():
    pass


# table: dict {x0 : f(x0)}
def LagrangeInterpolation(table, x):
    pass


# table: dict {x0 : f(x0)}
def NewtonInterpolation(table, x):
    pass


if __name__ == "__main__":
    print("Задача алгебраического интерполирования\n"
          "Интерполяционный многочлен в форме Ньютона и в форме Лагранжа\n")
    print("Вариант №6")
    print("f(x): x^2 / (1 + x^2)\n"
          "a = -0.5, b = 1\n"
          "m+1 = 31, n = 8")
    func = lambda y: y ^ 2 / (1 + y ^ 2)
    values = int(input("Введите число значений в таблице (m+1): "))
    m = values - 1
    a = float(input("Введите A (начало отрезка): "))
    b = float(input("Введите B (конец отрезка): "))
    x = float(input("Введите X (точка интерполирования): "))
    n = int(input("Введите N (степень интерполяционного многочлена, не превышающая m): "))
    while n > m:
        n = int(input("Получено недопустимое значение n, введите другое: "))
