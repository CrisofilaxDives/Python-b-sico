# Loops, For and While

comidas = list(("Peras", "Mangos", "Bananos", "Sandia"))

# Para hacer print() de cada uno de los elementos podríamso hacer esto:
print(comidas[0])
print(comidas[1])
print(comidas[2])
print(comidas[3])

# Pero si agregamos un objeto más, nos toca hacer lo mismo:
comidas.append("Lulo")
print(comidas[4])

# Podemos evitarnos, digitar cada vez usando, bucles o iteradores
## "for", que usa una variable que indica cada una de las partes, "in" que indica en donde y la variable
## de la lista, ":" y luego lo que se quiere hacer.
## En si, "for" recorre cada elemento de la lista. 
## Además, funciona también con condicionales
for comida in comidas:
    if comida == "Mangos":
        print("Tienen descuento")
    print(comida)
## Para terminar la ejecución del "for", debemos usar "break", en un punto inferiora lo nombrado como
## la opción para parar
numeros = list(range(1, 50))
for numero in numeros:
    print(numero)
    if numero == 10:
        break
## También podemos usar "continue" para seguir la ejecución del "for"
numeros_1 = list(range(1, 100))
for numero_1 in numeros_1:
    print(numero_1)
    if numero_1 == 9:
        continue
    elif numero_1 == 11:
        break 

# Otro condicional es "while" que repite el codigo en el que esta inscrito:
cuenta = 5
while cuenta <= 10:
    print("Te amo Juli")
    cuenta = cuenta + 1 
# Si no ponemos que cuenta = cuenta + 1, se generara un bucle infinito
