# try / except

# Son unos condicionales usadoas para evitar los problemas en códigos donde se espera tenerlos.
# Un ejemplo es un int(input()) al ingresarle letras o simbolos
# Si el código en el "try" funciona, "except" se evitara
# Si el código en el "try" no funciona, se salta al "except"

while True:
    try: 
        number = int(input("Ingrese un nuúmero: "))
        break
    except:
        print("Hubo un error")

# Se puede usar "while True" para generar un bucle y asi volver a ingresar la información

# También tenemos el operador lógico "!=", que sirve para indicar que algo no es igual a:

x = 24
if x != 24:
    print("No es un 24")
else:
    print("Es un 24")

# Se puede usar exit() para terminar con un proceso