# grace.grace.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=800, height=500)
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
templo = Cena(TEMPLO)
tumba = list("ABCDE"*3)
tesouros = list([1,2,3,4,5,6,7,8,9]*2)
tumba += tesouros
shuffle(tumba)
#input(tumba)
cripta = []
mochila = 0
templo.vai()
for cam in tumba:
    cripta += [cam]
    if input(f"Cripta :{cripta} vai?") != 's':
        break
    if cam in tesouros:
        mochila += cam
    else:
        if cam in cripta:
            input("perdeu")
            cripta = []
            mochila = 0
            break
        #cripta += [cam]
input(f"ganhou: {mochila}")