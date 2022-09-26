# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
def ManobraTrem():
    return [random.choice(Comandos) for in range(10)] 
    
print(ManobraTrem())
