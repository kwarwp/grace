# grace.ruzwana.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
""" Tesouro Inca - Orientado a Objetos

"""
from random import shuffle
from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
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
CTEMPLO = Cena(TEMPLO)
CTESOURO = Cena(TESOURO)
cena_monstro = Cena(MONSTRO)
CABANA = Cena('https://i.imgur.com/eOqt4eP.jpg')


class Tesouro:
    """ O jogo do Tesouro Inca """
    def __init__(self):
        self.templo = CTEMPLO
        self.tesouro = CTESOURO
        self.cabana = CABANA
        
        
    def escolheu(self, resposta):
        if resposta == "A":
            self.tesouro.vai()
        else:
            self.cabana.vai()
        
    def vai(self):
        """ Inicia o jogo """
        self.templo.vai()
        Texto("Vai se aventurar?", A="sim", B="não", foi=self.escolheu, cena=self.templo).vai()


Tesouro().vai()