# Функция collections.namedtuple – это фабрика, порождающая подклассы
# tuple, дополненные возможностью задавать имена полей и имя класса; это помогает при отладке.
from collections import namedtuple

# Для создания именованного кортежа нужно задать два параметра: имя
# класса и список имен полей; последний может быть любым итерируемым объектом, содержащим строки,
# или одной строкой, в которой имена перечислены через запятую
City = namedtuple('City', 'name country population coordinates')
# Данные передаются конструктору в виде позиционных аргументов (тогда
# как конструктор кортежа принимает единственный итерируемый объект).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# К полям можно обращаться по имени или по номеру позиции.
print(tokyo)
print(tokyo.population)

# _fields – кортеж, содержащий имена полей данного класса
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make() позволяет создать экземпляр именованного кортежа из итерируемого объекта;
# конструктор City(*delhi_data) делает то же самое.
delhi = City._make(delhi_data)
delhi2 = City(*delhi_data)
print(delhi)
print(delhi2)
# _asdict() возвращает объект collections.OrderedDict, построенный по
# именованному кортежу.
print(delhi._asdict())
