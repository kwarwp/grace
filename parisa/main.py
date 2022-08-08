# grace.parisa.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Art Adriel <art.adriel@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
PERIGOS = "p2jHT5d ho6ZMAL G2u6KB1 awwkaBO hZ0ohTz"

from random import choice 

def joga_tesouro():
    """Incia o jogo do tesouro Inca"""
    camaras = ["Aranha", "Múmia", "Cobra", "Desabamento", "Incêndio"]
    camara = choice(camaras)  #sortear 
    criptas.append(camara[1])
    return input(f"Você visitou {criptas} achou {camara}.  Continua? s ou n?")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Parisa {__name__}. Quer jogar? (s ou n)")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala) 
    while joga_tesouro() == "s":
      pass
    fala = "que pena"
    input(fala)
    
if __name__== "__main__": 
  tesouro_inca()