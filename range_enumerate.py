#20
"""
for valor in range(20): # asi imprimira del 0 al 19  ya que el (20), no lo incluirá
    print(valor)
"""
    
"""
for valor in range(21): # aqui si imprimira el 0 al 20 ya que el (21) no lo incluye
    print(valor)
"""   

"""
for valor in range(10,21):# aqui imprimira del 10 al 20 , ya que nuevamente el (21) no es incluyente
                          # limite inferior 10 si es incluyente y el superior  20 no 
    print(valor)
"""

#range recibe un tercer parametro que es opcional
#por defecto se incrementa de 1 en 1 la iteracion

"""
for valor in range(1,31,2): # con esto le estoy diciendo que se incrementa de 2 en 2  
                            # desde  el 1 hasta el 30  sin contar el 31 ya que no se incluira
                            # imprimira los numeros impares ya que empieza del 1
    print(valor)
"""

"""
lista =[1,2,3,4,5,6,7,8]

for valor in range(len(lista)): # el tamaño de la lista
    print(lista[valor]) # valor representa la posicion que tiene la lista
    
"""

"""
lista = [1,2,3,4,5,6,7,8]
for valor in range(len(lista)):
    print(valor) # asi imprimira solo la posicion de los elementos  de la lista
    
"""

"""
lista = [1,2,3,4,5,6,7,8]
for valor in enumerate(lista): # enumerate recibe un objeto iterable 
    print(valor)
"""

lista = [1,2,3,4,5,6,7,8]
for posicion, valor in enumerate(lista):
    print("El Valor {0} esta en la posición {1}".format(valor,posicion)) # asi se formatea una cadena
