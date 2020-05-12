# Tuples avanzadas

tuple_1 = (1, 2, 3)
 
## Usando tuple()
tuple_2 = tuple((4, 5, 6))

## Métodos
### dir() para mirar lo que se puede hacer con una Tuple
# print(dir(tuple_1))

## Si se pone un solo dato, no es considerado un Tuple
tuple_3 = (2)
print(tuple_3)
print(
    type(tuple_3)
)
## Para especificar un Tuple de un solo elemento, ponle una coma
tuple_4 = (1,)
print(tuple_4)
print(
    type(tuple_4)
)

## Hacer print() según indice
print(tuple_1[1])

## Usar "del" para eliminar un Tuple
# del tuple_1
# print(tuple_1)
