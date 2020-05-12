# Modulos
# Los modulos son conjutos de código que nos evitan escribirlo nosotros mismos
# Existen 3 tipos: los nuestros, los de otras personas, los de Python
# Para usar un modulo de Python usamos "import"
# En https://docs.python.org/3/py-modindex.html
# podemos ver todos los modulos disponibles en Python
# Y en https://pypi.org/
# podemos descargar modulos hechos por otras personas o empresas

# Probemos con datetime
# Se puede googlear su información:
# https://docs.python.org/3/library/datetime.html

# import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes = 130))

# También podemos usar otro método para poder usar ciertas funciones dentro del modulo

from datetime import timedelta, date

print(timedelta(minutes = 170))
print(date.today())

from fmath import suma, resta

suma(5, 8)
resta(8, 3)

# Para instalar un modulo de otras personas, usamos la consola con el comando pip install "nombre del
# paquete", pe. colorama

from colorama import Fore, Style, init
init(convert = True)
print(Fore.RED + "Hola")

# Existen muchos modulos, como Flask para crear aplicaciones web como Django, que son framework.
# Tkinter para crear interfaces gráficas de usuario