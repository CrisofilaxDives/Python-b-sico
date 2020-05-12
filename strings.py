#Strings avanzados

myStr = "Hola Mundo"
#Con la función dir() podemos saber que se puede hacer con un tipo de dato
#Usando Control+Shift+P y escribiendo "comment", al darle click a Add comment line,
#las lineas seleccionadas se volveran comentarios
# print(
#     dir(myStr)
# )

#Los Strings tienen propiedades y métodos dentro de ellos con los cuales podemos trabajar
#Usemos el método upper() que hace que todos los caracteres esten en mayúsculas
print(myStr.upper())

#lower() sirve para poner todo en minuscula
print(myStr.lower())

#swapcase() intercambia el orden entre minusculas y mayúsculas
print(myStr.swapcase())

#capitalize() pone la primera letra de cada String en mayúscula, y el resto en minusculas
#capitalize() no funciona si hay un signo antes de la primera palabra, pero si convierte el resto
print(myStr.capitalize())

#replace() sirve para reemplazar una parte de un String por lo qué designemos
print(myStr.replace("Hola", "Hey"))

#Se pueden usar diversos métodos juntos, llamado método encadenado
#Se ejecuta el primer método y luego el segundo
print(myStr.replace("Hola", "qué tal").upper())

#count() sirve para contar caracteres de un String
print(myStr.count("o"))

#startswith() sirve para saber si un conjunto de caracteres es el que comienza el String
print(myStr.startswith("Hola"))
print(myStr.startswith("Hello"))

#endswith() sirve para lo contrario de startswith()
print(myStr.endswith("Mundo"))
print(myStr.endswith("Mundos"))

#split() sirve para dividir un String por defecto en un "espacio" y no funciona con 1 palabra
print(myStr.split())
string_1 = "Papaya"
string_2 = "Coco"
string_3 = "A E I"
print(string_1.split())
print(string_2.split())
print(string_3.split())
#También se le puede indicar por donde hacer el split()
string_4 = "Huevos,Leche"
print(string_4.split(","))
print(string_1.split("y"))

#find() busca los caracteres que se quieran en un String y te dice, en que indice o posición esta. De 0 a ...
print(myStr.find("H"))

#len() sirve para saber el tamaño de un String
print(
    len(myStr)
)

#index() sirve para saber la posición o indice de un caracter en un String
print(myStr.index("M"))

#isnumeric() sirve para saber si un String es un número, pero solo enteros sin letras ni simbolos
print(myStr.isnumeric())
string_5 = "23"
string_6 = "1.6"
string_7 = "1 y 6"
string_8 = "Y 2 pescados"
string_9 = "1 X"
string_10 = "X 24"
string_11 = "X-24"
string_12 = "24-X"
string_13 = "X-24-y"
string_14 = "45-Y-86"
print(string_5.isnumeric())
print(string_6.isnumeric())
print(string_7.isnumeric())
print(string_8.isnumeric())
print(string_9.isnumeric())
print(string_10.isnumeric())
print(string_11.isnumeric())
print(string_12.isnumeric())
print(string_13.isnumeric())
print(string_14.isnumeric())

#isalpha() sirve para saber si un String es alfabetico, si hay espacios o número = False
print(string_5.isalpha())
print(string_6.isalpha())
print(string_7.isalpha())
print(string_8.isalpha())
print(string_9.isalpha())
print(string_10.isalpha())
print(string_11.isalpha())
print(string_12.isalpha())
print(string_13.isalpha())
print(string_14.isalpha())
print(myStr.isalpha())
print(string_1.isalpha())

#Usando print(string["cualquier número"]) podemos elegir la posición de lo que queramos print()
print(myStr[3])
#Usando números negativos podemos comenzar desde el últmo caracter del String
print(myStr[-1])

#Otras formas de print() con Strings
print(myStr + ", bienvenido.")
#Al hacer esto print(f"{myString}, bienvenido.") podemos saltarnos la concatenación, al hacer que dentro
#del String aún funcione la variable "myStr" al poner antes de las comillas f
print(f"{myStr}, bienvenido.")
#Otra forma usando format()
print("{0}, bienvenido.".format(myStr))