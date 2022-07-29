# grace.roxanne.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Vanessa Vianna <vanmvianna@gmail.com>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
# IMPORTANDO BIBLIOTECAS
from random import shuffle
from _spy.vitollino.main import Cena, STYLE
from random import shuffle
STYLE.update(width=1000, height=500)
#IMAGENS
TEMPLO = "https://i.imgur.com/DuyTTha.jpg"
TESOURO = "https://i.imgur.com/OuPgmla.jpg"
A = "https://imgur.com/iCrJ46A"
M = "https://imgur.com/a/KYT6HiQ"
F = "https://imgur.com/xYv9YdG"
C = "https://i.imgur.com/8VfAotu.jpg"
D = "https://i.imgur.com/OHmUIhz.jpg" 
#CENAS
cena_templo = Cena(TEMPLO)
cena_tesouro = Cena(TESOURO)
cena_A = Cena(A)
cena_M = Cena(M)
cena_F = Cena(F)
cena_C = Cena(C)
cena_D = Cena(D)
#MONTAGEM DO JOGO
jogar = input ("Quer jogar o tesouro Inca?")
tumba = list("AMFCD"*3)
tesouro = [1,2,3,4,5,6,7,8,9]*2
tumba += tesouro
shuffle(tumba)
corredor = []
mochila = 0
#JOGO
if jogar == 's':
    input("simbora!", cena_templo.vai())
    for camara in tumba:
        dois_monstros = (camara not in tesouro) and (camara in corredor)
        eh_tesouro = camara in tesouro
        if eh_tesouro:
            mochila += camara
        corredor.append(camara)
        tumba = list("AMFCD"*3)
    for tumba in camara:
        Cena(tumba).vai
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