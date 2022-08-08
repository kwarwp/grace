# grace.angie.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Vanessa Vianna <vanmvianna@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
"""IMAGENS"""
TEMPLO = "https://i.imgur.com/DuyTTha.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
A = "https://imgur.com/iCrJ46A"
M = "https://imgur.com/a/KYT6HiQ"
F = "https://imgur.com/xYv9YdG"
C = "https://i.imgur.com/8VfAotu.jpg"
D = "https://i.imgur.com/OHmUIhz.jpg"

from random import choice

class Camara:
    def _init_(self, conteudo, valor=0):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        butim, sobra = self.valor // jogadores, self. valor %jog
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
    """Inicia o jogo do tesouro inca"""
    def __init__(self):
        self.criptas = []
        self.camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"] 
        self.camaras = [Camara(contem) for contem in self.camaras] * 3
        os_tesouros = [1,2,3,4,5,5, 7,7,9, 11,11,13,14, 15,17]
        self.os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
        
    def joga(self):
        #camara = choice(self.camaras)
        camara = self.camara.pop()
        
                tinha_monstro = (camara not in self.os_tesouros) and (camara in self.criptas) 
                self.criptas.append(camara)
                revela = [cam.revela() for cam in self.criptas]
                cam= camara.revela()
                if tinha_monstro:
                    input(f"Ja existia {cam} na {revela}. Você abandonou correndo")
                    return "n"
                return input(f"Você visitou {revela} achou {cam}. Continua(s)")
        
def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Roxanne {__name__}.Quer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    #while _joga_tesouro() == "s":
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
    
if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()