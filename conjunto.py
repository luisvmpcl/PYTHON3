#19
"""
 #conjunto = set()
conjunto = { 1,2,3}
conjunto.add(10) # para añadir un elemento al conjunto,, los conjuntos son aleatorios es decir desordenandos
conjunto.add("Luis Ventocilla")
print(conjunto)

"""
"""
#regla: no existe elementos repetidos dentro de un conjunto
conjunto = { 1,2,4,4,4,4,4,5,6,7,6,5,5,5,6}
print(conjunto) # imprimira sin los elementos repetidos
"""


"""
#convertir una lista en conjunto

lista = [1,2,3,4,5,6,7,8,8,8,8,8,3,3,3,2]
print(lista)
conjunto = set(lista)
print(conjunto)
"""

"""
#convertir una conjunto en lista
conjunto = {1,2,3,4,5,6,7,8,8,8,8,8,3,3,3,2}
print(conjunto)
#conjunto = set(conjunto)
#lista = list(conjunto)
#print(lista)

conjunto =list(set(conjunto)) # hace lo mismo en una sola linea
print(conjunto)
"""


"""
# para verificar las pertenencias en un conjunto
conjunto = {1,2,3,4,5,6,7,8,9,8,7,6,5,5,6,4,3,2}
print(conjunto)
pertenencia = 3 in conjunto
print(pertenencia)

"""

"""
# para verificar las pertenencias en un conjunto
conjunto = {1,2,3,4,5,6,7,8,9,8,7,6,5,5,6,4,3,2}
print(conjunto)
pertenencia = '2'  not in conjunto #
print(pertenencia)

"""

cadena = "Mi nombre es Luis Ventocilla , Agradecido con Dios Siempre"
cadena = set(cadena) #lo convierte en conjunto
print(cadena) # imprimirá los caracteres pero no repetidos a menos que se mayuscula  tambien el espacio '' y la coma ,



