#28
# que es una funcion recursiva?- es una funcion que se llama asi misma en su propia ejecucion

"""
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Luisvmpcl.pe")
        
cuenta_atras(10)# imprimira 9 8 7  ......1 .. Luisvmpcl.pe

"""


"""
def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Luisvmpcl.pe")
    print(f"Orden de liberacion {numero}") # se libera la memoria de manera inversa
        
cuenta_atras(10)# imprimira 9 8 7  ......1 .. Luisvmpcl.pe

"""


"""
def calcular_factorial(numero):
    if numero > 1:
        numero = numero * calcular_factorial(numero - 1)
    return numero

print(calcular_factorial(5))

"""

"""

def calcular_factorial(numero):
    if numero > 1:
        numero *= calcular_factorial(numero - 1) # Es otra forma de calcular
    return numero

print(calcular_factorial(5))
"""


def calcular_factorial(numero):
    if numero > 1:numero *= calcular_factorial(numero - 1) 
    return numero

print(calcular_factorial(5))



