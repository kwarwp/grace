# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    return random.choice(Comandos)
    
print(ManobraTrem())
