"""
Clase 2 
Funciones
"""

def mi_primer_funcion():
    print("hola, esta es mi primer funcion")

def pow(base, exp):
    resultado = base**exp
    return resultado

def saludar(mensaje: str) -> str:
    """ Este es un ejemplo de como se pueden especificar los tipos
    de variable en una funcion y su valor de retorno. 
    """
    print(mensaje)
    return mensaje

def saludar2(mensaje="hola mundo"):
    print(mensaje)


def comprar_comida(elemento, tarjeta=True):
    """
    Ejemploe una funcion con paremetros obligatorios y opcionales
    """
    if tarjeta:
        print("Usted compro con su tarjeta: ", elemento)
    else:
        print('Usted pago en efectivo: ',  elemento)

respuesta = mi_primer_funcion()
print(type(respuesta))
print(respuesta)


respuesta = pow(2, 2)
print(type(respuesta))
print(respuesta)

respuesta = saludar("Hola todxs")
print(type(respuesta))
print(respuesta)

print()

# debe responder usando el valor por defecto
saludar2()
saludar2("Chau mundo")

comprar_comida("manzanas", tarjeta=False)
comprar_comida("manazanas")


## PARADIGMAS
# En programacion hay al menos 3 paradigmas:
# 1) Procedural 
# 2) Orientados Objectos
# 3) Funcional 
#
#
# POO
# OOP
#Object ORiented Programming

# python trata de ser un lenguaje multiparadigma

mi_funcion_lambda = lambda x: x*2

print("Mi funcion lambda ejecutada: ", mi_funcion_lambda(2))

# Paradigma procedural clasica
lista = [1, 2, 3, 4]
lista2 = []
for e in lista:
    lista2.append(e*2)
print(lista2)

# Paradigma funcional
res = list(map(lambda x: x*2, lista))
print(res)

# Paradigma procedural, usando list comprehension
mi_nueva_lista = [ e*2 for e in lista]
print(mi_nueva_lista)