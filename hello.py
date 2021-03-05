print('Hello!!!')
a = 5
print(a)
a = 10
if a > 12:
    print(a)
else:
    print("A no es mayor a 12")


# ejemplo select case en python
b = 1

if b == 1:
    print("Usted eligio 1")
elif b == 2:
    print("Usted eligio 2")
elif b == 3:
    print("Usted eligio 3")
else:
    print("B no es ni 1, ni 2 ni 3")


# For con range
print("\nFor loop")
for x in range(1, 5, 2):
    print("X ahora vale: ", x)

print("\nWhile loop")

indice = 0
while indice < 5:
    print("Mi indice vale: ", indice)
    # indice = indice + 1
    indice += 1 



print("\nFin programa")