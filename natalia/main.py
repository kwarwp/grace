# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    def valido():
        return " ".join(random.choice(Comandos) for i in range(10))
    Manobras = [valido() for j in range(10)] 
    return Manobras
    
print(ManobraTrem())
