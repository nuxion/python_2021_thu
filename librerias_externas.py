"""
clase 3 
librerias externas
https://pypi.org/search/?q=requests
# desde la terminal ejecutar
pip install requests
"""
import requests

response = requests.get("https://httpbin.org/get")
texto = response.text
print(texto)
jsondata = response.json()
print(jsondata)

