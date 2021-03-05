
# Primer ejemplo de coleccion basado en un string
saludo = "Hola mundo"
print(type(saludo))
print(saludo)

# Recorro el string caracter por caracter
for x in saludo:
    print(x)

print("\nListas: ")
lista = ['h', 'o', 'l', 'a']
# indice: 0    1    2    3
# https://lh3.googleusercontent.com/proxy/QVbSYrRqvuLC53Ql53S15MMh-7cYl4hOj0Gn6H5FUiTeDxKlH44KmdUVr71e2L8PH_aH42SKQO_3c3AsKab5ZIisWfDuWjlErYs3jlPlKo_jQZV--OvFNg
print(lista)
print(type(lista))


for x in lista:
    print(x)

# Tambien puedo acceder a traves de su indice
print("Posicion 1 de la lista: ", lista[1])
if lista[1] == 'o':
    print("Ok!!")


for x in range(0, len(lista)):
    print(x)

# Recorro la lista usando range como indice
for x in range(0, len(lista)):
    print("valor x: ", lista[x])

alumnos = [['pepe', 'garcia', 33],['julieta', 'perez', 26], ['julian', 'rodriguez', 50]]

# imprimo fila por fila
for fila in alumnos:
    print(fila)

# imprimo solo el apellido
for fila in alumnos:
    print(fila[1])


# Quiero calcular la edad promedio de mis alumnos
edades = 0
for alumno in alumnos:
    print(alumno[2])
    edades = edades + alumno[2]
print("La suma de todas las edades es igual a: ", edades)
promedio = edades / len(alumnos)
print("El promedio de edad del curso es: ", promedio)

# Diccionario
dic = { 'nombre': 'jose', 'apellido': 'perez', 'edad': 44 }

alumno = {'nombre': 'jose', 'apellido': 'perez', 'edad': 44, 'materias': ['python', 'sql', 'data science']}
print(type(alumno['materias']))
alumno['edad'] = 55
print(alumno['edad'])
alumno.update({'mail': 'jose_88@hotmail.com'})


# Puedo representar mi estructura de datos alumnos inicial de una forma distinta usando diccionarios:
# original: 
alumnos = [['pepe', 'garcia', 33],['julieta', 'perez', 26], ['julian', 'rodriguez', 50]]

alumnos_mejorado = [
    { 'nombre': 'jose', 'apellido': 'perez', 'edad': 44 },
    { 'nombre': 'maria', 'apellido': 'garcia', 'edad': 24 },
    { 'nombre': 'jose', 'apellido': 'rodirugez', 'edad': 34 },
]

for alumno in alumnos_mejorado:
    print("Alumno apellido: ", alumno['apellido'])

alumnos_materias = [
    { 'nombre': 'jose', 'apellido': 'perez', 'edad': 44, 'materias': ['python', 'javascript'] },
    { 'nombre': 'maria', 'apellido': 'garcia', 'edad': 24, 'materias': ['sql', 'agile', 'python'] },
    { 'nombre': 'jose', 'apellido': 'rodirugez', 'edad': 34, 'materias': ['agile', 'liderazgo'] },
]

for alumno in alumnos_materias:
    for materia in alumno['materias']:
        print(materia)




