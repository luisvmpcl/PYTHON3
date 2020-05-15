#17

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla =("Hola", "Luisvmpcl", "Instagram")

lista_to_tupla = tuple(lista)   #convertir una lista en tupla   #palabra reservada
tupla_to_list = list(tupla) # convierte una tupla en lista  # palabra reservada list
#print(lista_to_tupla)   # al momento de imprmir nos deberia imprimir como una lista ejemplo (1,2,3,4,5,6, etc)

print(tupla_to_list) # imprimira una lista
"""

lista = [1,2,3,4,5,6,7,8,5,5,5,5,5,]
lista2 = ["Ventocilla.pe", "Luis"]

lista.append(15) # asi agregando un elemento a la lista claro lo  coloca en la ultima posicion
lista.insert(3, "Luis Ventocilla") # asi estamos añadiendo un elemento a la lista en la posicion 2    # el 3 es la posicion  y Luis Ventocilla el valor

# para eliminar valores de una lista
#lista.remove(3) 
#lista.pop() #elimina la ultima posicion
#lista.pop(2) # asi elimina una posicion especifica

# para limpiar elementos de una lista
#lista.clear()
#valor =lista.pop(4)  # pop retorna el valor eliminado
#print(valor)


# para saber cuantas veces se repite un elementos
cantidad = lista.count(5) 
print(lista)

# para unir elementos de una lista a otra o viceversa
#lista.extend(lista2)
#print(lista)

lista2 = lista.copy() # es similar a lista2 = lista
#lista2 = lista
print(lista2)