#Variables
name = "David"
print(name)
#Se puede hacer con cualquier tipo de dato
age = 24
print(age)
compras = ["Arroz", "Carne", "Papas"]
print(compras)
#Gracias al "case sensitive", los nombres de las variables se discriminan entre si
#No es lo mismo, Age que age
#No se puede comenzar un nombre de variable con un número, pero se puede hacer asi: _1age o age_1.
#Esto son convenciones. Otras son Snake case, Camel case y Pascal case.
#La convención más usada es Snake case: book_name
#Podemos ahorrar tiempo nombrando variable asi:
weight, height = 68, 1.71
print(weight)
print(height)
#También se puede imprimir en una sola linea:
print(weight, height)

#Constantes
#Una de ellas es pi, ya que nunca cambia. Las variables constantes se escriben en mayúscula: PI = 3.14
PI = 3.1416
MY_LASTNAME = "Maldonado"

#El valor de las variables siempre puede cambiar.
print(name)
name = "Alejandro"
print(name)