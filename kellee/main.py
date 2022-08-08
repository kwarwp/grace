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

from roxanne.main import _tesouro_inca as Carlo_tesouro #Renomeia a funcao importada

def _joga_tesouro():
    """Inicia o jogo do Tesouro Inca"""
    return input("Você achou Aranha. Continua? Tecle (s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem-vindo ao Tesouro Inca - versão Kellee {__name__}.Quer jogar? tecle (s)")
    fala = "Sim!" if quer == "s" else "Que pena..."
    input(fala)
    while _joga_tesouro() == "s":
        fala = "Sim!" 
        input(fala)
    fala = "Que pena!"
    input(fala)

if __name__ == "__main__":   # Chama o modulo com mesmo nome se for o principal
    #Carlo_tesouro()
    tesouro_inca()