# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
Bagunca = ["baixo cima", "cima baixo", "baixo baixo", "cima cima"
"enter enter", "esquerda direita", "direita esquerda"] 
def ManobraTrem():
    def valido():
        Manobra = " ".join(random.choice(Comandos) for i in range(10))
        if any (engano for engano in Bagunca if engano in Manobra): 
            return None
        else: 
            return Manobra
    Manobras = [valido() for j in range(10)] 
    return Manobras
    
print(ManobraTrem())
