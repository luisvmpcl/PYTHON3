#11
ista =['Facebook', 'Twitter', 'Instagram','Whatsapp'] # dentro de las listas van los elementos
lista2 = ['Luisvmpcl.pe', 30 , True, 14.7]

#          0                   1
lista3 =['lista',['Facebook', 'Twitter', 'Instagram','Whatsapp']]         #agregando una lista dentro de una lista
#print(lista3)
"""
para imprimir los elementos individualmente
            0         1           2          3
lista ['Facebook', 'Twitter', 'Instagram','Whatsapp']
Formula  : posicion_final = n -1 , donde n : numero de elementos de la lista
"""

#print(lista[3])
#print(lista3[1])
#print(lista3[1][3])  # asi imprimimos a la lista3 =['lista',['Facebook', 'Twitter', 'Instagram','Whatsapp']] 

#lista3 =['lista',['Facebook', 'Twitter', 'Instagram','Whatsapp'],'']         #agregando ELEMENTOS A UNA LISTA  , OJO ESTA NO ES LA MANERA DE HACERLO
#lista3[2]=20
lista3 =['lista',['Facebook', 'Twitter', 'Instagram','Whatsapp']]
lista3.append(20)
lista3.append('Agregando elementos a la lista')   #se le conoce como listas dinamicas o arreglos dinamicos



print(lista3)


