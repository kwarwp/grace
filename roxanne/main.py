# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
""" O Jogo do Tesouro Inca

    Um grupo de aventureiros se arrisca em uma escavação antiga de um templo inca.
    
    Changelog
    ---------
    * função tesouro_inca - executa o jogo.
    * função _joga_tesouro - avança na cripta.
"""
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
PERIGOS = "p2jHT5d ho6ZMAL G2u6KB1 awwkaBO hZ0ohTz"
#from parisa.main import tesouro_inca as art_tesouro
# from courtney.main import _joga_tesouro as art_joga
from random import choice


class JogaTesouro():
    """Inicia o jogo do tesouro inca"""
    def __init__(self):
        self.criptas = []
        self.camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
        
    def joga(self):
        camara = choice(self.camaras)
        tinha_monstro = camara in self.criptas
        self.criptas.append(camara)
        if tinha_monstro:
            input(f"Ja existia {camara} na {self.criptas}. Você abandonou correndo")
            return "n"
        return input(f"Você visitou {self.criptas} achou {camara}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Roxanne {__name__}.Quer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    # while art_joga() == "s":
    _joga_tesouro = JogaTesouro()
    while _joga_tesouro.joga() == "s":
        pass
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()

