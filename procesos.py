"""
Clase 5 
procesos
"""
import subprocess

# msg = input("Ingrese un mensaje...")
# print(msg)

# subprocess.run(["mkdir", "test"])
# subprocess.run(["touch", "test/prueba.txt"])
# subprocess.run(["rm", "-r", "test/"]) # OJO borrado recursivo de la carpeta

hostname = subprocess.run(["hostname"], capture_output=True, encoding='utf-8')
print(type(hostname.stdout))
print(hostname.stdout)

grep_error = subprocess.run(["grep", "-RTTTAE"], capture_output=True, encoding='utf-8')
print(grep_error.stderr)


# Momento inception
inception = subprocess.run(["python", "hello.py"], capture_output=True, encoding='utf-8')
print("Inception: ", inception.stdout.splitlines())

# Ejemplo de como abrir una nueva ventana de firefox en un sitio determinado
# subprocess.run(["firefox", "--new-window", "https://www.google.com"])


# Listando procesos
# en linux/mac, ps es como el taskmanager de windows, en windows
# tengo el comando tasklist
lista_procesos = subprocess.run(["ps", "-ef"], capture_output=True, encoding="utf-8")
# print(lista_procesos)
firefox = 0
for l in lista_procesos.stdout.splitlines():
    # obtengo el pid:
    pid = l.split()[1]
    # subprocess.run(["kill", "-9", pid], capture_output=True, encoding="utf-8")
    if "firefox" in l:
        print(l)
        firefox += 1

print(f"Hay {firefox} procesos de firefox arriba ")
