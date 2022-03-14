from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # Оператор + порождает результат типа Vector
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Мы можем также реализовать оператор *, выполняющий умножение на скаляр
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Ни один из реализованных специальных методов (кроме __init__) не вызывается напрямую
# внутри самого класса или при типичном использовании класса
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print(v3)
print(abs(v2 * 3))
