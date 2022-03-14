colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# Генерирует список кортежей, упорядоченный сначала по цвету, а затем по размеру
tshirts = [(color, size) for color in colors
           for size in sizes]
print(tshirts)
