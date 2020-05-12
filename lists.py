#List avanzadas

#Se pueden crear Lists usando list()
list_1 = list("Limon")
print(list_1)
# list_2 = list("Limón", 2, 2.5, True, None)
# print(list_2)
#Se genera un error, porque list() solo resiste un argumento, o sea, 1 integer, float, string, boolean o none
#Para poder hacerlo se necesita usar tuple
list_2 = list((1, 1.5, "Limón", None, True))
print(list_2)

#Listas basadas en rangos por range()
#Funciona dandole un rango de donde comienza a un número antes de donde termina
#Luego, se usa list() para crear un List con ese rango
rango = list(range(1, 11))
print(rango)

#Para saber que se puede hacer con un List, se usa dir()
# print(dir(rango))
##len()
print(
    len(list_2)
)
##print() según número de indice
print(list_2[2])
##O con el indice inverso
print(list_2[-1])
##usar "in" para saber si hay algo en el List
print(1 in list_2)
print(2 in list_2)
##Se puede reemplazar elementos de la List
list_2[1] = 1.6
print(list_2)

#Métodos de las List
##append() para agregar nuevos elementos a la List
##Solo puede ser 1
list_2.append("Huevo")
print(list_2)
##extend() para agregar más elementos por medio de un Tuple o List
list_2.extend((3, 2.6, False))
print(list_2)
##insert() para agregar un elemento en un indice deseado
##Puede hacerse con el indice inverso o con len() que nos dará la longitud total del List, o sea, 
##quedará de último
list_2.insert(3, "Pera")
print(list_2)
list_2.insert(-1, 153)
print(list_2)
list_2.insert(len(list_2), "Fin")
print(list_2)
##pop() paar quitar elementos de una List
##Si no se le indica, quitara solo el último elemento
list_2.pop()
print(list_2)
list_2.pop(3)
print(list_2)
##remove() para quitar items especificos del List
list_2.remove("Huevo")
print(list_2)
##clear() para limpiar la lista
# list_2.clear()
# print(list_2)
##sort() paar ordenarlos alfabeticamente solo Strings
##Los Strings no alfabeticos van de primera
list_3 = ["Papas", "Huevos", "Salchicha", "1"]
print(list_3)
list_3.sort()
print(list_3)
###Usando reverse=True, hacemos que se organize al revez
list_3.sort(reverse=True)
print(list_3)
##index()
print(list_3.index("Papas"))
##count()
print(list_3.count("Huevos"))