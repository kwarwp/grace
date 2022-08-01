# grace.ruzwana.main.py
# -*- coding: UTF8 -*-
# This file is part of program Jogo Inca
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception
""" Tesouro Inca - Orientado a Objetos

"""
from browser import alert
from random import shuffle
from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
STYLE.update(width=1000, height='600px')
OURO = "https://i.imgur.com/aqt77Uj.png"
TURQUESA = "https://i.imgur.com/dRj6lAy.png"
OBSIDIAN = "https://i.imgur.com/UFVadxc.png"
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
CABANA = 'https://i.imgur.com/eOqt4eP.jpg'
CCABANA = Cena('https://i.imgur.com/eOqt4eP.jpg')


class Camara:
    """ Uma Camara do Templo """
    def __init__(self, imagem, valor=0):
        self._imagem = Cena(imagem)
        self._valor = valor
        
    def texto(self, fala, foi, **kwargs):
        Texto(self._imagem, fala, foi=foi, **kwargs).vai()
        
    def segue(self, vai, desiste):
        def testa(resposta):
            vai() if resposta == "A" else desiste()
        texto = f"Você achou {self._valor} tesouros, Prossegue?" if self._valor else "Prossegue?"
        self.texto(texto, foi=testa, A="sim", B="não")
        Tesouro.JOGO.recebe(self._valor)
        
    def vai(self):
        """ Revela a Câmara """
        self._imagem.vai()
        v = self._valor
        g, o, t = v // 10, (v % 10) //5, v % 5
        elm = [OURO]*g + [OBSIDIAN] * o + [TURQUESA] *t
        [Elemento(img, cena=self._imagem, w=80, h=80, x=80+i*100, y=400) for i, img in enumerate(elm[:9])]
        [Elemento(img, cena=self._imagem, w=80, h=80, x=80+i*100, y=500) for i, img in enumerate(elm[9:])]
        
        return self


class Tumba:
    """ Uma Tumba com várias Câmaras """
    def __init__(self):
        self._tumba = [Camara(img) for img in (ARANHA, MUMIA, COBRA, DESABA, CHAMAS)]
        valores = (2,3,4,5,6,7,8,9,11,12,13,14,15,17)*2
        tesouros = [Camara(TESOURO, valor) for valor in valores]
        self._tumba = self._tumba *3
        self._tumba += tesouros
        shuffle(self._tumba)
        self._cripta = []
        
    def vai(self):
        """ Revela a Câmara """
        def nada():
            Tesouro.JOGO.termina()
            #Camara(CABANA).vai()
        camara = self._tumba.pop()
        camara.vai()
        if camara in self._cripta:
            camara.texto("voce perdeu", lambda:None)
        else:
            self._cripta.append(camara)
            camara.segue(self.vai, nada)
            #alert(self._tumba)


class Tesouro:
    """ O jogo do Tesouro Inca """
    JOGO = None
    def __init__(self):
        Tesouro.JOGO = self
        self.templo = Camara(TEMPLO)
        #self.tesouro = Camara(TESOURO)
        self.tesouro = Tumba()
        self.cabana = Camara(CABANA)
        self.mochila = 0
                
    def termina(self):
        self.cabana = Camara(CABANA, self.mochila)
        self.cabana.vai()
        self.cabana.texto(f"Você ficou com {self.mochila} tesouros", lambda: None)
                
    def recebe(self, quantia):
        self.mochila += quantia
                
    def escolheu(self, resposta):
        if resposta == "A":
            self.tesouro.vai()
            #self.cabana.vai()
        else:
            self.cabana.vai()
        
    def vai(self):
        """ Inicia o jogo """
        self.templo.vai()
        self.templo.texto("Vai se aventurar?", foi=self.escolheu, A="sim", B="não")
        #Texto(self.templo, "Vai se aventurar?", A="sim", B="não", foi=self.escolheu).vai()


Tesouro().vai()