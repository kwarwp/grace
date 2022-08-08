# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Adriana Albuquerque <adriana.mota@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
PERIGOS = "p2jHT5d ho6ZMAL G2u6KB1 awwkaBO hZ0ohTz"
from parisa.main import tesouro_inca as art_tesouro

def _joga_tesouro():
    """Inicia o jogo do tesouro inca"""
    camaras = ["Aranha","Múmia","Cobra","Desabamento","Incêndio"]
    camara = choice(camaras)
    return input(f"Você achou {camara}. Continua(s)")

def tesouro_inca():
    """O jogo do Tesouro Inca"""
    quer = input(f"Bem vindo ao Tesouro Inca - versão Libby {__name__}.Quer jogar (s)?")
    fala = "Legal" if quer == "s" else "que pena"
    input(fala)
    while _joga_tesouro() == "s":
        fala = "legal"
        input(fala)
    fala = "que pena"
    input(fala)
    

if __name__ == "__main__":
    # art_tesouro()
    tesouro_inca()
