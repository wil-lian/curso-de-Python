'''
Tipos de datos incorporados
En programación, el tipo de datos es un concepto importante.

Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas diferentes.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de secuencia:	list, tuple, range
Tipo de mapeo:	dict
Establecer tipos:	set, frozenset
Tipo booleano:	bool
Tipos binarios:	bytes, bytearray, memoryview
Ninguno Tipo:	NoneType

'''

# obtener el tipo de dato con type
entero = 5
print(type(entero))

cadena = "hola mundo"
print(type(cadena))

flotante = 33.7
print(type(flotante))

complejo = 1j
print(type(complejo))

lista = ["banana", "orange", True, False, 1j, 9]
print(type(lista))

tupla = ("cherry", 1j, 7, 8,)
print(type(tupla))

rango = range(9)
print(type(rango))

diccionario = {"name": "william", "age": 30}
print(type(diccionario))
