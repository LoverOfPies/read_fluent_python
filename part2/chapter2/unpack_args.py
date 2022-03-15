# В этом контексте префикс * можно поставить только перед одной переменной,
# которая, впрочем, может занимать любую позицию
a, b, *rest = range(5)
print(rest)

a, b, *rest = range(2)
print(rest)

a, *body, c, d = range(5)
print(body)
