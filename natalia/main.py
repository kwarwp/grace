# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    Manobras = [random.choice(Comandos) for i in range(10)] 
    return Manobras
    
print(ManobraTrem())
