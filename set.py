# Tipo de dato: Set

#Sets son conjuntos de datos sin indices como los List o Tuples
set_1 = {"perro", "gato", "iguana"}
print(set_1)
print(
    type(set_1)
)

# Usar "in" para imprimir si un item esta dentro del set. True o False
print("perro" in set_1)

# add() para añadir items al inicio del Set
set_1.add("canario")
print(set_1)

# remove() para quitar items especificos
set_1.remove("canario")
print(set_1)

# clear() para limpar un Set
# set_1.clear()
# print(set_1)

# Usar "del" para eliminar el Set
# del set_1
# print(set_1)