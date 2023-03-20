# las variables se declaran sin asignar el tipo
x = 5
y = "jhon"
print(x)
print(y)


# se pueden volver a asigar nuevos valores a otra variable ya establesida
z = 8
z = "william"
print(z)


# podemos asignar el tipo de valor
a = str("34343")
b = int(454)
c = float(232)


# o tambien para obtner el tipo de dato
print(type(a))
print(type(b))
print(type(c))


# las variables se pueden declarar con comillas simples o dobles
x = 'william'
print(x)
x = "william"
print(x)


# las variables en mayusculas o minisculas se distinguen en python
a = 4
A = "william"
print(a)
print(A)

"""Nombres de variables"""
"""
Nombres de variables
Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (edad, nombre del coche, volumen_total). Reglas para las variables de Python:
Un nombre de variable debe comenzar con una letra o el carácter de subrayado
Un nombre de variable no puede comenzar con un número
Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _)
Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, Edad y EDAD son tres variables diferentes)
Un nombre de variable no puede ser ninguna de las palabras clave de Python ."""

# camel case
myVariableName = "fabricio"

# pascual case
MyVariableName = "tito"

# snake case
my_variable_name = "vargas"


"""Asignar valores multiples"""
# asignar multiples valores en una sola linea
x, y, z = "orange", True, 3
print(x)
print(y)
print(z)

# un valor para multiples variables
x = y = z = "yellow"
print(x)
print(y)
print(z)

# Desenpaquetar una coleccion
frutas = ["banana", "orange", "cherry"]
a, b, c = frutas
print("Desenpaquetando una coleccion")
print(a)
print(b)
print(c)

'''Variables de Salida'''
g = "Python is awesome"
print(g, x, y)
# tambien podemos utilizar el operador + para generar multiples variables
print(g + x + y)

# para numeros el operador  + funciona como operador matematico
r = 7
u = 8
print(r + u)

# nos puede mandar error cuando tratamos de sumar un numero y un string
# f = 6
# i = "hola"
# print(f + i)

'''Variables Globales'''
'''Las variables que se crean fuera de una funcion se las conoce como
variables globales'''
n = "awesome"


def myFunc():
    print("Python is: " + n)


myFunc()

# variables global con el mismo nombre de la variable de una funcion
print("Esta es otro ejemplo")
q = "awesome"


def myFunc():
    q = "outfull"
    print("Python is: " + q)


myFunc()
print(q)

# la palabra clave global


def myFunction():
    global name
    name = "william"


myFunction()
print(name)

# para canbiar el valor de una variable global
# utilizar la varible global dentro de la funcion
name = "fabricio"


def myFunction():
    global name
    name = "william"


myFunction()
# el valor canbia a william de lo que era fabricio
print(name)
