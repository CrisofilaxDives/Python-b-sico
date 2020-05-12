# Control de flujo, Conditionals

# age = int(input("Introduzca su edad en años: ")) 

# Para poder hacer print() de un texto especifico al hacer input() de número y este sea menor o mayor,
# según tengamos definido, podemos usar "if" al comparar con otro valor
## "<" menor que
comparacion_ej_1 = 20 < 30
print(comparacion_ej_1)
## ">" mayor que
comparacion_ej_2 = 20 > 30
print(comparacion_ej_2) 
## "==" igual que
comparacion_ej_3 = 20 == 20
print(comparacion_ej_3)
## "<=" menor o igual que
comparacion_ej_4 = 20 <= 30
print(comparacion_ej_4)
## ">=" menor o igual que
comparacion_ej_5 = 20 >= 20
print(comparacion_ej_5)

# if age > 18:
#     print(f"{age} es mayor que 18.")
# if age < 18:
#     print(f"{age} es menor que 18.")
# if age == 18:
#     print(f"{age} es igual a 18.")

## Podemos usar "else", para indicar un caso contrario la "if"
# if age > 18:
#     print(f"{age} es mayor.")
# else:
#     print(f"{age} es menor.")

## Se puede hacer con Strings
# nombre = input("Escriba su nombre: ")
# nombre_lower = nombre.lower()
# if nombre_lower == "david":
#     print("Acceso concedido.")
# else:
#     print("Acceso denegado.")

## Se pueden hacer más comparaciones con "elif"
# fruta = input("Escriba su fruta preferida: ")
# fruta_lower = fruta.lower()
# if fruta_lower == "mango":
#     print("Genial")
# elif fruta_lower == "guayaba":
#     print("Super")
# elif fruta_lower == "tomate de arbol":
#     print("Qué asco")
# else:
#     print("Buena opción")

## Se pueden encadenar más de un "if", condicionales anidadas
# usuario = input("Escriba su usuario: ")
# if usuario == "pepe":
#     contraseña = input("Escriba su contraseña: ")
#     if contraseña == "contraseña":
#         print("Bienvenido")
#     else:
#         print("Contraseña invalida")
# else:
#     print("Usuario incorrecto")    

## Opereradores lógicos
##Podemos usar "and", "or", "not" para comparar dos veces algo
numero = int(input("Esciba un numero: "))
if numero > 1 and numero < 100:
    print("Correcto")
else:
    print("Incorrecto")
if numero > 1 or numero < 100:
    print("Correcto")
else:
    print("Incorrecto")
if (not(numero == 50)):
    print("Correcto")
else:
    print("Incorrecto")