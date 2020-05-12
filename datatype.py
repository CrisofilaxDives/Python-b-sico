print("Hello World!") #"Hello World!" es un tipo de datos llamado String o cadena de datos o de caracteres
print("Hello World!") #Un tipo de datos String
print("Hello world!") #Es un String, pero diferente, ya que se diferencia por la "w", ya que es un caracter diferente
print('Hello World!') #Usar comillas simples '' tambien nos puede ayudar a definir un String
print('''Hello World!''') #Usar triple comillas simples para definir Strings
print("""Hello World!""") #Triples comillas dobles para definir Strings

type("Hello World!") #type() sirve para saber el tipo de dato que se quiera. "str" es String
type(100) #Nos dira "int" o Integer o Entero, ya que es un numero
print(100) #Se puede hacer print() de un Integer
print("100") #Tambien se puede hacer print() de un String con los caracteres "100"
print(
    type("Hello World!") #Si funciona
)

print("Good" + "Bye") #Se pueden unir Strings usando "+", esto se llama concatenación 
print("Good" + " " + "Bye"+ "!") #probaré si se puede concatenar más de dos string, si se puede
print(13 + 17) #"+" entre dos Integer es una suma

print(
    type(10.5) #10.5 no es un Integer porque es un decimal, asi que type() nos dira que es class "float"
) 

print(
    type(True)
    ) #son dos estados de datos, que definen el tipo de dato Boolean, es un tipo de dato lógico.
print(
    type(False)
    ) 

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #para agrupar datos en un tipo de dato llamado List, debemos usar llaves []
#separando los datos con comas
["Limón", "Naranja", "Uva"] #Tambien puede hacerse con Strings
[12.2, 12.3, 12.4] #Floats
[False, False, True] #También Booleans
[56, "Granadilla", 2.5, True] #O combinados
print(
    type(
        [1, 2]
    )
)
#Las listas estan hechas de distintos items o elementos

(45, 55, 60) #esto es una tupla o Tuple, es una forma de agrupar datos inmutables, que no se
#podran cambiar una vez definidos. Un Tuple se define entre ()
print(
    type(
        (45, 55, 60)
    )
)

#esto es una prueba
print("mi" + " " + "amor" + " " + "por" + " " + "Juli" + " " + "siempre" + " " + "crece")
print(
        type(
                ("mi", " ", "amor", " ", "por", " ", "Juli", " ", "siempre", " ", "crece"))
)

print(
    type(                           
        {                           #Este es un tipo de agrucpación que crea el tipo de dato Dictionary
            "nombre":"david",       #Que genera un class 'dict', cada seccion se debe separar con comas         
            "apellido":"maldonado"  #estos se conocen como clave y valor o key y value
        }
    )
)
print(
    {
        "fruta":"limón",
        "origen":"colombia"
    }
)

print(
    type(None)  #None es un tipo de dato NoneType, un dato que no esta, faltante, que no existe
)
print(None)