"""
Los magos de la academia de magia están teniendo problemas para decir sus pases mágicos porque no saben calcular restos. 
Ayudalos!

Para decir hechizos antes tienen que contar hasta un número pero si el número es múltiplo de 3 reemplazarlo por "abracadabra"
y si el número es múltiplo de 5 reemplazarlo por "alakazam". Si es múltiplo de 3 y 5 tienen que decir "abracadabraalakazam".

Hacé un script en python que reciba el número hasta el que tienen que llegar e imprima qué palabras mágicas 
tienen que decir antes de su hechizo.

Por ejemplo, esta sería una corrida hasta el número 20:

$ python3 magic.py 20
    1
    2
    abracadabra
    4
    alakazam
    abracadabra
    7
    8
    abracadabra
    alakazam
    11
    abracadabra
    13
    14
    abracadabraalakazam
    16
    17
    abracadabra
    19
    alakazam
"""
"""
for i in range(1, self.limite):
            if i%3 == 0 and i%5 == 0: 
                print("abracadabraalakazam") 
            elif i%3 == 0: 
                print("abracadabra") 
            elif i%5 == 0: 
                print("Alakazam") 
            else:
                print(i) 
"""


class Mago:

    def __init__(self, limite=20):
        self.limite = limite

    def escribir(self):
        pass
        #f = open("resultado.txt", "a")
        # f.write())  

    def hacer_magia(self):
        for i in range(1, self.limite):
            if i%3 == 0 and i%5 == 0: 
                print("abracadabraalakazam") 
            elif i%3 == 0: 
                print("abracadabra") 
            elif i%5 == 0: 
                print("Alakazam") 
            else:
                print(i) 

merlin = Mago(20)
merlin.hacer_magia()
