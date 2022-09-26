# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
Bagunca = ["baixo cima", "cima baixo", "baixo baixo", "cima cima"
"enter enter", "esquerda direita", "direita esquerda"]

class trem:  #1 vagao ou uma locomotiva
    def __init__(self, posicao, sinal):       #elementos da imagem
        self.carro = posicao            #locomotiva
        self.sinal = sinal             #estação / sinaleira
    def direita(self):
        if self.carro == sul: 
            self.carro = self.sinal
        if self.carro == oeste: 
            self.carro = norte
        if self.carro == leste: 
            self.carro = norte
    def esquerda(self):
        if self.carro == norte: 
            self.carro = self.sinal
        if self.carro == oeste: 
            self.carro = sul
        if self.carro == leste: 
            self.carro = sul
    def baixo(self):                    #separa a locomotiva do azul
        #resolver
    def alto(self):                     #separa o azul do branco
        #resolver
            
class composicao: #todo o trem 
    def __init__(self):      
        self.vermelho = trem(sul, leste)   
        self.branco = trem(sul, leste)     
        self.azul = trem(sul, leste)      
        self.sinal = leste    
    def direita(self):
        self.vermelho.direita()
        self.azul.direita()
        self.branco.direita()
    


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
