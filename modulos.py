"""
Clase 3 
Modulos
Puede ser standards de python o modulos de terceros

# para ver librerias standares
   https://docs.python.org/es/3/tutorial/stdlib.html
"""
# Para hacer un reloj super basico me importo dos librerias 
from datetime import datetime # me permite saber la hora
import time # Me permite aplicar un wait de un segundo
# from time import sleep # otra forma de importar sleep

for x in range(0, 2):
    print(datetime.now())
    time.sleep(1)
    # sleep(1)

# listar archiovs de un directorio
import os

for f in os.listdir():
    print(f)

print()
# Para importar este modulo lo que neceisto
# es indicar el nombre'
# import mimodulo
# mimodulo.saludo_personalizado(name)
from mimodulo import saludo_personalizado


saludo_personalizado("Xavier")
