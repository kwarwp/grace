# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    def valido():
        return " ".join(random.choice(Comandos) for i in range(10))
    Manobras = [manobra for j in range(10) if manobra:= valido()] 
    return Manobras
    
print(ManobraTrem())
