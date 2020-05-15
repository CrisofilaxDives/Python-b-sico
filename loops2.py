# Loops 2
## Tratamos de encontrar el número más grande de una lista de números desorganizados

from random import sample

list_1 = sample(range(0, 1000), 100)
print(list_1)

numero_mas_grande = -1
print(f"Al comienzo, el número más grande es: {numero_mas_grande}")
for numero in list_1:
    if numero > numero_mas_grande:
        numero_mas_grande = numero
    print(numero_mas_grande, numero)

print(f"Ahora, el número más grande es: {numero_mas_grande}")

## Podemos usar este metodo para enumerar o contar cosas en una lista

list_2 = sample(range(0,500), 10)
print(list_2)
x = 0
print(f"Comienzo {x}")
for numero in list_2:
    x = x + 1
    print(f"{x}. {numero}")
print(f"Final {x}")

## Podemos sumar los elementos de la lista

list_3 = sample(range(0, 100), 20)
print(list_3)
x = 0
print(f"Al comenzar tenemos: {x}")
for y in list_3:
    x = x + y
    print(f"{x} {y}")
print(f"Al final tenemos: {x}")

## Teniendo el total podemos tener el promedio

list_4 = sample(range(0, 100), 10)
print(list_4)
x = 0
n_datos = len(list_4)

for y in list_4:
    x = x + y
    print(f"{x} {y}")
print(f"Tenemos un total de: {x}")
media = x / n_datos
print(f"Y tenemos un promedio de: {media}")

## Podemos filtrar datos con Loops 

list_5 = sample(range(0, 100), 10)
print(list_5)
for n in list_5:
    if n > 50:
        print(f"El número más grande es: {n}")

## Podemos buscar usando Booleans

list_6 = sample(range(0, 100), 10)
found = False
print(list_6)
for n in list_6:
    if n < 50:
        found = True
        print(found, n)
    else:
        found = False
        print(found, n)

## Con None
## En vez de tener "numero_mas_grande = -1" como indicador de que no hemos visto ningun numero,
## podríamos usar "None"
list_1 = sample(range(0, 1000), 100)
print(list_1)

smallest = None
print(f"Al comienzo, el número más pequeño es: {smallest}")
for n in list_1:
    if smallest == None:
        smallest = n
    elif n < smallest:
        smallest = n
    print(smallest, n)

print(f"Ahora, el número más pequeño es: {smallest}")

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')   