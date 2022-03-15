# Кортеж, в который распаковывается выражение, может содержать вложенные
# кортежи, например (a, b, (c, d)), и Python правильно заполнит их,
# если выражение соответствует структуру вложенности.

# Каждый кортеж содержит четыре поля, причем последнее – это пара координат
metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# Присваивая последнее поле кортежу, мы распаковываем координаты
for name, cc, pop, (latitude, longitude) in metro_areas:
    #  Условие if longitude <= 0: отбирает только мегаполисы в Западном полушарии
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
