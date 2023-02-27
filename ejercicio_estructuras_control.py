accion_1="estoy en la entrada del evento"
accion_2="me estoy registrando"


#estructura de control (condicional o sentencia if o si)
#permite continuar un flujo (realizar algo)si se cumple
#y en caso de no cumplirse,se puede o no continuar con otro flujo (hacer algo mas)
#esta sentencia(if)va acompañado de los operadores de conparacion
"""
if estructura_datos_1 < estutructura_datos_2
if estructura_datos_1 <= estutructura_datos_2
if estructura_datos_1 > estutructura_datos_2
if estructura_datos_1 >= estutructura_datos_2
if estructura_datos_1 == estutructura_datos_2
if estructura_datos_1 != estutructura_datos_2
"""
#hay varias maneras de utilizar la sentencia if
#if simple,if compuesto,if anidado

#if simple
#dato_comparacion=18
#edad=30 
"""
#if simple
print("cuantos años tienes?")
edad=input()
edad=int(edad)
if edad>=18:
    print("ingresar y disfrutar el evento")
"""
"""
#if compuesto
print("cuantos años tienes?")
edad=input()
edad=int(edad)
if edad>=18:
    print("ingresar y disfrutar el evento")
else:
    print("no puede ingresar")
"""
"""
#if anidado
boleta= False

print("cuantos años tienes?")
edad=input()
edad=int(edad)
if edad>=18 and boleta:
    print("ingresar y disfrutar el evento")
    
else:
    print("no puede ingresar")
"""
"""
print("escriba la localidad de su boleta")
localidad=input()
localidad=int(localidad)

if localidad==1:
    print("VIP=500000")
if localidad==2:
    print("PREFERENCIAL=400000")
if localidad==3:
    print("GENERAL=200000")
if localidad==4:
    print("BAJA=100000")
if localidad < 1  or localidad > 4 :
    print("la localidad de su boleta no existe")
"""

def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None