#17
"""

lista = [1,2,3,4,5,6,7,8,9,10]
tupla =("Hola", "Luisvmpcl", "Instagram")

lista_to_tupla = tuple(lista)   #convertir una lista en tupla   #palabra reservada
tupla_to_list = list(tupla) # convierte una tupla en lista  # palabra reservada list
print(lista_to_tupla)   # al momento de imprmir nos deberia imprimir como una lista ejemplo (1,2,3,4,5,6, etc)
#print(tupla_to_list) # imprimira una lista   ['Hola', 'Luisvmpcl', 'Instagram']
"""

"""
lista = [1,2,3,4,5,6,7,8,5,5,5,5,5]
lista2 = ["Ventocilla.pe", "Luis"]

lista.append(900) # asi agregando un elemento a la lista claro lo  coloca en la ULTIMA POSICION
lista.insert(4, "Luis Ventocilla") 
#asi estamos añadiendo un elemento a la lista en la posicion 3 y el 4 es la posicion, Luis Ventocilla es el valor

#print(lista)
print(lista2)
"""


"""
# para eliminar valores de una lista
lista = [1,2,100,4,5,6,7,8,5,5,5,5,5,200]
#lista.remove(100)  # asi estariamos eliminando al 100
#lista.pop() #elimina la ultima posicion
lista.pop(6) # asi elimina una posicion especifica en este caso seria el 7
print(lista)
"""

"""
# para limpiar elementos de una lista
lista = [1,2,3,4,5,6,7,8,5,'Ventocilla',5,5,5]
#lista.clear()
#print(lista)
valor =lista.pop(4)  # pop retorna el valor eliminado de dicha posicion que hayamos elejido
print(valor)
"""


"""
# para saber cuantas veces se repite un elementos
lista = [1,2,3,4,5,6,7,8,5,'Ventocilla',5,5,5,5,5,5,5,5,5,5]
cantidad = lista.count(5) 
print(cantidad)
"""

"""
# para unir elementos de una lista a otra o viceversa
lista = [1,2,3,4,5,6,7,8,5,5,5,5,5]
lista2 = ["Ventocilla.pe", "Luis"]
lista.extend(lista2)
print(lista)
"""


lista = [1,2,3,4,5,6,7,8,5,5,5,5,5]
lista2 = ["Ventocilla.pe", "Luis"]
lista2 = lista.copy() # es similar a lista2 = lista
#lista2 = lista # estamos igualando lista2 con lista los elementos
print(lista2)

