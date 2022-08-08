# grace.kellee.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Erica Scheffel <ericascheffel@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
from _spy.vitollino.main import Cena, STYLE

STYLE.update(width=1000, height=500)
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
ARANHA = "https://i.imgur.com/p2jHT5d.png"
COBRA = "https://i.imgur.com/ho6ZMAL.png"
CHAMAS = "https://i.imgur.com/G2u6KB1.jpg"
MUMIA = "https://i.imgur.com/awwkaBO.jpg"
DESABA = "https://i.imgur.com/hZ0ohTz.jpg"

#from roxanne.main import _tesouro_inca as Carlo_tesouro #Renomeia a funcao importada
from random import choice, shuffle

class Camara:
    def __init__(self, conteudo, valor=0):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        butin = self.valor // jogadores
        sobra = self.valor % jogadores
        #A linha abaixo substitui asduas acima
        #butim, sobra = self.valor // jogadores, self.valor % jogadores #// - Divisao inteira
        self.valor = sobra
        return butim
    def __repr__(self):
        return self.conteudo
        
class Incursao:
    pass
class Tumba:
    pass
class Jogador:
    pass

class JogaTesouro():
    """Inicia o jogo do Tesouro Inca"""
    def __init__(self):
        self.criptas = []
        self.camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
        self.camaras = [Camara(contem) for contem in self.camaras]*3
        os_tesouros = [1,2,3,4,5,5,7,7,9, 11,11,13,14, 15,17]
        self.os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
    
    def joga(self):        
        # camara = choice(self.camaras)  
        camara = self.camaras.pop() 
        
        tinha_monstro = (camara in self.criptas) and (camara not in self.oh_tesouros)
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam = camara.revela()
        if tinha_monstro:
            input(f"Já existia {cam} na {revela}. Você fugiu!")
            return "n"    
        return input(f"Você visitou {revela} e achou {cam}. Continua? Tecle (s)")     
   
def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem-vindo ao Tesouro Inca - versão Kellee {__name__}.Quer jogar? tecle (s)")
    fala = "Sim!" if quer == "s" else "Que pena..."
    input(fala)
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass        
    fala = "Que pena!"
    input(fala)

if __name__ == "__main__":   # Chama o modulo com mesmo nome se for o principal
    #Carlo_tesouro()
    tesouro_inca()