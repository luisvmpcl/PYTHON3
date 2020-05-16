#26
"""
def multiplicar(valor,valor2,valor3):
    resultado =1
    resultado *= valor  # es lo mismo que escribir  resultado = resultado * valor
    resultado *= valor2
    resultado *= valor3
    return resultado
print(multiplicar(6,1,2))

"""

"""
def multiplicar(* args): # sin el asterisco es un entero con el * lo conviente en una tupla
                       # args recibe todo los valores que lo envias
    resultado =1
    for i in args:
        resultado *= i
    return resultado
print(multiplicar(6,1,2))

"""

"""
def multiplicar(*variable):# args se usa por convencion de los desarroladores de python
                          # aqui estoy usando variable y responde igual
    resultado =1
    for i in variable:
        resultado *= i
    return resultado
print(multiplicar(6,1,2))

"""
"""
def multiplicar(inicio,*args): # en este caso inicio es un entero y colocara antes del *args
    for i in args:
        inicio *= i
    return inicio
print(multiplicar(20,6,1,2))

"""

"""
def multiplicar(inicio,*args): # en este caso inicio es un entero y colocara antes del *args
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(20))

"""

"""
def multiplicar(inicio,*args): # en este caso inicio es un entero y se colocara antes del *args
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(20))

"""

"""
def multiplicar(inicio,*args,**kwargs): # **kwargs  representa a los diccionarios
    print(kwargs)
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(20,12,4,56,5,3, resultante = 20 , cancelacion =50))

"""



def multiplicar(inicio,*args,**variante): # **kwargs  representa a los diccionarios, recordatorio que **kwargs  es una convencion de los desarrolladores de python
                                        # podemos colocar otras ejemplo variante etc
    print(variante)
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(20,12,4,56,5,3, resultante = 20 , cancelacion =50))






