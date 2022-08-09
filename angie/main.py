# grace.angie.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  vanessa vianna <vanmvianna@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

""" O Jogo do Tesouro Inca """

"""importacao de diretorio / biblioteca"""
from random import shuffle
from _spy.vitollino.main import Cena, STYLE
STYLE.update(width=1000, height=500)

"""IMAGENS"""
TEMPLO = "https://i.imgur.com/DuyTTha.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
A = "https://imgur.com/iCrJ46A"
M = "https://imgur.com/a/KYT6HiQ"
F = "https://imgur.com/xYv9YdG"
C = "https://i.imgur.com/8VfAotu.jpg"
D = "https://i.imgur.com/OHmUIhz.jpg" 

"""CENAS"""
cena_templo = Cena(TEMPLO)
cena_tesouro = Cena(TESOURO)
cena_A = Cena(A)
cena_M = Cena(M)
cena_F = Cena(F)
cena_C = Cena(C)
cena_D = Cena(D)
lista_de_cenas = [cena_A, cena_M, cena_F, cena_C, cena_D]

"""classe / modulos"""
class Camara:
    def __init__(self, conteudo, valor=0):
        self.conteudo = conteudo
        self.valor = valor
    def revela(self):
        return self.conteudo
    def resgata(self, jogadores):
        butim, sobra = self.valor // jogadores, self.valor % jogadores
        self.valor = sobra
        return butim
    def __repr__(self):
        return self.conteudo

class JogaTesouro():
    def __init__(self):
        self.criptas = []
        camaras = ["A", "M", "C", "D", "I"]
        self.camaras = [Camara(contem) for contem in camaras] * 3
        os_tesouros = [1,2,3,4,5,5, 7,7,9, 11,11,13,14, 15,17]
        self.os_tesouros = [Camara(valor, valor) for valor in os_tesouros]
        self.camaras += self.os_tesouros
        shuffle(self.camaras)
        
    def joga(self):
        camara = self.camaras.pop()
        tinha_monstro = (camara not in self.os_tesouros) and (camara in self.criptas) 
        self.criptas.append(camara)
        revela = [cam.revela() for cam in self.criptas]
        cam= camara.revela()
        if tinha_monstro:
            input(f"Ja existia {cam} na {revela}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {revela} achou {cam}. Continua(s)")
        if cam == lista_de_cenas[6]  
        return  cena_(6).vai()
        


def tesouro_inca():
    quer = input(f"Bem vindo ao Tesouro Inca - versão Angie {__name__}.Quer jogar (s)?", cena_templo.vai())
    fala = "ok" if quer == "s" else "que triste"
    input(fala)
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
if __name__ == "__main__":
    tesouro_inca()