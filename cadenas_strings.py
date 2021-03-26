"""
Clase 2 
Cadenas strings
"""

def saludar(nombre, apellido):
    # usando format
    print("Hola {} {} como estas?".format(nombre, apellido))
    # f-strings
    print(f"Hola {nombre} {apellido} como estas?")
    print("Hola %s %s como estas?" %  (nombre, apellido))

saludar("Xavier", "Petit")
saludar(1, 2)

base_url = "https://www.google.com/search?q="
palabras_a_buscar = ["river", "boca", "san lorenzo", "racing"]
urls = []
for palabra in palabras_a_buscar:
    fullurl = f'{base_url}{palabra}'
    print(fullurl)
    urls.append(fullurl)

print(urls)