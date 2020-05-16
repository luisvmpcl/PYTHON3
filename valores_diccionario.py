#23
# para   recorrer y obtener multiple valores de un diccionario
"""
diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor

for clave,valor in diccionario.items(): # items  es un metodo de diccionario
    print("{0}-->{1} ".format(clave,valor))
    
"""

"""

diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor

for clave in diccionario:
    resultado = diccionario.get(clave, "No existe un valor asociado a esta clave o no existe esta clave")
    print(resultado)  
"""
  
"""

diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor

for clave,valor in diccionario.items():
    #print("{0}--> {1} ".format(clave,valor))  
    pass  # para que no haga nada en esta linea de codigo
    
for clave in diccionario:
    resultado = diccionario.get(clave, "No Existe un valor asociado a esta clave o no existe esta clave")  
   # print(resultado)

#para obtener solo los valores de un diccionario
valores = diccionario.values() # values es una funcion que contiene los diccionarios en python
print(valores)

"""


"""

diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor

for clave,valor in diccionario.items():
    #print("{0}--> {1} ".format(clave,valor))  
    pass  # para que no haga nada en esta linea de codigo
    
for clave in diccionario:
    resultado = diccionario.get(clave, "No Existe un valor asociado a esta clave o no existe esta clave")  
   # print(resultado)

#para obtener solo los valores de un diccionario
for valor in diccionario.values():# values es una funcion que contiene los diccionarios en python
    print(valor)
    
"""


diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor

for clave,valor in diccionario.items():
    #print("{0}--> {1} ".format(clave,valor))  
    pass  # para que no haga nada en esta linea de codigo
    
for clave in diccionario:
    resultado = diccionario.get(clave, "No Existe un valor asociado a esta clave o no existe esta clave")  
   # print(resultado)

#para obtener solo las claves de un diccionario
for clave in diccionario.keys():# values es una funcion que contiene los diccionarios en python
    print(clave)
