#27
"""
def potencia(numero,exponente):
    numero = pow(numero,exponente) #pow eleva a la potencia
    return numero
print(potencia(8,2))

"""

"""
def potencia(numero,exponente):
    return pow(numero, exponente)

print(potencia(8,2))

"""

"""
# funcion = lambda parametro_1 , parametro_2, etc : logica

potencia = lambda numero , exponente: pow(numero,exponente) # es mas expresivo
print(potencia(10,2))

"""


# funcion = lambda parametro_1 , parametro_2, etc : logica
multiplicar_por_10 = lambda numero: numero * 10
potencia = lambda numero,exponente: pow(multiplicar_por_10(numero),exponente) # es mas expresivo
print(potencia(10,2))

