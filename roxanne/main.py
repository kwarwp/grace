# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=1000, height=500)
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
ARANHA = "https://i.imgur.com/p2jHT5d.png"
COBRA = "https://i.imgur.com/p2jHT5d.png"
templo = Cena(TEMPLO)
cena_tesouro = Cena(TESOURO)
cena_monstro = Cena(MONSTRO)
templo = Cena(TEMPLO)
jogar = input ("Quer jogar o tesouro Inca?")
tumba = list("AMCDI"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
mochila = 0
templo.vai()
if jogar == 's':
    input("simbora!")
    for camara in tumba:
        dois_monstros = (camara not in tesouro) and (camara in corredor)
        eh_tesouro = camara in tesouro
        if eh_tesouro:
            mochila += camara
            cena_tesouro.vai()
        else:
            cena_monstro.vai()
        corredor.append(camara)
        fica = input(f"Você já encontrou {corredor}, fica(s) ou sai(n)")
        if dois_monstros:
            input("você perdeu")
            mochila = 0
            break
        if fica != "s":
            input(f"Voce desistiu, mas ficou com {mochila} tesouros")
            break
else:
    input("pena!")