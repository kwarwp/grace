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
    def _init_(self, conteudo, valor):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        butim, sobra = self.valor // jogadores, self. valor %jog
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
    
    def joga(self):
        camara = choice(self.camaras)
        tinha_monstros = camara in self.criptas
        self.criptas.append(camara) 
        if tinha_monstros:
           input(f"já existia {camara} na {criptas}. Você abandonou correndo")
           return "n"
        return input(f"Você visitou {criptas} achou {camara}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Roxanne {__name__}.Quer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    #while _joga_tesouro() == "s":
    _joga_tesouro = JogaTesouros()
    fala = "beleza"
    input(fala)
    fala = "que pena"
    input(fala)
    
if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()