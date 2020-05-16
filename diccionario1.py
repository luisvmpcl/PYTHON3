#22
#diccionario = {1: "Hola", 2: "Como estas", 3: "Bien"}
#print(diccionario)
"""

diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
}

print(diccionario)
"""


"""
diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
}
diccionario = {} # aqui estoy redefiniendo el diccionario es decir va imprimir vacio
print(diccionario)
"""

"""
diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien",
    1: "y tu?" # como vemos hay 2 claves con diferentes valores ; entonces  agregara al diccionario lo ultimo
}
print(diccionario)
"""


"""
diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
print(diccionario[2])
"""


"""
diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
#esta es la manera correcta de obtener un valor de un diccionario
print(resultado)
"""



diccionario = {
    1:"Hola",
    2:"Como estas",
    3:"Bien"
    
}
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave") 
diccionario[4] ="Que Fino" # asi añadimos un valor
print(diccionario)

