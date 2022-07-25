# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Douglas <douglasvsa@ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=1000, height=500)
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
A = "https://imgur.com/Yb6sBTC"
M = "https://imgur.com/t4RwAwH"
C = "https://imgur.com/DYlxlxS"
D = "https://imgur.com/gS0inP9"
I = "https://imgur.com/CikvXEF"

templo = Cena(TEMPLO)
cena_tesouro = Cena(TESOURO)
templo = Cena(TEMPLO)
A = Cena(A)
M = Cena(M)
C = Cena(C)
D = Cena(D)
I = Cena(I)

jogar = input ("Quer jogar o tesouro Inca?")
tumba = list[A, M, C, D, I]*3
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