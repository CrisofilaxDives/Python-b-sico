#Números avanzados

#Operaciones
##Se puede hacer entre Floats e Integers
##Suma
print(1 + 1)

##Resta
print(145 - 27)

##Multiplicación
print(5 * 9)

##División
print(8 / 3)
##Esta es una división que nos devuelve el número entero
print(5 // 2)
##Operador de módulo
##Esta es una división que solo nos devuelve el residuo
print(8 % 3)

##Exponenciación
print(5 ** 3)

##Orden de las operaciones
##Primero las exponenciales, luego multiplicaciones o diviciones, por último, resta y suma
print(20 - 10 / 5 * 3 ** 2)
##Se puede hacer uso de los parentesis
print((20 - 10) / (5 * 3 ** 2))

#Usos de los números
##Insertar números por médio de input()
edad = input("Inserta tu edad: ")
print(edad)
print(
    type(edad)
)
##Los datos insertados se pueden manipular
# nueva_edad = edad + 5 
# print(nueva_edad)
##Esto da error, porque todo lo que se inserte en un programa, es un String
##Se puede convertir un String en un Integer usando int()
# nueva_edad = int(edad) + 5
# print(nueva_edad)
##Para prevenir errores, por ejemplo al poner letras, podemos usar int()
nueva_edad = int(edad) + 5
print(nueva_edad)
print(
    type(nueva_edad)
)