"""
Siguiendo el ejemplo del ejercicio 301, guardar estos valores en  una tabla de sqlite3:

    2020-04-08;95.5;140.0,44.5
    2020-04-09;95.5;140.0,43.5

Cada columna significa lo siguiente:
    fecha;dolar_blue;dolar_oficial;diferencia


Como ayuda uno de los lugares donde se puede tomar informacion es de:

https://www.dolarsi.com/api/api.php?type=valoresprincipales

"""
import requests

url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"


response = requests.get(url)
dolar_data = response.json()
try:
    valor_oficial = dolar_data[0]['casa']['venta']
    valor_blue = dolar_data[1]['casa']['venta']

    print(f'Valor oficial: {valor_oficial}, valor blue: {valor_blue}')
except KeyError:
    print("La respuesta del servidor no es valida")

#for x in range(0, len(dolar_data)):
#    print(dolar_data[x])
#
#n = 0
#while n < len(dolar_data):
#    print(dolar_data[n])
#    n += 1

for x in dolar_data:
    print(x)


