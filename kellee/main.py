# grace.kellee.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Erica Scheffel <ericascheffel@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
jogar = input("Quer jogar o Tesouro Inca?")
tumba = list("AMCDI"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
if (jogar == 's' or 'S' or "sim" or "SIM" or "Sim"):
    print("Então vamos!")
    print("Clique ok para encontrar cada monstro da tumba")
    input("Simbora")
    for camara in tumba:
        dois_monstros = camara in corredor
        corredor.append(camara)        
        fica = input(f"você encontrou {corredor}, você fica?")
        if (fica != 's' or 'S' or "sim" or "SIM" or "Sim"):
            input("Você desistiu")
            break
        
        if dois_monstros:
            input("Você perdeu")
            break
else:
    print("Que pena")
