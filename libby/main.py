# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Adriana Albuquerque <adriana.mota@nce.ufrj.br>,
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
#from parisa.main import _joga_tesouro as art_joga
from random import choice
criptas = [] 
def _joga_tesouro():
    """Inicia o jogo do tesouro inca"""
    camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
    camara = choice(camaras)
    criptas.append (camara)
    tinha_monstro = 
    if tinha_monstro:
    return "n"
    return input(f"você visitou {criptas} achou {camara}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Libby {__name__}.Quer jogar (s)?")
    fala = "great" if quer == "s" else "que pena"
    input(fala)
    while _joga_tesouro() == "s":
        fala = "great"
        input(fala)
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()
