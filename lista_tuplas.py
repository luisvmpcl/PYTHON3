#24
# union d3 listas con tuplas

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union, union1, union2 = lista[0], lista[1],lista[2]
print(union)
print(union1)
print(union2)
"""

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union, union1, *union2 = lista # *union2 imprimira del 3 en edelante en este ejemplo es decir estamos distribuyendo los valores
print(union)
print(union1)
print(union2)

"""


##############  aqui recien estamos uniendo la lista con la tupla
"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union = zip(lista,tupla) # aqui unimos
print(union)#  no imprimira el objeto con su direccion de memoria  -----   <zip object at 0x00D552C8>
 """
 
"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union = list(zip(lista,tupla)) # aqui lo convierte en lista y lo une
print(union) # imprimira una lista y dentro de ella una tupla

"""

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union = tuple(zip(lista,tupla)) # aqui lo convierte en tupla y lo une
print(union) # imprimira una tupla y dentro de ella contiene las tuplas

"""

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')

union = dict(zip(lista,tupla)) # aqui lo convierte en diccionario   # NOTA  LOS DICCIONARIOS SOLO ACEPTA 2 VALORES
print(union) # imprimira un diccionario  , es muy util se queremos que apartir de aqui querramos trabajar con diccionarios

"""

"""
lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')
lista2 = ['12','14','15',(9,8,7)]

union = list(zip(lista,tupla,lista2)) 
print(union) 

"""


lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('Hola','Luis','Ventocilla','Mendoza','luisvmpcl.pe','Instagram')
lista2 = ['12','14','15',(9,8,7)]

union = tuple(zip(lista,tupla,lista2)) 
print(union) 

 

 
 
 
 