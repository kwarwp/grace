# grace.angie.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Vanessa Vianna <vanmvianna@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
#IMAGENS
TEMPLO = "https://i.imgur.com/DuyTTha.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
A = "https://imgur.com/iCrJ46A"
M = "https://imgur.com/a/KYT6HiQ"
F = "https://imgur.com/xYv9YdG"
C = "https://i.imgur.com/8VfAotu.jpg"
D = "https://i.imgur.com/OHmUIhz.jpg"
from parisa.main import tesouro_inca as art_tesouro

def _joga_tesouro():
    """Inicia o jogo do tesouro inca"""
    camara = ["Aranha", "Cobra", "Mumia", "Desabamento", "Incendio"]
    return input("Você achou Aranha. Continua(s)")
    
def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Roxanne {__name__}.Quer jogar (s)?")
    fala = "beleza" if quer == "s" else "que triste"
    input(fala)
    while _joga_tesouro() == "s":
        fala = "beleza"
        input(fala)
    fala = "que pena"
    input(fala)

if __name__ == "__main__":
   #art_tesouro()
   tesouro_inca()