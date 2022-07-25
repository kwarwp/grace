# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
jogar = input ("Quer jogar o tesouro Inca?")
tumba = list("AMCDI"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
if jogar == 's':
    input("simbora!")
    for camara in tumba:
        dois_monstros = camara in corredor
        corredor.append(camara)
        fica = input(f"Você já encontrou {corredor}, fica(s) ou sai(n)")
        if fica != "s":
            input("Voce desistiu")
            break
        if dois_monstros:
            input("você perdeu")
            break
else:
    input("pena!")