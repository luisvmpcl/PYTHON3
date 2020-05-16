# ejercicio 7
"""
Averiguar si un numero ingresado por consola es par o impar y ademas
averiguar si es negativo o positivo
"""

"""
print('\t\t\t\tEjercicio 1')  # \t es para las tabulaciones
numero = int(input('Ingrese un número : \n')) # permite convertir un numero en positivo

if numero%2 ==0:  # % es el residuo si es 0 es positivo
    print('El número ingresado es un número par')
    if numero >0:
        print('El número tambien es positivo')
    else:
        print('El número tambien es negativo')
else:
    print('el número ingresado es impar')
    if numero >0:
        print('El número tambien es positivo')
    else:
        print('El número tambien es negativo')
"""
#esta es otra forma de resolver
print('\t\t\t\tEjercicio 1')  # \t es para las tabulaciones
numero = int(input('Ingrese un número : \n')) # permite convertir un numero en positivo

if numero%2 ==0:  # % es el residuo si es 0 es positivo
    if numero > 0:
        print('El número ingresado es un número par y ademas es positivo')    
    else:
        print('El número ingresado es un número par y ademas es negativo')
else:
    print('el número ingresado es impar')
    if numero >0:
        print(' El número ingresado es un número impar y ademas es positivo')
    else:
        print('El número ingresado es un número impar y ademas es negativo')









