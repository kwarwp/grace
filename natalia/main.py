# grace.natalia.main.py

import random

Comandos = [ "direita", "esquerda", "cima", "baixo", "enter"]
Bagunca = ["baixo cima", "cima baixo", "baixo baixo", "cima cima"
"enter enter", "esquerda direita", "direita esquerda"]
class plataforma:
    def __init__ (self, nome): 
        self.vagoes = [ ] 
        self.nome = nome
    def __repr__(self):
        return self.nome
    
    def sair_esquerda (self, vagao):
        if vagao in self.vagoes: 
            self.vagoes.remove(vagao)
            
    
    def sair_direita (self, vagao):
        if vagao in self.vagoes: 
            self.vagoes.remove(vagao)    
    
    def chegar_direita (self, vagao):
        
        self.vagoes.append(vagao)

    def chegar_esquerda (self, vagao):
        
        self.vagoes = [vagao] + self.vagoes
norte, sul, leste, oeste = plataforma(1), plataforma(2), plataforma(3), plataforma(4)

class trem:  #1 vagao ou uma locomotiva
    def __init__(self, posicao, sinal, nome):       #elementos da imagem
        self.carro = posicao            #locomotiva
        self.sinal = sinal             #estação / sinaleira
        self.nome = nome
    def __repr__(self):
        return self.nome
    def direita(self):
        if self.carro == sul: 
            self.carro = self.sinal
            oeste.chegar_esquerda(self.carro)
            sul.sair_direita(self.carro)
        
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
        pass
        #resolver
    def alto(self):                     #separa o azul do branco
        pass
        #resolver
            
class composicao: #todo o trem 
    def __init__(self):      
        self.vermelho = trem(sul, leste, 'v')   
        self.branco = trem(sul, leste, 'b')     
        self.azul = trem(sul, leste, 'a')      
        self.sinal = leste  
        sul.vagoes = [self.branco, self.azul, self.vermelho]
    
    def direita(self):
        self.vermelho.direita()
        self.azul.direita()
        self.branco.direita()


    
        
    
def testaTrem():
    r = composicao()
    print(sul.vagoes)
    r.direita()
    print(sul.vagoes)
def ManobraTrem():
    def valido():
        Manobra = " ".join(random.choice(Comandos) for i in range(10))
        if any (engano for engano in Bagunca if engano in Manobra): 
            return None
        else: 
            return Manobra
    Manobras = [valido() for j in range(10)] 
    return Manobras
    
# print(ManobraTrem())
testaTrem()