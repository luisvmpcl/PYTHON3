#16

"""
def nombreFuncion():
    INSCTRUCCIONES QUE SE DESEAN EJECUTARLAS
    return valor
"""

"""
def sumar():
    numero = int(input('Ingrese primer numero para la suma:'))
    numero2 = int(input('Ingrese segundo numero para la suma:'))
    
    suma = numero + numero2
    print('El resultado de sumar los numeros ingresados es: '+str(suma)) # str  tenemos que castearlo  
    
sumar()

"""

"""
def sumar():
    numero = int(input('Ingrese primer numero para la suma:'))
    numero2 = int(input('Ingrese segundo numero para la suma:'))
    
    suma = numero + numero2
    print('El resultado de sumar los numeros ingresados es: '+str(suma)) # str  tenemos que castearlo 
    
for i in range(4):  # si queremos que se repita 4 veces 
    sumar()
"""    
    

def sumar(numero, numero2): # es opcional los parametros 
    suma = numero + numero2
    return suma    
    
for i in range(4):  # si queremos que se repita 4 veces 
    numero = int(input('Ingrese primer numero para la suma:'))
    numero2 = int(input('Ingrese segundo numero para la suma:'))
    print('El resultado de sumar los numeros ingresados es: '+str(sumar (numero, numero2))) # str  tenemos que castearlo 