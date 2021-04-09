"""
Clase  3

https://docs.python.org/3/library/exceptions.html
"""

def division(a, b):
    return a / b



# Funcionamiento normal
resultado = division(4, 2)

print(resultado)

# Que pasa si divido por cero?
try:
    resultado = division(4, 0)
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except NameError:
    print("Tipeaste mal")


print("Queres realizar otra operacion?")

## Generar una excepcion

def suma_pares(lista):
    """
    Si la suma de los elementos de la lista no
    es par , generar una exception del tipo
    ValueError.
    """
    resultado = 0
    for numero  in lista:
        resultado += numero

    if resultado % 2 == 0:
        return resultado
    else:
        raise(ValueError("El resultado no es par"))

res = suma_pares([2, 2, 4])
assert res == 8
print(res)

# para capturar la excepcion utilizo un try:
try:
    res = suma_pares([2, 2, 5])
except ValueError:
    print("Perdiste, la suma no es par")


# Como agarrar una excepcion en un diccionario?

mi_dict = {'name': 'Pepe', 'age': 25 }
try:
    print(mi_dict['lastname'])
except KeyError:
    # una mala practica es "silenciar" un error
    pass
    # print("La key no existe...")

print("Termino el programa perfectamente")