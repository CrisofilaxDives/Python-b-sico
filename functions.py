# Funciones

# Hemos usado varias funciones ya: print(), dir(), len(), type()
# Para crear una función debemos usar la palabra clave "def" luego el nombre de la función,
# "()" y por último ":"
# def hola():
#     print("¡Hola Mundo!")

# hola()

# Podemos hacer más avanzada la función al darle un parametro
# def hola(nombre):
#     print(f"Hola, {nombre}")

# hola("David")

# En caso de no rellenar, nos dará error, asi que de esta manera podemos darle un valor predefinido
# def hola(nombre = "usuario"):
#     print(f"Hola {nombre}")

# hola()

# Podemos hacer que la función nos devuelva un dato usando "return"
# def suma(n1, n2):
#     return n1 + n2

# print(suma(2, 3))

# Otra forma de crear funciones es usando "lambda"
suma = lambda n1, n2: n1 + n2 

print(suma(3, 8))
    
