# grace.kellee.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Erica Scheffel <ericascheffel@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
from random import shuffle
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=1000, height=500)
TEMPLO = "https://i.imgur.com/OOTUIwl.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
MONSTRO = "https://i.imgur.com/lcvvL1B.png"
ARANHA = "https://i.imgur.com/p2jHT5d.png"
COBRA = "https://i.imgur.com/ho6ZMAL.png"
CHAMAS = "https://i.imgur.com/G2u6KB1.jpg"
MUMIA = "https://i.imgur.com/awwkaBO.jpg"
DESABA = "https://i.imgur.com/hZ0ohTz.jpg"
templo = Cena(TEMPLO)
cena_tesouro = Cena(TESOURO)
cena_monstro = Cena(MONSTRO)
jogar = input("Quer jogar o Tesouro Inca?")
tumba = list("AMCDI"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
mochila = 0
templo.vai()
if jogar == 's':
    #print("Então vamos!")
    #print("Clique ok para encontrar cada monstro da tumba")
    input("Simbora")
    for camara in tumba:
        dois_monstros = (camara not in tesouro) and (camera in corredor)
        eh_tesouro = camara in tesouro
        if eh_tesouro:
            mochila += camara
            cena_tesouro.vai()
        else:
            cena_monstro.vai()
            
        corredor.append(camara)        
        fica = input(f"você já encontrou {corredor}, se você fica digite s, se você sai digite n")
        if dois_monstros:
            input("Você perdeu")
            mochila = 0
            break
        
        if fica != "s":
            input(f"Você desistiu, mas ficou com {mochila} tesouros")
            break
                
else:
    print("Que pena")
