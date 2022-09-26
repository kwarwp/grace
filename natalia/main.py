# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    def valido():
        Manobra = " ".join(random.choice(Comandos) for i in range(10))
        if "enter enter" in Manobra: 
            return None
        else: 
            return Manobra
    Manobras = [valido() for j in range(10)] 
    return Manobras
    
print(ManobraTrem())
